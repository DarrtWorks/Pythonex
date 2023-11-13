#To check the frequency of the given interger in inputed array.
#To input in an array/list we use array.append()
arr =[]

n = int(input("How many elements are in the array?"))


for i in range(n):
    arr.append(int(input("please enter an element:")))

f = 0
d = input("Frequency of which number do you want to find?")

for j in arr:
    if j == d:
        f = f + 1

print("Frequency of",d,"is:",f)        