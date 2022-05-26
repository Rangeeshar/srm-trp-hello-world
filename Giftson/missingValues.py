"""
python program to find the missing number from a sorted array
or print 0 if the there is no missing number

Sample Input:
2 3 4 5 7 8 9

Sample Output:
6 

"""
# present flag to indicate that there`s a missing value defaulted to False
present = False
# storing the values got in a list
nArray = list(map(int, input().split()))
# iterating through individual elements and comparing with the next element
for i in range(len(nArray) - 1):
    # if 2 sequential values are present then, the average of them is a fraction
    # so if 2 non sequential values are found then the average of the remainder is 0
    if (nArray[i] + nArray[i + 1]) % 2 == 0:
        print(nArray[i] + 1)
        present = True
        break
    else:
        continue
if present == False:
    print(0)
