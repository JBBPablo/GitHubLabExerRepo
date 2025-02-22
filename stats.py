from collections import Counter

data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_numbers[n // 2]

def mode(numbers):
    count_dict = Counter(numbers)
    max_count = max(count_dict.values())
    
    if max_count == 1:  
        return None

    mode_list = [num for num, count in count_dict.items() if count == max_count]
    
    return mode_list[0] if len(mode_list) == 1 else mode_list

def mean(numbers):
    return sum(numbers) / len(numbers)

print(f"Median: {median(data)}")
print(f"Mode: {mode(data)}")
print(f"Mean: {mean(data)}")
