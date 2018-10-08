# combine profanity
with open('bad-words.txt', 'r', encoding='utf8') as f1, \
        open('swearWords.txt', 'r', encoding='utf8') as f2, \
        open("profanity.txt", "w") as f3:
    f3.write(f1.read().strip() + f2.read().strip())
    print(f3)
