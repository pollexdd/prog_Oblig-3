# fikk hjelp fra denne nettsiden: https://cuny.manifoldapp.org/read/how-to-code-in-python-3/section/46d41008-33ca-4f32-9937-7ddb9a86c5ce

from random import randrange


def volum_funk(*args):
    x = 1
    for num in args:
        x *= num
    print(x)

volum_funk(6,2,7)
volum_funk(1,2,9)
volum_funk(3,2,7)
volum_funk(4,1,7)
volum_funk(2,2,9)