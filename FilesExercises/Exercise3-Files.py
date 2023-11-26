file_name = input("Enter the name of the file that you want to create: ")
file_content = input("Enter the content that you want to insert in the file: ")
with open(file_name, "w") as f:
    f.write(file_content)
print(f"The file {file_name} has been created with the given content")
