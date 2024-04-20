import turtle

# 设置turtle
t = turtle.Turtle()
t.speed(2)

# 绘制图像
for _ in range(4):
    t.forward(100)
    t.right(90)

# 结束绘制
turtle.done()
