#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

    print(name_list)

    for name in name_list:
        with open("./Input/Letters/starting_letter.txt") as letter:
            letter_list = letter.readlines()
            name_str = str(letter_list[0])
            letter_list[0] = name_str.replace("[name]", name.strip())
            updated_letter = ''.join(letter_list)

            with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w") as new_letter:
                new_letter.write(updated_letter)
