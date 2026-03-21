def ispalindrome(s):
    s.lower()
    cleaned =""
    for char in s:
        if char.isalnum():
            cleaned += char
    return cleaned == cleaned[::-1]

print(ispalindrome("racecar"))