# 

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    n = int(input())

    sum_of_integers = sum(range(n + 1))
    factorial_of_n = factorial(n)

    print(sum_of_integers)
    print(factorial_of_n)


if __name__ == '__main__':
    main()
