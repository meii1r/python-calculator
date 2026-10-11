def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError
        return a / b
    raise ValueError


def main():
    print("Калькулятор. Пример: 12 * 3")
    print("Операции: + - * /   Выход: q")
    while True:
        text = input("> ").strip()
        if text.lower() in ("q", "exit", "выход"):
            break
        parts = text.split()
        if len(parts) != 3:
            print("Формат: число операция число")
            continue
        try:
            a = float(parts[0].replace(",", "."))
            b = float(parts[2].replace(",", "."))
            result = calculate(a, parts[1], b)
            if result == int(result):
                result = int(result)
            print("=", result)
        except ZeroDivisionError:
            print("Ошибка: на ноль делить нельзя")
        except ValueError:
            print("Ошибка: проверь числа и операцию")


if __name__ == "__main__":
    main()
