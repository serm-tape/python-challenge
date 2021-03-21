# What this function do?
def doSomething(numbers):
    for i in range(0, len(numbers)):
        m = i
        for j in range(i + 1, len(numbers)):
            if numbers[m] < numbers[j]:
                m = j

        tmp = numbers[i]
        numbers[i] = numbers[m]
        numbers[m] = tmp

    return numbers


input_list = [4, 9, 10, 12, 6, 7, 8]
output = doSomething(input_list)
print(output)
