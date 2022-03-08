import turtle as t

# 삼각형
for x in range(4):
    t.color("red")
    t.fd(100)
    t.left(120)
    t.fd(100)
    t.left(120)
    t.fd(100)
    
    
# 사각형
for x in range(4):
    t.color("green")
    t.pensize(3)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)


# 원
for x in range(4):
    t.color("blue")
    t.pensize(5)
    t.circle(50)
    t.lt(90)

