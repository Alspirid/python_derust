"""In-memory key-value store with sorted output, TTL, and backup/restore."""

import time
from typing import TypedDict


class SnapshotEntry(TypedDict):
    value: str
    ttl: float | None


_MISSING = object()


class MemoryDB:
    """A simple in-memory key-value store with TTL support."""

    store: dict[str, tuple[str, float | None]]

    def __init__(self) -> None:
        self.store = {}

    # ── Core Operations ──────────────────────────────────────────────

    def set(self, key: str, value: str, ttl: float | None = None) -> None:
        if not key:
            raise ValueError("key cannot be empty")
        expiry = time.monotonic() + ttl if ttl is not None else None
        self.store[key] = (value, expiry)

    def get(self, key: str) -> str | None:
        self._is_expired(key)
        result = self.store.get(key)
        return result[0] if result else None

    def delete(self, key: str) -> bool:
        self._is_expired(key)
        return self.store.pop(key, _MISSING) is not _MISSING

    def __len__(self) -> int:
        self._purge_all()
        return len(self.store)

    # ── Sorted Output ────────────────────────────────────────────────

    def items_sorted(self, reverse: bool = False) -> list[tuple[str, str]]:
        self._purge_all()
        return [(k, v) for k, (v, _) in sorted(self.store.items(), reverse=reverse)]

    # ── Backup / Restore ─────────────────────────────────────────────

    def backup(self) -> dict[str, SnapshotEntry]:
        self._purge_all()
        now = time.monotonic()
        return {
            k: {"value": v, "ttl": exp - now if exp is not None else None}
            for k, (v, exp) in self.store.items()
        }

    def restore(self, snapshot: dict[str, SnapshotEntry]) -> None:
        now = time.monotonic()
        self.store = {
            k: (str(d["value"]), now + d["ttl"] if d["ttl"] is not None else None)
            for k, d in snapshot.items()
            if d["ttl"] is None or d["ttl"] > 0
        }

    # ── Internal Helpers ─────────────────────────────────────────────

    def _is_expired(self, key: str) -> bool:
        result = self.store.get(key)
        if result is None:
            return False
        _, expiry = result
        if expiry is not None and time.monotonic() > expiry:
            del self.store[key]
            return True
        return False

    def _purge_all(self) -> None:
        for k in list(self.store):
            self._is_expired(k)


# ── Quick smoke test ─────────────────────────────────────────────────

if __name__ == "__main__":
    db = MemoryDB()

    # basic ops
    db.set("banana", "yellow")
    db.set("apple", "red")
    db.set("cherry", "dark red")
    assert db.get("apple") == "red"
    assert db.get("missing") is None
    assert len(db) == 3

    # delete
    assert db.delete("banana") is True
    assert db.delete("banana") is False
    assert len(db) == 2

    # sorted output
    db.set("banana", "yellow")
    assert db.items_sorted() == [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "dark red"),
    ]
    assert db.items_sorted(reverse=True)[0] == ("cherry", "dark red")

    # TTL
    db.set("temp", "gone soon", ttl=0.1)
    assert db.get("temp") == "gone soon"
    time.sleep(0.15)
    assert db.get("temp") is None
    assert len(db) == 3

    # edge: ttl=0.0 expires immediately
    db.set("instant", "poof", ttl=0.0)
    time.sleep(0.01)
    assert db.get("instant") is None

    # edge: empty-string value
    db.set("empty", "")
    assert db.get("empty") == ""
    assert db.delete("empty") is True

    # backup / restore
    db2 = MemoryDB()
    db2.set("permanent", "stays")
    db2.set("expiring", "ticking", ttl=10.0)
    time.sleep(0.1)

    snap = db2.backup()
    assert snap["permanent"]["ttl"] is None
    assert 0 < snap["expiring"]["ttl"] < 10.0

    db3 = MemoryDB()
    db3.restore(snap)
    assert db3.get("permanent") == "stays"
    assert db3.get("expiring") == "ticking"
    assert len(db3) == 2

    print("All tests passed.")
