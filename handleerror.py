try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
