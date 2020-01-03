# Get sentence from user
original = input("Write a sentence to code! ").strip().lower()

#split sentence into words
words = original.split()

#loop through words and convert into pig latin
new_words = []

#if word starts with a vowel, add "yay"
for word in words:
    if word[0] in "aeiou":
        new_word = word +"yay"
        new_words.append(new_word)

#if word starts with consonant, move first to end and add "ay"
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        cons = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

#stick words back together

output = " ".join(new_words)
#output final string
print(output)
