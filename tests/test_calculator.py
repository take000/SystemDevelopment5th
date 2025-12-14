"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting two positive numbers."""
        # Arrange
        a = 10
        b = 4
        expected = 6

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self, calc):
        """Test subtracting a negative from a positive."""
        # Arrange
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self, calc):
        """Test subtracting a positive from a negative."""
        # Arrange
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_with_zero(self, calc):
        """Test subtracting zero from a positive number."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_positive(self, calc):
        """Test subtracting a positive number from zero."""
        # Arrange
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self, calc):
        """Test subtracting floating point numbers."""
        # Arrange
        a = 5.5
        b = 2.2
        expected = 3.3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying two positive numbers."""
        # Arrange
        a = 6
        b = 7
        expected = 42

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self, calc):
        """Test multiplying two negative numbers."""
        # Arrange
        a = -4
        b = -5
        expected = 20

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self, calc):
        """Test multiplying a positive and a negative number."""
        # Arrange
        a = 4
        b = -3
        expected = -12

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_by_zero(self, calc):
        """Test multiplying by zero."""
        # Arrange
        a = 9
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero_by_positive(self, calc):
        """Test multiplying zero by a positive number."""
        # Arrange
        a = 0
        b = 9
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self, calc):
        """Test multiplying floating point numbers."""
        # Arrange
        a = 2.5
        b = 1.2
        expected = 3.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing two positive numbers."""
        # Arrange
        a = 20
        b = 4
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self, calc):
        """Test dividing two negative numbers."""
        # Arrange
        a = -12
        b = -3
        expected = 4

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_and_negative(self, calc):
        """Test dividing a positive by a negative number."""
        # Arrange
        a = 12
        b = -3
        expected = -4

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_and_positive(self, calc):
        """Test dividing a negative by a positive number."""
        # Arrange
        a = -12
        b = 3
        expected = -4

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_zero_by_positive(self, calc):
        """Test dividing zero by a positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        # Arrange
        a = 7.5
        b = 2.5
        expected = 3.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_by_zero_raises_value_error(self, calc):
        """Test dividing by zero raises ValueError."""
        # Arrange
        a = 5
        b = 0

        # Act / Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)
