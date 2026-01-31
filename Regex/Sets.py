import re
test_string = 'helloHELLO 123_'
pattern = re.compile('[a-zA-Z0-9]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)