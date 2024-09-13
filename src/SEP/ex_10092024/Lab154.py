import os

try:
    full_path = os.getcwd()
    print(full_path)
    file = open(full_path+'/exam.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File not Found")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
