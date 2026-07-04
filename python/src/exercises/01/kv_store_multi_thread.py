import threading
import time
from dataclasses import dataclass
from typing import TypedDict


class BackupItem(TypedDict):
    """JSON-serializable snapshot entry (relative TTL, not absolute expiry)."""

    val: str
    ttl: float | None


@dataclass(slots=True)
class _StoreItem:
    val: str
    expiry: float | None  # absolute time.monotonic() deadline, or None

    def is_expired(self, now: float) -> bool:
        return self.expiry is not None and self.expiry < now


class MemoryDB:
    """In-memory key-value store with per-key TTL. Thread-safe."""

    def __init__(self) -> None:
        self._store: dict[str, _StoreItem] = {}
        self._lock = threading.Lock()

    # -- internal helpers: caller must hold self._lock --

    def _get_live(self, key: str) -> _StoreItem | None:
        """Return the item if present and unexpired; evict and return None otherwise."""
        item = self._store.get(key)
        if item is None:
            return None
        if item.is_expired(time.monotonic()):
            del self._store[key]
            return None
        return item

    def _purge_all(self) -> None:
        now = time.monotonic()
        expired = [k for k, item in self._store.items() if item.is_expired(now)]
        for key in expired:
            del self._store[key]

    # -- public API --

    def set(self, key: str, value: str, ttl: float | None = None) -> None:
        if ttl is not None and ttl < 0:
            raise ValueError(f"ttl must be non-negative, got {ttl}")
        expiry = time.monotonic() + ttl if ttl is not None else None
        with self._lock:
            self._store[key] = _StoreItem(val=value, expiry=expiry)

    def get(self, key: str) -> str | None:
        with self._lock:
            item = self._get_live(key)
            return item.val if item is not None else None

    def delete(self, key: str) -> bool:
        with self._lock:
            if self._get_live(key) is None:
                return False
            del self._store[key]
            return True

    def __len__(self) -> int:
        with self._lock:
            self._purge_all()
            return len(self._store)

    def items_sorted(self, reverse: bool = False) -> list[tuple[str, str]]:
        with self._lock:
            self._purge_all()
            return sorted(
                ((key, item.val) for key, item in self._store.items()),
                reverse=reverse,
            )

    def backup(self) -> dict[str, BackupItem]:
        with self._lock:
            self._purge_all()
            now = time.monotonic()
            return {
                key: BackupItem(
                    val=item.val,
                    ttl=item.expiry - now if item.expiry is not None else None,
                )
                for key, item in self._store.items()
            }

    def restore(self, backup: dict[str, BackupItem]) -> None:
        now = time.monotonic()
        restored = {
            key: _StoreItem(
                val=d["val"],
                expiry=d["ttl"] + now if d["ttl"] is not None else None,
            )
            for key, d in backup.items()
        }
        with self._lock:
            self._store = restored
