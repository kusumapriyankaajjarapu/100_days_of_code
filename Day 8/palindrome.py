#Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a
#palindrome else it should return false.

def check_palindrome(word):
    l = len(word)
    for i in range(0,l // 2 + 1):
        if(word[i] != word[l-1-i]):
            return False
    return True

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
