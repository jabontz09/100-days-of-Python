#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def create_letters():
    names = []
    template = ""
    with open("./Intermediate/day-24/Mail Merge Project Start/input/Names/invited_names.txt", "r") as f:
        names = f.readlines()

    with open("./Intermediate/day-24/Mail Merge Project Start/input/Letters/starting_letter.txt", "r") as f:
        template = f.read()

    for name in names:
        name = name.strip()
        with open(f"./intermediate/day-24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
            content = template.replace("[name]", name)
            f.write(content)

create_letters()