
def main():
    nos = getdata()
    getmin(nos)

def getmin(nos):
    min = nos[0]
    for i in nos:
        if min > i:
            min = i
    print("Minimum number is : ",min)

def getdata():
    n = int(input("Enter how many numbers : "))
    nos = []
    print("Enter the Numbers : ")
    for i in range(n):
        num = int(input())
        nos.append(num)
    print(nos)
    return nos

if __name__ == '__main__':
    main()