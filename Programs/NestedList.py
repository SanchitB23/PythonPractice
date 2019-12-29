res = []
sort = []
names = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    res.append([name, score])
    sort.append(res[_][1])
    sort = sorted(sort)
# print(sort)

# find sec_last
for i in range(len(sort) - 1):
    if sort[i + 1] != sort[i]:
        sm = sort[i + 1]
        break

# print(sm)

for i in range(len(res)):
    if sm == res[i][1]:
        names.append(res[i][0])
    names.sort()

for name in names:
    print(name)
