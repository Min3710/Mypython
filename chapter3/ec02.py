import turtle
t=turtle.Turtle()
t.shape("turtle")

n=int(input("몇각형을 그리시겠습니까"))
angle=360//n

for i in range(n):
    t.forward(30)
    t.left(angle)

