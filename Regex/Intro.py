import re
test_string = '123abc456789abc123ABC'

# Method to print a raw string
a = r'\tHello World\n'
print(a)

pattern = re.compile(r'abc')
# ----- Method 1 -----
matches = pattern.findall(test_string)
print(matches)

# ----- Method 2 ----- finditer() - it will return the all the matches of the given pattern
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

# ----- Method 3 -----
matches = re.finditer(r'abc',test_string)
for match in matches:
    print(match)

