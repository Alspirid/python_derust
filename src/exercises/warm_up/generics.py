def first[T](array: list[T]) -> T:
    return array[0]


class Stack[T]:
    store: list[T]

    def __init__(
        self,
    ) -> None:
        self.store = []

    def push(self, item: T) -> None:
        self.store.append(item)

    def pop(self) -> T:
        return self.store.pop()


s = Stack[int]()
s.push(1)
s.push(2)
print(s.pop())  # → 2   (the checker knows it's an int)
