"""File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read."""

try:
    with open(input('enter_file_name: '), "r") as file:
        print("File opened successfully.")
        new_file_name = input("Enter the new file name: ")
        try:
            with open(new_file_name, "x") as new_file:
                for line in file:
                    new_file.write(line)
        except OSError:
            print("Error creating the new file. Please check the file permissions.")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except OSError:
    print("Error opening the file. Please check the file permissions.")