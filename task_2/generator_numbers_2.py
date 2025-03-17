import re
# працює і без цього, але callable з маленької букви
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"\b\d+\.\d+\b"  # регулярний вираз для знаходження чисел
    # тут також можливе використання re.finditer()
    for numbers in re.findall(pattern, text):
        # повернення числа як результату;можливе группування типу: yield float(match.groupe())
        yield float(numbers)


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
