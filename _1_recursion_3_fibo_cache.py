import time
from functools import lru_cache


# cache implementovana pomoci default mutable parametru - default hodnota cache je vytvorena pri deklaraci funkce a potom muze byt sdilena
def fibo_simple_cache(nth: int, cache: dict = dict()) -> int:
    if nth <= 0:
        raise ValueError("fibo defined for positive numbers")

    if nth == 1:
        return 0
    if nth == 2:
        return 1

    else:
        # pokud je n-ty clen uz v pameti, ziskame ho odtamtud ...
        if (nth - 1) in cache.keys():
            previous_fibo = cache[(nth - 1)]
        else:
            # ... jinak ho spocitame a ulozime do pameti
            previous_fibo = fibo_simple_cache(nth - 1)
            cache[(nth - 1)] = previous_fibo

        return previous_fibo + fibo_simple_cache(nth - 2)


# muzeme dojit k vyssim hodnotam i - protoze nedochazi prakticky k zadnemu zpomaleni
for i in range(1, 50):
    t0 = time.time()
    result = fibo_simple_cache(i)
    duration = time.time() - t0
    print(f"Fibo({i}) = {result}, Duration: {duration}")

# introspekci muzeme zjistit, kde ve funkci je ulozena cache ...
fibo_simple_cache
dir(fibo_simple_cache)
fibo_simple_cache.__defaults__[0].clear()


# Fibonacci calculator pomoci classy - lepsi implementace cache
class Fibo:

    def __init__(self) -> None:
        self._cache = dict()

    def __call__(self, nth: int) -> int:
        if nth == 1:
            return 0
        if nth == 2:
            return 1

        if (nth - 1) in self._cache.keys():
            previous_fibo = self._cache[(nth - 1)]
        else:
            previous_fibo = self(nth - 1)
            self._cache[(nth - 1)] = previous_fibo

        return previous_fibo + self(nth - 2)

    def reset_cache(self):
        self._cache.clear()


fibo = Fibo()
fibo(30)
fibo._cache


# pouzijeme lru cache z functools - funguje pouze pro hashable argumenty, ale je vyrazne jednodussi na implementaci (jen dekorace funkce)
@lru_cache(maxsize=500)
def fibo_with_lru(nth: int) -> int:
    if nth <= 0:
        raise ValueError("fibo defined for positive numbers")

    if nth == 1:
        return 0
    if nth == 2:
        return 1
    else:
        return fibo_with_lru(nth - 1) + fibo_with_lru(nth - 2)


fibo_with_lru(40)


# ukazka fungovani cache - funkce je u opakovanych argumentu uplne vynechana a odpovida se pomoci zname hodnoty z cache
@lru_cache(100)
def fn(a):
    print(f"Called with {a}")
    time.sleep(2)
    return a * 2


print(fn(30))
print(fn((30, 20)))
print(fn(set([30, 20])))

my_list = [1, 2, 3]
list(fn(tuple(my_list)))

# unhashable argumenty nefunguji dohromady s lru cache
fn(["asdf", 1234])

# co je to hash?
hash("ahoj")
hash(1.23)

{
    "a": 123
}

630198673033659366
hash((1, 2, 3, 4))

hash([1, 2, 3])

d = dict()
# unhashable objekty nelze pouzit jako klice v dictionary
d[[1, 2, 3]] = 123
