def normalize(numbers) -> list[float]:
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def normalize_copy(numbers: list[int]):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)

    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits:
    data_path: str

    def __init__(self, data_path: str):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits("some_file.txt")
percentages = normalize(visits)
