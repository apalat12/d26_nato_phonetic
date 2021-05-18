
import pandas as pd

names = pd.read_csv("nato_phonetic_alphabet.csv")

# for (letter,word) in names.iterrows():
#     print(word.letter,word.code)
nato_dict = {word.letter:word.code for (letter,word) in names.iterrows()}

# print(nato_dict)

while True:
    usr_name = input("What's your name:")
    try:
        res =[nato_dict[i] for i in usr_name.upper()]
        break
    except KeyError:
        print("Only letters please")

print("Your nato code is:")
print(res)

dummy = input("Press enter to close:")
