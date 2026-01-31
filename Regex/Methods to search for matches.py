import re
test_string = '123abc456789abc123ABC'

# Method 1: findall()
pattern = re.compile(r'abc')
matches = pattern.findall(test_string)
for match in matches:
    print(match)

# Method 2: match() - it will return the pattern if it is present only on the beginning of the string
pattern = re.compile(r'123')
match = pattern.match(test_string)
print(match)

# Method 3: search() - it will only return the pattern in their first match
pattern = re.compile(r'abc')
match = pattern.search(test_string)
print(match)

