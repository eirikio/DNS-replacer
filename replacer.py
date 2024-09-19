import os

file_name = "textfile.txt"
file_path = os.path.join(os.getcwd(), file_name)

if not os.path.isfile(file_path):
    print(f"File not found")
    exit(1)

replacement_word = input("Enter the word to replace: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content.replace("URL", replacement_word)

    new_file_name = f"{os.path.splitext(file_name)[0]}_replaced.txt"
    new_file_path = os.path.join(os.getcwd(), new_file_name)

    with open(new_file_path, 'w') as new_file:
        new_file.write(updated_content)

    print(f"All instances of 'URL' has been replaced with '{replacement_word}.")
    print(f"The updated content has been saved to '{new_file_name}")

except Exception as e:
    print(f"An error occured: {e}.")