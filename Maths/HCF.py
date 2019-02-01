def gethcf(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    # Base Case
    if num1 == num2:
        return num1
    if num1 > num2:
        return gethcf(num1 - num2, num2)
    return gethcf(num1, num2 - num1)


def main():
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    print('The HCF of %s and %s is %s' % (num1, num2, gethcf(num1, num2)))


if __name__ == '__main__':
    main()