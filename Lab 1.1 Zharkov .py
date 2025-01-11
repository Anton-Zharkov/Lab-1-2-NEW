numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = numbers.index(None)
valid_numbers = [num for num in numbers if num is not None]
average_value = sum(valid_numbers) / len(numbers)
numbers[missing_index] = average_value# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)