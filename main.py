import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    name = input("Please enter your name: ").upper()
    try:
        name_nato_phonetic = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(name_nato_phonetic)

generate_phonetic()
