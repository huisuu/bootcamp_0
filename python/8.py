"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

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
