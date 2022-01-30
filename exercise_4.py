sum = 0

for i in range(5):
    while True:
        val = input(f"Enter int #{i + 1}: ")

        if val.isdecimal() or (val[0] == "-" and val[1:].isdecimal()):
            sum += int(val)
            break
        print("Invalid input. Please enter an int.")

print(f"Your sum is {sum}")
