try:
    # co mamy zrobic
    a = 10
    result = a / 0
    print(result)
except ZeroDivisionError:
    #co zrobic, jesli wystapi jakis blad
    print("You can't divide number by zero!")

def add_number():
    try:
        user_input = input("Provide number: ")
        print(int(user_input) + 6)
    except TypeError:
        print("Please provide number.")
        add_number()
    except ValueError:
        print("You provided string instead of number.")
        add_number()

add_number()
