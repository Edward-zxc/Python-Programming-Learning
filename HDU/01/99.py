def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if 2 <= length <= 6:
        if s[0:2].isalpha():
            for i in range(1, length - 1):
                if s[i].isdigit():
                    if s[i - 1].isalpha() and s[i + 1].isalpha():
                        return False
            return True
        for i in range(length):
            if not s[i].isalpha() or not s[i].isdigit():
                return False
    else:
        return False


main()
