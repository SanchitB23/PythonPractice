size = int(input())

num = list(map(int, input().rstrip().split()))
mod = 0
# for i in range(size):
#     for j in range(size):
#         temp = num[i] % num[j]
#         if temp >= mod:
#             mod = temp
num.sort(reverse=True)
second = num[0]
flag = 0
for i in range(len(num) - 1):
    # calc second largest
    if num[i + 1] != num[i]:
        second = num[i + 1]
        flag = 1
        break
    # if second % max(num) > mod:
    #     mod = second % max(num)
if flag == 0:
    print(0)
else:
    print(second)

# print(num)
# print(mod)
