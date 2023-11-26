file_name = input("Enter the name of the file that you want to create: ")
file_content_lines = []
while True:
    line = input("Enter a line or press enter to finish: ")

    if not line:
        break

    file_content_lines.append(line)

with open(file_name, "w") as file:
    for content_line in file_content_lines:
        file.write(content_line + "\n")
print(f"{file_name} was created with its appropriate content")