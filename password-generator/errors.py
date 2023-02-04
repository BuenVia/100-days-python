#FileNotFound

#KeyError

#IndexError

#TypeError

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# else:

# finally:






# title = "Python in easy steps"

# try:
#     print(titel)
# except NameError as msg:
#     print(msg)





day = 32

try:
    if day > 31:
        raise ValueError("Invalid Day Number")
except ValueError as msg:
    print("The program found an ", msg)
finally:
    print("But today is beautiful anyway")