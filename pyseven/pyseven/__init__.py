from email._header_value_parser import get_phrase
print("Hello World")
print("I am the Strategist")
phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)
# Changing don't panic in to on tap
for i in range(4):
    plist.pop()
plist.remove("'")
plist.remove("D") 
plist.extend([plist.pop(), plist.pop()]) 
plist.insert(2, " ")
plist.pop(4) 
new_phrase="".join(plist)
print(plist)
print(new_phrase)
vowels=['a','e','i','o','u']
word=input('Enter a word to search for vowels')
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)        