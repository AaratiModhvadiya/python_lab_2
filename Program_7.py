# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, this is a sample text.\nSecond line of text.')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of example.txt:")
    print(content)
