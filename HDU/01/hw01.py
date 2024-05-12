def main():
    x,y = get_fraction("Fraction: ").split('/')
    temp = (int(x) / int(y)) * 100
    round_temp = round(temp)
    if temp <= 1:
        print('E')
    elif temp >= 99:
        print('F')
    else:
        print(f'{round_temp}%',end = "")


def get_fraction(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
