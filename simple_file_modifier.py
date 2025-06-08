
# Ask the user to type the name of the file
filename = input("Enter the name of the file you want to read: ")

try:
    # Try to open the file and read all lines
    with open(filename, 'r') as file:
        content = file.readlines()

    # Change the text - here we make all letters uppercase
    new_content = []
    for line in content:
        new_content.append(line.upper())

    # Save the new content into a new file
    new_filename = "new_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.writelines(new_content)

    print(f"Done! The new file is saved as: {new_filename}")

except FileNotFoundError:
    # This happens if the file doesn't exist
    print("Error: The file was not found. Please check the name and try again.")
except:
    # This handles other reading problems
    print("Error: Something went wrong while reading the file.")
