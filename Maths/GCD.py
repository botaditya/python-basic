def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def main():
    try:
        nos = input("Enter two Integers separated by comma (,): ").split(',')
        num1 = int(nos[0]) 
        num2 = int(nos[1])
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
    print(f"gcd({num1}, {num2}) = {gcd(num1, num2)}")

if __name__ == '__main__':
    main()