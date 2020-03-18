try:
    # co mamy zrobic
    a = 10
    result = a / 0
    print(result)
except ZeroDivisionError:
    #co zrobic, jesli wystapi jakis blad
    print("You can't divide number by zero!")

def add_number():
    answer = True

    while answer:
        try:
            user_input = input("provide number ")
            print(int(user_input) + 6)
        except TypeError:
            print("please provide number")
        except ValueError:
            print("you provided string instead of number ")
            add_number()
        finally:
            answer = False

add_number()
