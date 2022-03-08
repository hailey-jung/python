s = 0
x = 1
while x <= 10:
    s = s + x
    print("x:", x, "s:", s)
    x = x + 1

#for x in range 와의 차이
s = 0
for x in range(1, 11):
    s = s + x
    print("x:", x, "s:", s)
