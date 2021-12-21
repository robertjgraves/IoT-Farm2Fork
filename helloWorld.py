print("Hello World!")
print("Robert was here!")

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Count not open file.log')

print("End of program")
