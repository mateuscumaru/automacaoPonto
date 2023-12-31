import math
import random


'''
for x in range(33):
    print('GB_l%s_lblData / GB_l%s_lblDia / GB_l%s_txtEnt1 / GB_l%s_txtSai1' % (x, x, x, x))
'''


def retorna_ponto(dias_uteis):

    mins_trab = 0
    ponto = []

    for n in range(dias_uteis):
        hr_inicio = random.randint(8, 9)

        if hr_inicio == 9:
            hr_fim = 18
        else:
            hr_fim = 17

        min_inicio = random.randint(0, 59)

        if n == dias_uteis - 1:
            hr_inicio = math.floor((480 - mins_trab) / 60)
            min_inicio = (480 - mins_trab) % 60
            if mins_trab > 0:
                hr_fim = (hr_inicio + 9) - math.ceil((mins_trab - min_inicio) / 60)
                min_fim = (min_inicio - abs(mins_trab)) % 60
            else:
                hr_fim = (hr_inicio + 9) + math.floor((abs(mins_trab) + min_inicio) / 60)
                min_fim = (min_inicio + abs(mins_trab)) % 60

        else:
            if n % 2 == 0:
                if min_inicio <= 10:
                    min_fim = random.randint(0, min_inicio)
                else:
                    min_fim = random.randint((min_inicio - 10), min_inicio)
            else:
                if min_inicio >= 50:
                    min_fim = random.randint(min_inicio, (min_inicio + (10 - (min_inicio - 49))))
                else:
                    min_fim = random.randint(min_inicio, (min_inicio + 10))

        mins_trab += (((((hr_fim - 1) * 60) - (hr_inicio * 60)) + (min_fim - min_inicio)) - 480)

        if len(str(hr_inicio)) == 1:
            hr_inicio = '0' + str(hr_inicio)
        if len(str(min_inicio)) == 1:
            min_inicio = '0' + str(min_inicio)
        if len(str(hr_fim)) == 1:
            hr_fim = '0' + str(hr_fim)
        if len(str(min_fim)) == 1:
            min_fim = '0' + str(min_fim)

        ponto.append([str(hr_inicio) + ':' + str(min_inicio), str(hr_fim) + ':' + str(min_fim)])

        print(str(hr_inicio) + ':' + str(min_inicio) + ' ~ ' + str(hr_fim) + ':' + str(min_fim))
        print(mins_trab)

    return ponto


# print(retorna_ponto(24))
