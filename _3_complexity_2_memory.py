from memory_profiler import profile


def generate_numbers_range():
    return range(10_000_000)


def generate_numbers_list():
    return list(range(10_000_000))


def generate_numbers_tuple():
    return tuple(range(10_000_000))


def generate_numbers_set():
    return set(range(10_000_000))


@profile
def main():
    a = generate_numbers_range()
    b = generate_numbers_list()
    c = generate_numbers_tuple()
    d = generate_numbers_set()

    del a

    del d

    del c


if __name__ == '__main__':
    main()
