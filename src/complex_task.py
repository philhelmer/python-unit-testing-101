def complex_algorithm(input_low: float, input_high: float, adjustment_factor: float) -> float:
    first_intermediate_result = input_low / (input_high - input_low)
    second_intermediate_result = (adjustment_factor * input_high) / (input_low + input_high)
    final_result = (first_intermediate_result + second_intermediate_result) * adjustment_factor
    return final_result


if __name__ == "__main__":
    result = complex_algorithm(2.5, 4.3, 20.98)
    print(f'the result is {result}')

