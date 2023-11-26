with open("../montanyas.txt", "r") as file:
    lines = file.readlines()

num_lines = len(lines)
print(f"There are {num_lines} lines in this txt file")
while True:
    try:
        line_number = int(input(f"Enter a lime from number 1 to {num_lines} for the line you would like to change: "))

        if 1 <= line_number <= num_lines:
            break
        else:
            print("Invalid line number. Please enter in the valid range: ")
    except ValueError:
        print("Invalid input. Pleae enter a number in the range: ")
chosen_line = lines[line_number - 1]
print(f"content of line {line_number} is: {chosen_line}")
new_content = input("Now enter the new content that you want to add to the line: ")
with open("../montanyas.txt", "w") as file:
     file.writelines(lines)
print(f" the new content of {chosen_line} is now: {new_content}")