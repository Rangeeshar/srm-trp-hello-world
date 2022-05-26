present = False
nArray = list(map(int, input().split()))
for i in range(len(nArray) - 1):
    if (nArray[i] + nArray[i + 1]) % 2 == 0:
        print(nArray[i] + 1)
        present = True
        break
    else:
        continue
if present == False:
    print(0)
