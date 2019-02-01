import math
def checkPrime(num):
    if num%2 == 0 and num>2: 
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

def main():
    num = int(input("Enter a Number : "))
    print(checkPrime(num))

if __name__ == '__main__':
	main()