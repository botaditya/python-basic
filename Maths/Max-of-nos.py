def getmax(nos):
    max = nos[0]
    for x in nos:
      if x > max:
          max = x
    print("Maximum number is ",max)

def getdata():
    n = int(input("Enter how many numbers : "))
    nos = []
    print("Enter the Numbers : ")
    for i in range(n):
        num = int(input())
        nos.append(num)
    print(nos)
    return nos


def main():
    fnos = getdata()
    getmax(fnos)

if __name__ == '__main__':
    main()