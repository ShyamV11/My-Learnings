def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

# given string
mystr = "python string reversal"
print("Given String: ", mystr)

# Reversed string
print("Reversed String: ", reverse(mystr))

