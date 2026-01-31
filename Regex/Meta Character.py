import re
test_string = '123abc456789abc123ABC'

# # '.' Matches any character except new line
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.') - matches only the dot(.) character

# # '^' Matches when the string is starting with the given pattern
# pattern = re.compile(r'^123')

# '$' Matches when the string is ending with the given pattern
pattern = re.compile(r'ABC$')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)