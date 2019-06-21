


while True:
    print("Jest to program, do wskazywania największej liczby\nsposród 3 podanych prze Ciebie\n")
    print("write number 1:")
    num1 = input()
    print("write number 2:")
    num2 = input()
    print("write number 3:")
    num3 = input()
    if num1 > num2 and num1>num3:
        print("the largest number is num1")
        break
    elif num2 > num1 and num2 > num3:
        print("the largest number is num2")
        break
    elif num3 > num1 and num3 > num2:
        print("the largest number is num3")
        break
