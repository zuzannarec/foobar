# Write a function that takes in a string of lowercase letters and returns the first non-repeating character.
# The first non-repeating character is the first character in a string that occurs only once.
# If the input string does not contain any non-repeating charcters your function should return None

# Example 1:
# input_string = "abcabcxabc"
# output = "x"

# Example 2:
# input_string = "t"
# output = "t"

# Example 3:
# input_string = "yuyuy"
# output = None


from collections import OrderedDict

def firstNonRepeatingCharacter1(string):
    non_repeating = OrderedDict()
    for idx, char in enumerate(string):
        if char in non_repeating.keys():
            non_repeating[char] = -1
        else:
            non_repeating[char] = 1
    while len(non_repeating) > 0:
        key, value = non_repeating.popitem(last=False)
        if value == 1:
            return key
    return None

def firstNonRepeatingCharacter2(string):
    freq = dict()
    for lett in string:
        if lett in freq.keys():
            freq[lett] += 1
        else:
            freq[lett] = 1
    for idx, lett in enumerate(string):
        if freq[lett] == 1:
            return lett
    return None

def firstNonRepeatingCharacter3(string):
    for idx1, lett1 in enumerate(string):
        repeat = False
        for idx2, lett2 in enumerate(string):
            if lett1 == lett2 and idx1 != idx2:
                repeat = True
                break
        if not repeat:
            return lett1
    return None

print(f"{firstNonRepeatingCharacter1('abcabcxabc')}, Expected: x")
print(f"{firstNonRepeatingCharacter2('abcabcxabc')}, Expected: x")
print(f"{firstNonRepeatingCharacter3('abcabcxabc')}, Expected: x")

print(f"{firstNonRepeatingCharacter1('t')}, Expected: t")
print(f"{firstNonRepeatingCharacter2('t')}, Expected: t")
print(f"{firstNonRepeatingCharacter3('t')}, Expected: t")

print(f"{firstNonRepeatingCharacter1('yuyuy')}, Expected: None")
print(f"{firstNonRepeatingCharacter2('yuyuy')}, Expected: None")
print(f"{firstNonRepeatingCharacter3('yuyuy')}, Expected: None")


def upper_case(func):
    def wrapper(self):
        return func(self).upper()
    return wrapper

class Foo:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @upper_case
    def fullName(self) -> str:
        return f"{self.name} {self.surname}"

foo = Foo("Zuza", "Rec")
print(foo.fullName())