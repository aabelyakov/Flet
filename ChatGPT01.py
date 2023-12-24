# Для определения последнего дня февраля в заданном году вам нужно учесть,
# является ли год високосным. Високосный год содержит 366 дней вместо обычных
# 365, и в феврале в этом случае 29 дней.
# Правило определения високосного года: год високосный, если он делится на 4,
# но если он также делится на 100, то он високосный только в том случае, если
# делится на 400.

# В строке 9 применяется атрибут weeks объекта timedelta. Этот атрибут
# позволяет указать количество недель, на которое нужно изменить дату.
#
# В данном коде строка 9 используется для преобразования относительного смещения
# в годах и месяцах в эквивалентное количество недель. Умножение года на 52 и
# месяц на 4 приблизительно учитывает среднюю длину года и месяца в днях,
# превращая их в количество недель. Это не идеальный способ, так как длина года
# точно не равна 52 неделям, а месяц - 4 неделям, но в большинстве случаев это
# достаточно близко.
# Это делается для того, чтобы учесть смещение в годах и месяцах при вычислении
# новой даты с использованием объекта timedelta.


from datetime import datetime, timedelta


def изменить_дату(исходная_дата, года=0, месяцы=0, дни=0, часы=0, минуты=0, секунды=0):
    новая_дата = исходная_дата + timedelta(
        days=дни,
        seconds=секунды,
        minutes=минуты,
        hours=часы,
        weeks=года * 52 + месяцы * 4
    )
    return новая_дата


# Пример использования:
исходная_дата = datetime(2023, 1, 1, 12, 0, 0)
новая_дата = изменить_дату(исходная_дата, года=-1, месяцы=2, дни=-3, часы=4,
                           минуты=-5, секунды=6)

print("Исходная дата:", исходная_дата)
print("Новая дата:", новая_дата)
