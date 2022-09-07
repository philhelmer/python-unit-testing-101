from src.complex_task import complex_algorithm

def test_complex_algorithm_with_positive_input():
    # Arrange
    input_low = 2.5
    input_high = 4.3
    adjustment_factor = 20.98
    expected_result = 111.70478758169938

    # Act
    actual_result = complex_algorithm(input_high, input_low, adjustment_factor)

    # Assert
    assert expected_result == actual_result


def test_complex_algorithm_with_negative_input():
    # Arrange
    input_low = -14.1
    input_high = -5.8
    adjustment_factor = -24.98
    expected_result = 424.6750330689593

    # Act
    actual_result = complex_algorithm(input_high, input_low, adjustment_factor)

    # Assert
    assert expected_result == actual_result