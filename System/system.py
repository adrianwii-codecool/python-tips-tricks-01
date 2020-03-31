import os

home = os.getcwd()
print(home)

linux_cmd = 'start chrome'
osx_cmd = 'open -a "Google Chrome"'
os.system(osx_cmd)

# webpage = input("Enter webpage address: ")
# my_cmd = 'open -a  "{}" "{}"'.format("Google Chrome", webpage)
# os.system(my_cmd)

# run my python program
option = input("Chose program to run: ")

if option == 'Dictionaries':
    my_cmd = 'Python  {}'.format("../Dictionaries/dictionary.py")
elif option == 'Lists':
    my_cmd = 'Python  {}'.format("../Lists/list.py")
else:
    exit()

os.system(my_cmd)