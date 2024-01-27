#程式邏輯題目第二題
from collections import Counter
celebration_str = "Hello welcome to Cathay 60th year anniversary"

def count_str_func(data):
    data = str(data)
    counter_data = Counter(data.upper())
    tmp_set = set()

    filtered_elements = [char for char in data if char.isalnum()]
    unique_elements = set(filtered_elements)
    sorted_elements = sorted(unique_elements, key=lambda x: (not x.isnumeric(), x.upper()))

    for char in sorted_elements:
        if char.upper() not in tmp_set:
            tmp_set.add(char.upper())
            count_data = counter_data[char.upper()]
            print(f"{char.upper()} {count_data}")

count_str_func(celebration_str)
