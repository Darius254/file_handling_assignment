# file_handling_assignment.py

# File Creation and Writing
try:
    # Open the file in write mode and add initial lines
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1.\n")
        file.write("Number: 12345\n")
        file.write("This is line 3 with some text and numbers: 67890\n")
    print("File created and initial content written successfully.")
except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# File Reading and Display
try:
    # Open the file in read mode and display content
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nFile content after initial writing:")
        print(content)
except FileNotFoundError:
    print("File not found: Unable to read the file.")
except PermissionError:
    print("Permission denied: Unable to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode and add additional lines
    with open("my_file.txt", 'a') as file:
        file.write("Appending line 4.\n")
        file.write("Another number: 54321\n")
        file.write("This is the last appended line.\n")
    print("Additional lines appended successfully.")
except PermissionError:
    print("Permission denied: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final Reading and Display with Error Handling
try:
    # Open the file in read mode again to display final content
    with open("my_file.txt", 'r') as file:
        final_content = file.read()
        print("\nFile content after appending:")
        print(final_content)
except FileNotFoundError:
    print("File not found: Unable to read the file.")
except PermissionError:
    print("Permission denied: Unable to read the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


