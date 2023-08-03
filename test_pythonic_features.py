import unittest
import time
from pythonic_features import CustomCollection, timing_decorator, CustomDataStructure, fibonacci_sequence

class TestCustomCollection(unittest.TestCase):
    def test_for_in_loop(self):
        collection = CustomCollection()
        collection.add_item(1)
        collection.add_item(2)
        collection.add_item(3)

        result = [item for item in collection]
        self.assertEqual(result, [1, 2, 3])

    def test_list_comprehension(self):
        collection = CustomCollection()
        collection.add_item(1)
        collection.add_item(2)
        collection.add_item(3)

        result = [item ** 2 for item in collection]
        self.assertEqual(result, [1, 4, 9])

    def test_convert_to_list(self):
        collection = CustomCollection()
        collection.add_item(1)
        collection.add_item(2)
        collection.add_item(3)

        result = list(collection)
        self.assertEqual(result, [1, 2, 3])


class TestTimingDecorator(unittest.TestCase):
    def test_function_execution_time(self):
        @timing_decorator
        def slow_function():
            time.sleep(2)
            return "Function executed successfully!"

        result = slow_function()
        self.assertEqual(result, "Function executed successfully!")


class TestCustomDataStructure(unittest.TestCase):
    def test_custom_data_structure_equality(self):
        data_structure1 = CustomDataStructure(10)
        data_structure2 = CustomDataStructure(10)
        data_structure3 = CustomDataStructure(0)

        self.assertEqual(data_structure1, data_structure2)
        self.assertNotEqual(data_structure1, data_structure3)

    def test_custom_data_structure_truthiness(self):
        data_structure1 = CustomDataStructure(10)
        data_structure2 = CustomDataStructure(0)

        self.assertTrue(data_structure1)
        self.assertFalse(data_structure2)


class TestFibonacciSequence(unittest.TestCase):
    def test_fibonacci_sequence_generation(self):
        fib_sequence = fibonacci_sequence()
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        for i, fib_num in zip(range(10), fib_sequence):
            self.assertEqual(fib_num, expected_sequence[i])


if __name__ == "__main__":
    unittest.main()
