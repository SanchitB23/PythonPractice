test_cases = int(input())  # Test Cases
data_array = []


def count_subString(param):
    a = [-1]
    count = 0  # [arr,char,n]
    i = 0
    if param[-1] == 1:
        if param[0] == param[-2]:
            count = count + 1
    else:
        while i < param[-1]:
            if param[0][i] == param[1]:
                a.append(i)
                count = count + 1
            i = i + 1
        i = 1
        while i < len(a):
            n1 = a[i] - a[i - 1] - 1
            n2 = param[-1] - a[i] - 1
            count = count + n1 + n2 + n1 * n2
            i = i + 1
    return count


for _ in range(0, test_cases):
    n = int(input())  # length of str
    strings = list(map(str, input().rstrip().split()))
    strings.append(n)
    data_array.append(strings)
for pos in data_array:
    res = count_subString(pos)
    print(res)
