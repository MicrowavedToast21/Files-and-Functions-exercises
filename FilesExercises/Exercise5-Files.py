with open("../montanyas.txt", "r") as file:
     lines = file.readlines()

num_lines = len(lines)
while True:
    try:
        line_number = int(input(f"Enter a lime from number 1 to {num_lines}: "))

        if 1 <= line_number <= num_lines:
            break
        else:
            print("Invalid line number. Please enter in the valid range: ")
    except ValueError:
        print("Invalid input. Pleae enter a number in the range: ")

chosen_line = lines[line_number - 1]
print(f"content of line {line_number} is: {chosen_line}")
