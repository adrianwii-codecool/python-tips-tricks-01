dictionary = {"Avatar" : 2009, "Golden Eye" : 1995, "Toy Story" : 1993}

# key : value

print(dictionary["Toy Story"])

print(*dictionary.values())
print("Avatar" in dictionary)

dictionary["Golden Eye"] = 2022
print(2022 in dictionary.values())

print(dictionary)

del dictionary["Toy Story"]

print(dictionary)
