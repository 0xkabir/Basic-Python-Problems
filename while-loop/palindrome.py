word = input("Enter a word to check if palindrome: ").lower()
i = 1
check_word = ''
while i <= len(word):
    check_word += word[len(word)-i]
    i+=1
print(f"{word.capitalize()} is a palindrome" if word == check_word else f"{word.capitalize()} is not a palindrome")