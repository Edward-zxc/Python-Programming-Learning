class redpacket:
    def __init__(self,money):
        self.money=money
        self.Trag=False
    def get_red_packer(self):
        if self.Trag:
            print('你已经领过了红包')
        else:
            self.Trag=True
            print(f"恭喜你抢到{self.money}元红包")

class group_red_packer(redpacket):
    def __init__(self,number,money):
        if number <= 0 or money <= 0:
            raise ValueError("红包个数和金额必须大于0")
        super().__init__(number)
        self.number = number
        self.money = money

    def grab_red_packet(self):
        if self.number <= 0:
            print("你来晚了，红包已经抢完啦")
        else:
            grabbed_amount = round(self.money / self.number, 2)
            self.number -= 1
            self.money -= grabbed_amount
            print(f"恭喜你抢到{grabbed_amount}元红包")
try:

    print("普通红包:")
    red_packet = redpacket(10)
    red_packet.get_red_packer()
    red_packet.get_red_packer()


    print("\n群红包:")
    group_red_packet = group_red_packer(3, 20)
    group_red_packet.grab_red_packet()
    group_red_packet.grab_red_packet()
    group_red_packet.grab_red_packet()
    group_red_packet.grab_red_packet()

except ValueError as e:
    print("输入错误:", e)