"""
Implement a class MemoryDB that supports three operations:

set(key: str, value: str) -> None — store a key-value pair
get(key: str) -> str | None — retrieve by key, return None if missing
delete(key: str) -> bool — remove a key, return True if it existed, False otherwise

Also add __len__ so len(db) returns the number of stored keys.

items_sorted(reverse: bool = False) -> list[tuple[str, str]]
— return all key-value pairs sorted alphabetically by key. When reverse=True, sort descending.


"""

import time
from typing import TypedDict

_MISSING = object()


class StoreItem(TypedDict):
    val: str
    expiry: float | None


class BackupItem(TypedDict):
    val: str
    ttl: float | None


class MemoryDB:
    store: dict[str, StoreItem]

    def __init__(self) -> None:
        self.store = {}

    def _is_expired(self, key: str) -> bool:
        store_item = self.store.get(key)
        if store_item is None:
            return False

        expiry = store_item["expiry"]
        if expiry is not None and expiry < time.monotonic():
            del self.store[key]
            return True

        return False

    def set(self, key: str, value: str, ttl: float | None = None) -> None:
        if ttl is not None and ttl < 0:
            raise ValueError(f"ttl must be non-negative, got {ttl}")
        expiry = time.monotonic() + ttl if ttl is not None else None
        self.store[key] = {"val": value, "expiry": expiry}

    def get(self, key: str) -> str | None:
        if self._is_expired(key):
            return None
        result = self.store.get(key)
        return result["val"] if result else None

    def delete(self, key: str) -> bool:
        self._is_expired(key)
        return self.store.pop(key, _MISSING) is not _MISSING

    def _purge_all(self) -> None:
        for key in list(self.store):
            self._is_expired(key)

    def __len__(self) -> int:
        self._purge_all()
        return len(self.store)

    def items_sorted(self, reverse: bool = False) -> list[tuple[str, str]]:
        self._purge_all()
        return [
            (key, d["val"])
            for (key, d) in sorted(
                self.store.items(), key=lambda kv: kv[0], reverse=reverse
            )
        ]

    def backup(self) -> dict[str, BackupItem]:
        self._purge_all()
        now = time.monotonic()
        backup: dict[str, BackupItem] = {}
        for key, d_value in self.store.items():
            ttl = d_value["expiry"] - now if d_value["expiry"] is not None else None
            backup[key] = {"val": d_value["val"], "ttl": ttl}
        return backup

    def restore(self, backup: dict[str, BackupItem]) -> None:
        now = time.monotonic()
        restored: dict[str, StoreItem] = {}
        for k, d in backup.items():
            expiry = d["ttl"] + now if d["ttl"] is not None else None
            restored[k] = {"val": d["val"], "expiry": expiry}

        self.store = restored


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
