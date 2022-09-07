from src.complex_task import complex_algorithm

def test_complex_algorithm_with_positive_input():
    input_low = 2.5
    input_high = 4.3
    adjustment_factor = 20.98
    expected_result = 111.70478758169938

    actual_result = complex_algorithm(input_high, input_low, adjustment_factor)

    assert expected_result == actual_result

def test_complex_algorithm_with_negative_input():
    input_low = -14.1
    input_high = -5.8
    adjustment_factor = -24.98
    expected_result = 424.6750330689593

    actual_result = complex_algorithm(input_high, input_low, adjustment_factor)

    assert expected_result == actual_result