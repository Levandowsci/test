def calculate_profit(
    initial_amount, monthly_deposit, annual_interest_rate, deposit_period
):
    total_amount = initial_amount
    monthly_interest_rate = annual_interest_rate / 12 / 100

    for month in range(1, deposit_period + 1):
        total_amount += monthly_deposit  # Добавляем сумму пополнения в текущий месяц
        monthly_interest = (
            total_amount * monthly_interest_rate
        )  # Рассчитываем проценты за текущий месяц
        total_amount += monthly_interest  # Прибавляем проценты к общей сумме

        print(
            f"Месяц {month}: Общая сумма на счету - {total_amount:.2f}, Прибыль в этом месяце - {monthly_interest:.2f}"
        )

    return total_amount


# Получаем данные от пользователя
initial_amount = int(input("Введите начальную сумму вклада: "))
monthly_deposit = int(input("Введите сумму пополнения в месяц: "))
annual_interest_rate = int(input("Введите годовую процентную ставку: "))
deposit_period = int(input("Введите срок вклада в месяцах: "))

# Вызываем функцию для расчета прибыли по вкладу и выводим результаты
total_amount = calculate_profit(
    initial_amount, monthly_deposit, annual_interest_rate, deposit_period
)
print(
    f"Общая сумма на счету после {deposit_period} месяцев составит: {total_amount:.2f}"
)


