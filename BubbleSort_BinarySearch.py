l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def b_sort(a):
    j = 0
    while j < len(a) - 1:
        i = 0
        while i < len(a) - 1:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            i = i + 1
        j = j + 1

b_sort(l)
print(l)

def b_search(a, e):
    l = len(a)
    left = 0
    right = l - 1
    while left <= right:
        mid = (left + right) // 2
        if e == a[mid]:
            print('Number ' + str(e) + ' is Found ')
            break
        elif e < a[mid]:
            right = mid - 1
        elif e > a[mid]:
            left = mid + 1
    else:
        print('Number ' + str(e) + ' is Not Found ')

se = 10
b_search(l, se)
