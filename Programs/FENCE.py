# test_cases = int(input())
# plants = []
#
#
# # print(test_cases)
# def getFences(plant_pos, n, m, num_plants):
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if [i,j] in plant_pos:
#                 print(i,j)
#                 # i,j == plant_pos[i,j]
#             pass
#         pass
#     pass
#
#
# for test_case in range(test_cases):
#     temp_y = []
#     n, m, num_plants = map(int, input().rstrip().split())
#     for _ in range(num_plants):
#         temp_x = list(map(int, input().rstrip().split()))
#         temp_y.append(temp_x)
#     plants.append(temp_y)
#     # print(test_case)
#     getFences(plants[test_case], n, m, num_plants)
#
# print(plants)

test_cases = int(input())
case_plant_pos = []


def count_fence(param, n, m, k):
    print(param)
    x = param[0]
    y = param[1]
    count = 0
    for i in range(k):
        if x[0] - 1 in x:
            if y[1] - 1 in y:
                pass
            else:
                count += 1
                flag = 1

    # for num in param:
    #     x = num // m
    #     y = num % m
    '''
    if x[i]-1 in x
        if y[i] in y:
            pass
        else
            count++
    else
        count++
    '''
    # print(param)
    pass


for test_case in range(test_cases):
    n, m, k = map(int, input().rstrip().split())
    plants_pos_arr, x, y = [], [], []
    for _ in range(k):
        _x, _y = map(int, input().rstrip().split())
        # temp = (_x * m) + _y
        x.append(_x)
        y.append(_y)
        # plants_pos_arr.append('_'.join(x))
        # plants_pos_arr.append()
    case_plant_pos.append([x, y])
    count_fence(case_plant_pos[test_case], n, m, k)
# print(case_plant_pos)
