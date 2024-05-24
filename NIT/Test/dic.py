fruits = {
    "苹果": 200,
    "香蕉": 180,
    "草莓": 320,
    "西瓜": 480
}

# 输出所有元素
print("水果数据：")
for fruit, quantity in fruits.items():
    print(f"{fruit}: {quantity}斤")

prices = {
    "苹果": 4.5,
    "香蕉": 6.2,
    "草莓": 10.8,
    "西瓜": 1.5
}

print("\n水果价格：")
for fruit, quantity in fruits.items():
    price_per_kg = prices[fruit]
    total_price = price_per_kg * quantity
    print(f"{fruit}: {total_price:.2f}元")
