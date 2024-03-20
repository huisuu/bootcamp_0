# 

def main():
    while True:
        n = int(input())
        if n > 0:
            break
        else:
            print("X")

    sum_of_integers = sum(range(1, n + 1))
    print(sum_of_integers)

    return


if __name__ == '__main__':
    main()
