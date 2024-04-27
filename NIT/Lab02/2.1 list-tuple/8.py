import random


def fox_game():
    holes = [False] * 5
    fox_hole = random.randint(0, 4)
    holes[fox_hole] = True

    while True:
        guess = int(input("请选择一个洞口（0-4）："))
        if guess < 0 or guess > 4:
            print("请选择0到4之间的数字！")
            continue

        if holes[guess]:
            print("恭喜！你抓到了狐狸！")
            break
        else:
            print("很遗憾，这个洞口里没有狐狸。")
            fox_hole = (fox_hole + 1) % 5
            holes[fox_hole] = True


# 示例
fox_game()
