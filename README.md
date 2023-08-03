# Pythonic Features

Pythonic Features is a project that demonstrates various pythonic language features to improve code readability, maintainability, and functionality. It showcases examples of using iterators/generators, decorators, dunder methods, and more.

## Contents

The project consists of two files:

1. `pythonic_features.py`: This file contains the implementation of custom classes and functions that showcase pythonic language features.
2. `test_pythonic_features.py`: This file contains unit tests for the examples in `pythonic_features.py`.

## Features

### Custom Collection with Iterators/Generators

`CustomCollection` is a class that demonstrates the use of iterators and generators. It allows you to add items to a custom collection and use it in a for-in loop, list comprehension, or convert it to a list.

### Decorator for Function Behavior

The `timing_decorator` is a decorator function that calculates the time spent in a given function. It can be used to add behavior such as logging relevant info, slowing down the function, converting the return value, or validating some condition on the way in.

### Dunder Methods for Readability and Elegance

`CustomDataStructure` is a class that demonstrates the use of dunder methods (`__eq__` and `__bool__`). It adds the ability for two custom data structures to be considered equal and the ability for a custom data structure to be considered truthy or falsy.

### Custom Infinite Fibonacci Sequence

`fibonacci_sequence` is a function that generates an infinite Fibonacci sequence using generators. It showcases how to create and use a custom iterator with an infinite sequence.

## Running the Tests

To run the unit tests for the examples in `pythonic_features.py`, you can execute the following command:

```bash
python test_pythonic_features.py
