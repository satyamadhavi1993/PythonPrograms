def get_combinations(input):
    new_list = []
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            for k in range(j+1, len(input)):
                new_list.append((input[i], input[j], input[k]))
    return new_list

combinations = get_combinations([1, 2, 2, 3, 4])
print(f'All combinations of 3: {combinations}')
print(f'Unique combinations of 3: {set(combinations)}')
