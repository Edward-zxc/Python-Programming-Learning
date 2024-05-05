class Character:
    def __init__(self, name, gender, age, initial_power):
        self.name = name
        self.gender = gender
        self.age = age
        self.power = initial_power

    def __str__(self):
        return f"{self.name} {self.gender}, {self.age} years old  Power: {self.power}"

    def battle_in_bush(self):
        if self.power >= 200:
            self.power -= 200
            print(f"{self.name} 在草丛战斗中消耗了200战斗力，当前战斗力为 {self.power}.")
        else:
            print(f"{self.name} 战斗力不足，无法进行草丛战斗.")

    def self_training(self):
        self.power += 100
        print(f"{self.name} 进行了自我修炼，增长了100战斗力，当前战斗力为 {self.power}.")

    def multiplayer_game(self):
        if self.power >= 500:
            self.power -= 500
            print(f"{self.name} 参加了多人游戏，消耗了500战斗力，当前战斗力为 {self.power}.")
        else:
            print(f"{self.name} 战斗力不足，无法参加多人游戏.")

player_a = Character("小A", "女", 18, 1000)
player_b = Character("小B", "男", 20, 1800)
player_c = Character("小C", "女", 19, 2500)
print(player_a)
print(player_b)
print(player_c)
player_a.battle_in_bush()
player_b.self_training()
player_c.multiplayer_game()