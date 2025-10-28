import pandas

#TODO 1: Create a dictionary in the format: {"A": "Alfa",...}
data_input = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in data_input.iterrows()}

#TODO 2: Create a list of phonetic code words from a word that the user inputs.
def generate_phonetic():
    word_to_translate = input("Enter a word: ").upper()
    try:
        nato_translation = [alphabet_dict[letter] for letter in word_to_translate]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_translation)

generate_phonetic()