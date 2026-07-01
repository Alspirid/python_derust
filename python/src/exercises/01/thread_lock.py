import threading as t

e
class Counter:
    _counter: int
    _lock: t.Lock

    def __init__(self) -> None:
        self._counter = 0
        self._lock = t.Lock()

    def increment(self) -> None:
        with self._lock:
            self._counter += 1

    @property
    def value(self) -> int:
        return self._counter


# this should reliably print 50000, not a smaller racy number:

c = Counter()
threads = [
    t.Thread(target=lambda: [c.increment() for _ in range(5000)]) for _ in range(10)
]
for th in threads:
    th.start()
for th in threads:
    th.join()
print(c.value)
