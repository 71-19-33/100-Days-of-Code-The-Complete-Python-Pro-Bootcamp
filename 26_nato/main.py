import pandas

#TODO 1: Create a dictionary int he format: {"A": "Alfa",...}
data_input = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in data_input.iterrows()}

#TODO 2: Create a list of phonetic code words from a word that the user inputs.
programs_runs = True
while programs_runs:
    word_to_translate = input("Enter a word: ").upper()
    if word_to_translate == "exit":
        programs_runs = False
    nato_translation = [alphabet_dict[letter] for letter in word_to_translate]
    print(nato_translation)


