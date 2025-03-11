# Thesaurus App
print("============Thesauraus App============")
print("[1] View Synonyms \n[2] Add Synonyms")
ch = int(input("Enter your choice: "))
syn = {"awful": "terrible",
       "beautiful": "gorgeous",
       "start": "begin"
       }

if ch == 1:
    word = input("Enter the word: ")
    word = word.lower()
    if word in syn:
        print(f"Synonym of {word} is: {syn[word]}")
    else:
        print("Synonym Unknown!")
elif ch == 2:
    kword = input("Enter the main word: ")
    kword = kword.lower()
    synon = input("Enter the synonym: ")
    synon = synon.lower()
    if kword not in syn.keys() and kword not in syn.values():
        newsyn = {kword: synon}
        syn.update(newsyn)
        print(syn)
        print("Item Added!")
    else:
        print("Item Already Exists!")
else:
    print("Input Enter Correct Choice Code.")
