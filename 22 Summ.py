S = float(input("Введите сумму: "))
if S > 20:
    print("Итоговая сумма: ", str(round(S * 0.65, 2)), "  Скидка: ", str(round(S * 0.35, 2)))
else:
    print("Итоговая сумма: ", str(S), "  Скидка: 0 ")