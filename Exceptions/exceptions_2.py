# number tu guess
guess_number = 10

while True:
   try:
       user_number = int(input("Enter a number: "))
       if user_number < guess_number:
           raise ValueError("Too small.")
       elif user_number > guess_number:
           raise ValueError("Too large.")
       print("Correct! Congratulations!")
   except ValueError as error:
       print(error)
