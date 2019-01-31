word=open('words','r')
words=word.readlines()
cleanwords=[word.strip('\n').lower() for word in words]
def signature(word):
    return ''.join(sorted(word))

import collections
words_bysig=collections.defaultdict(list)


for word in cleanwords:
    words_bysig[signature(word)].append(word)

print("Enter letters")
user=input('>')
userletters=signature(user)
print("Possible Words: ")
print(words_bysig[userletters])