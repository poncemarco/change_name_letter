# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp'''file = open('my_file.txt')
# TODO 1: Create the rutes for the files

letter_rute = '/home/marco/PycharmProjects/day_24/Input/Letters/starting_letter.txt'
names_rute = '/home/marco/PycharmProjects/day_24/Input/Names/invited_names.txt'
letter_ready_rute = '/home/marco/PycharmProjects/day_24/Output/ReadyToSend/'



# TODO 3: Create a letter for every name
with open(names_rute, 'r') as names:
    names = names.readlines()
    # TODO 2: Leer y mostrar carta:
with open(letter_rute) as letter:
    letter = letter.read()
    for name in names:
        stripped_name = name.strip()
        to_change = '[name]'
        new_letter = letter.replace(to_change, stripped_name)
        with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)









# TODO 4: Change [name] for names in the files
'''txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x) '''


