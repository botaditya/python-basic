def getlcm(num1, num2):
    max = num1 if num1 > num2 else num2
    lcm = max
    while (True):
        if ((lcm % num1 == 0) and (lcm % num2 == 0)):
            break
        lcm += max
    return lcm


def main():
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    print("The LCM of %s and %s is %s." % (num1,num2,getlcm(num1, num2)))


if __name__ == '__main__':
    main()