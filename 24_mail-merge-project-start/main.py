#Extract names from list
with open("Input/Names/invited_names.txt", "r") as file_1:
    invitees = [s.strip("\n") for s in file_1.readlines()]

#Extract letter
with open("Input/Letters/starting_letter.txt", "r") as file_2:
    letter = file_2.read()

#Write individual letters
for invitee in invitees:
    invitation = letter.replace("[name]", invitee)
    with open(f"Output/ReadyToSend/letter_for_{invitee}.docx", "w") as file_3:
        file_3.write(invitation)

