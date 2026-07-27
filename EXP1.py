def Palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
words = input("Enter words separated by space: ").split()
print(Palindrome(words))