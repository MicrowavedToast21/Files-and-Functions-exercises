with open("../montanyas.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        print(line)