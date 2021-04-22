import unittest


def add_one(x):
    return x + 1


def subtract_one(x):
    return x - 1


class ExampleTests(unittest.TestCase):
    def test_add_one__returns_correct_result__with_valid_input(self):
        # Arrange
        input_value = 3
        expected_output_value = 4

        # Act
        actual_output_value = add_one(input_value)

        # Assert
        self.assertEqual(expected_output_value, actual_output_value)

    def test_subtract_one__returns_correct_result__with_valid_input(self):
        # Arrange
        input_value = 100
        expected_output_value = 99

        # Act
        actual_output_value = subtract_one(input_value)

        # Assert
        self.assertEqual(expected_output_value, actual_output_value)
