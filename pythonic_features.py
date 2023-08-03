import time
import itertools

# Custom Collection with iterators/generators
class CustomCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

# Decorator for calculating the time spent in a function
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Custom Data Structure with dunder methods
class CustomDataStructure:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __bool__(self):
        return self.value != 0

# Custom infinite Fibonacci sequence
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
