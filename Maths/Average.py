def average(nums):
    sum = 0
    n = 0
    for x in nums:
      sum += x
      n += 1
    avg = sum / n
    print("Average of numbers is : ",avg)

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
    average(fnos)

if __name__ == '__main__':
  main()