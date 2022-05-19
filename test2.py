import random
from math import sqrt


class Vector:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def __str__(self):
        return str(self.line) + "," + str(self.column)


def user_random(bound):
    rand = random.random()
    if rand <= bound:
        result = 0
    else:
        result = 1
    return result


def gaming(b1, b2):
    summa = 0
    game = [[2, -3], [-1, 2]]
    results = []
    for i in range(100):
        res = (Vector(user_random(b1), user_random(b2)))
        n = game[res.line][res.column]
        results.append(n)
        summa += n
    return [summa, results]


sq = 0
res = gaming(0.5, 0.25)
p1 = 0.5
p2 = 0.25
s = res[0]
exp = 2 * p1 * p2 + 2 * (1 - p1) * (1 - p2) - 3 * p1 * (1 - p2) - (1 - p1) * p2
disp = 4 * p1 * p2 + 4 * (1 - p1) * (1 - p2) + 9 * p1 * (1 - p2) + (1 - p1) * p2 - exp**2
for i in res[1]:
    sq += (i - s / 99) ** 2
sq = sqrt(sq / 100)
print("Общий выигрыш", s)
print("Средний выигрыш", s / 100)
print("Матожидание", exp)
print("Среднеквадратичное отклонение", sq)
print("Дисперсия", disp)
print("Теор. среднее квадратичное отклонение", sqrt(disp))
