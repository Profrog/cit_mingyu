import turtle as t
t.shape('turtle')
b=0
a="{:06d}".format(b)
t.speed(0)
for i in range(65):
    t.pencolor('#'+ a)
    t.circle(100, steps=3)
    t.right(5)
    b+=3000