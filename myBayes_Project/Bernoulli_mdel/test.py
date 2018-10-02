str= [1, 2, 3, 4, 5]
count = 0
for i in range(len(str)):
    if str[i] == 1:
        continue
    else:
        count += 1
print(count)