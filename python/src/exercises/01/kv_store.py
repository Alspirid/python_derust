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


class MemoryDB:
    _MISSING = object()
    store: dict[str, tuple[str, float | None]]

    def __init__(self) -> None:
        self.store = {}

    def set(self, key: str, value: str, ttl: float | None = None) -> None:
        if not key:
            raise ValueError("key can not be empty")
        expiry: float | None

        if ttl is not None and ttl > 0.0:
            expiry = time.monotonic() + ttl
        else:
            expiry = None
        self.store[key] = (value, expiry)

    def _is_expired(self, key) -> bool:
        result = self.store.get(key)
        if result is None:
            return False

        _, expiry = result
        if expiry is not None and time.monotonic() > expiry:
            del self.store[key]
            return True

        return False

    def get(self, key: str) -> str | None:
        self._is_expired(key)
        result = self.store.get(key)
        return result[0] if result else None

    def delete(self, key: str) -> bool:
        self._purge_all()
        val = self.store.pop(key, self._MISSING)
        return val is not self._MISSING

    def _purge_all(self) -> None:
        for k in list(self.store):
            self._is_expired(k)

    def __len__(self) -> int:
        self._purge_all()
        return len(self.store)

    def items_sorted(self, reverse: bool = False) -> list[tuple[str, str]]:
        self._purge_all()
        return [
            (x[0], x[1][0])
            for x in sorted(self.store.items(), key=lambda x: x[0], reverse=reverse)
        ]

    def backup(self) -> dict:
        self._purge_all()
        now = time.monotonic()
        return {
            k: {"value": v, "ttl": exp - now if exp is not None else None}
            for k, (v, exp) in self.store.items()
        }

    def restore(self, snapshot: dict) -> None:
        now = time.monotonic()
        self.store = {
            k: (d["value"], now + d["ttl"] if d["ttl"] is not None else None)
            for k, d in snapshot.items()
        }


db = MemoryDB()

db.set("permanent", "stays")
db.set("temp", "goes", ttl=10.0)
time.sleep(2.0)

snap = db.backup()
print(snap)
# "temp" should have ~8s remaining, not 10

db2 = MemoryDB()
db2.restore(snap)
db2.get("permanent")  # "stays"
print(db2.get("temp"))  # "goes" (with ~8s left)
