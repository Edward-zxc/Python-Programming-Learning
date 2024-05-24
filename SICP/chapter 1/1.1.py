def printTraninggle():
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i), "*" * (2 * i - 1))


printTraninggle()


def print_99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, "*", i, "=", j * i, end="\t")
        print()


print_99()

def bubbleSort():
    list_a = [37,52,5,2,6,6,7,9]
    for i in range(len(list_a)):
        for j in range(len(list_a)-i-1):
            if list_a[j]>list_a[j+1]:
                list_a[j+1],list_a[j]=list_a[j],list_a[j+1]
    list_a.reverse()
    print(list_a)

bubbleSort()