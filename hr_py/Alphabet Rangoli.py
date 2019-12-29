import string

size = int(input("Enter Size"))
letters = string.ascii_lowercase
w = 4 * size - 3

for i in list(range(size))[::-1] + list(range(1, size)):
    print('-'.join(letters[size - 1:i:-1] + letters[i:size]).center(w, '-'))
