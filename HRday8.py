# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook={}
n=int(input())
for i in range(0,n):
    key, value = input().split()
    phoneBook.update({key:value})

while 1:
    try:
        key=input()
        if key in phoneBook:
            value = phoneBook[key]
            print(key + "=" + str(value))
        else:
            print("Not found")
    except:
        break
