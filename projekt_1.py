from typing import Dict, Any

print("Welcome to the app. Please log in:")

oddelovac = 20 * "-"
masterdata = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
count = 0

# doplnit aby se to převedlo na malá písmena

while count < 3:
    username = input('Enter username: ')

    if username in masterdata:
        password = input("Password: ")
        break

    else:
        #print('Username is not in our list. Try again')
        if count == 2:
            print("Sorry, you failed to insert valid username")
            exit()
        else:
            print("Strange, we do not have this username in our system, try again:  ")
            count += 1

print()
print(oddelovac)

if masterdata.get(username) == password:
    print("We have 3 texts to be analyzed")
else:
    password = input("Password again, the one you entered before did not work, you have 2 attempts to go: ")
    if masterdata.get(username) == password:
        print("Great --> we have 3 texts to be analyzed:")

    else:
        password = input("Password again, even second attempt did not work out. You have a last one:  ")
        if masterdata.get(username) == password:
            print("Finally, we have 3 texts to be analyzed:")
        else:
            print("Sorry, you did not manage to enter correct password, you PC will burst in flames in 3...2...1...")
            exit()

print(oddelovac)

TEXTS = [
    "Situated BB about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, traphic traverse the valley. ",

    "At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 beet thick.",

    "The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."]

text_number = int(input("Enter a number btw. 1 and 3 to select: "))-1

if text_number in range(0,4) :
    print(oddelovac)
else:
    exit()


# pocet slov - word count, string splintnutý mezerou
chosen_text = TEXTS[int(text_number)].split(" ")
chosen_text_modif=[]

for slovo in chosen_text:
    chosen_text_modif.append(slovo.strip(".,"))

word_count = len(chosen_text_modif)

# velka a malá písmena - vytvořené nové listy
begin_cap_letters = []

while chosen_text_modif:
    chosen_text_word = chosen_text_modif.pop(0)
    if chosen_text_word.istitle():
        begin_cap_letters.append(chosen_text_word)

# obsahuje jen velká nebo jen malá písmena
chosen_text = TEXTS[int(text_number)].split(" ")
chosen_text_modif=[]

for slovo in chosen_text:
    chosen_text_modif.append(slovo.strip(".,"))

all_small = []
all_big = []

while chosen_text_modif:
    chosen_text_word = chosen_text_modif.pop(0)
    if chosen_text_word.islower() and chosen_text_word.isalpha():
        all_small.append(chosen_text_word)
    elif chosen_text_word.isupper() and chosen_text_word.isalpha():
        all_big.append(chosen_text_word)

###################################################################

numbers=[int(item) for item in TEXTS[int(text_number)].split() if item.isdigit()]

###################################################################

# PRINTS
# wordcount je už len, takže ok
print("There are ", word_count, "words  in selected text.")

# slova zacínající velkým písmenem:
if len(begin_cap_letters) > 1:
    print("There are ", len(begin_cap_letters), " titlecase words.")
elif len(begin_cap_letters) == 1:
    print("There is ", len(begin_cap_letters), " titlecase words.")
else:
    print("There is not any titilecase word.")

# slova obsahující jen velká písmena:
if len(all_big) > 1:
    print("There are ", len(all_big), " uppercase words.")
elif len(all_big) == 1:
    print("There is ", len(all_big), " uppercase words.")
else:
    print("There is not any uppercase word.")

# slova obsahující jen malá písmea:
if len(all_small) > 1:
    print("There are ", len(all_small), " lowercase words.")
elif len(all_small) == 1:
    print("There is ", len(all_small), " lowercase words.")
else:
    print("There is not any lowercase word.")

# Numerci string - ne poče číslic
if len(numbers) > 1:
    print("There are ", len(numbers), " numeric strings.")
elif len(numbers) == 1:
    print("There is ", len(numbers), " numeric string.")
else:
    print("There is not any numeric string in selected text.")

print()
print(oddelovac)
print()

# cetnost
chosen_text = TEXTS[int(text_number)].split(" ")
chosen_text_modif=[]

for slovo in chosen_text:
    chosen_text_modif.append(slovo.strip(".,"))

#list, kde jsou délky slov, všech
graf = []

for slovo in chosen_text_modif:
    if len(slovo) > 0:
        graf.append(len(slovo))

# slovnik pro vypsaní frekvencí výskytu delky slova:
frequency = dict()

for number in graf:
  frequency[int(number)]=frequency.setdefault(int(number), 0)+ 1


#sorting
import collections
sorted_frequency = collections.OrderedDict(sorted(frequency.items()))

for i in sorted_frequency:
   print(i,sorted_frequency.get(i)*"*",sorted_frequency.get(i))

#konečný print
print()
print("If we summed all the numbers in this text we would get:",sum(numbers))






