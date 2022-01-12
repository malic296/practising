import random

difficult = input("How strong you want your password to be? (easy, medium, strong): ")
length = input("How long do you want your password to be ? (number of characters): ")

letter_easy = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter_medium = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letter_strong = ["0","1","2","3","4","5","6","7","8","9"]

password_easy = []
password_medium = []
password_strong = []

if difficult == "easy":
    while len(password_easy) < int(length):
        position = random.randint(0, len(letter_easy) - 1)
        password_easy.append(letter_easy[position])
        password_easy1 = ["".join(password_easy)]

    print(f"You can use this password: {password_easy1[0]}.")

elif difficult == "medium":
    while len(password_medium) < int(length):
        medium_choice = random.randint(0,1)
        if medium_choice == 1:
            position_medium = random.randint(0, len(letter_medium) -1)
            password_medium.append(letter_medium[position_medium])
            password_medium1 = ["".join(password_medium)]

        else:
            position_medium1 = random.randint(0, len(letter_easy) - 1)
            password_medium.append(letter_easy[position_medium1])
            password_medium1 = ["".join(password_medium)]


    print(f"You can use this password: {password_medium1[0]}.")

elif difficult == "strong":
    while len(password_strong) < int(length):
        strong_choice = random.randint(0,2)
        if strong_choice == 0:
            position_hard = random.randint(0, len(letter_easy) -1)
            password_strong.append((letter_easy[position_hard]))
            password_strong1 = ["".join(password_strong)]

        elif strong_choice == 1:
            position_hard = random.randint(0, len(letter_medium) - 1)
            password_strong.append((letter_medium[position_hard]))
            password_strong1 = ["".join(password_strong)]

        else:
            position_hard = random.randint(0, len(letter_strong) - 1)
            password_strong.append((letter_strong[position_hard]))
            password_strong1 = ["".join(password_strong)]


    print(f"You can use this password: {password_strong1[0]}.")
else:
    print("Sorry that option was not there")