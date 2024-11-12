from typing import Optional


def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None


def gather_numbers() -> list[float]:
    numbers = []

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == "done":
            break

        number = str_to_float(user_input)

        if number is not None:
            numbers.append(number)  #Only add valid floats to the list

    return numbers

if __name__ == "__main__":
    numbers = gather_numbers()
    print("The sum of the numbers is:", sum(numbers))

#Enter a number (or 'done' to finish): 3.14
#Enter a number (or 'done' to finish): abc
#Enter a number (or 'done' to finish): 2.71
#Enter a number (or 'done' to finish): done
#The sum of the numbers is: 5.85


