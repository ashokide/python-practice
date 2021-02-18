




myList = list('hello')

for i in range(0,(len(myList)//2)):
    myList[i],myList[len(myList)-i-1] = myList[len(myList)-i-1],myList[i]

print(myList)
