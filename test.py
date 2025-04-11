def set_number(l):
    for i in range(1, len(l)):
        if not l[i] - l[i - 1] == 1:
            return l[i - 1] + 1
    return max(l) + 1


numbers = [0]

while True:
    event = input('Add or del window [1|2]: ')

    if event == '1':
        numbers.append(set_number(numbers))
        numbers.sort()
        print(f"Current list - {numbers}\n")

    elif event =='2':
        win_num = int(input('Chose del window number: '))
        del numbers[numbers.index(win_num)]
        print(f"list after del window - {numbers}\n")
