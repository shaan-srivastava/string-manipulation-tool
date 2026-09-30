def string_manipulation():

    text = input("Enter a string: ")

    while True:
        print("\n--- STRING MANIPULATION TOOL ---")
        print("1. Find length")
        print("2. Uppercase")
        print("3. Lowercase")
        print("4. Reverse string")
        print("5. Count character")
        print("6. Count words")
        print("7. Replace word")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Length of string:", len(text))

        elif choice == "2":
            print("Uppercase:", text.upper())

        elif choice == "3":
            print("Lowercase:", text.lower())

        elif choice == "4":
            print("Reversed string:", text[::-1])

        elif choice == "5":
            ch = input("Enter a character: ")
            print("Character occurs", text.count(ch), "time(s)")

        elif choice == "6":
            words = text.split()
            print("Number of words:", len(words))

        elif choice == "7":
            old_word = input("Enter word to replace: ")
            new_word = input("Enter new word: ")

            text = text.replace(old_word, new_word)

            print("New string:", text)

        elif choice == "8":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


string_manipulation()
