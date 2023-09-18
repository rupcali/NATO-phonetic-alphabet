import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

name = input("Please enter your name: ").upper()
name_nato_phonetic = [phonetic_dict[letter] for letter in name]
print(name_nato_phonetic)
