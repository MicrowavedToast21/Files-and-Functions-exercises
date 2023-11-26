while True:
      user_number_input = input("Enter numbers between 0-9 for user validation: ")
      if user_number_input.isnumeric():
          print("Input accepted!")
          break
      else:
          print("Invalid input. Please enter actual valid integer numbers between 0-9: ")
