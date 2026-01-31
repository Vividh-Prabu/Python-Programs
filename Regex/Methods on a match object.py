import re
test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)

# Span Method - it will return the start and stop values of the pattern in a tuple:(start,end)
for match in matches:
    print(match.span(),match.start(),match.end())

# Group Method - used to retrieve the actual matched text from a match object
for match in matches:
    print(match.group())
