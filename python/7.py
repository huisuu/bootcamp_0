# 

def main():
    year = int(input())
    month = int(input())

    if month in [4, 6, 9, 11]:
        print(30)
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(29)
        else:
            print(28)
    else:
        print(31)
    return


if __name__ == '__main__':
    main()
