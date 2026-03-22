# count vowels using function


def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count

# revers string using function
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

#   check the string is palindrome
def is_palindrome(s):
    return reverse_string(s) == s


print(count_vowels("Hello World"))
print(reverse_string("Tony"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
