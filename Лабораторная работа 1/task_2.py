# TODO Найдите количество книг, которое можно разместить на дискете
lists = 100
stroki = 50
simvoli = 25
mesto = (1024 * 1024 * 1.44) // 4
kniga = lists * stroki * simvoli
itog = mesto // kniga
print("Количество книг, помещающихся на дискету:", round(itog))
