import re

test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')
# Split - it will split the word and it will take the given parameter as a reference
splitted = pattern.split(test_string)
print(splitted)

test_string = 'hello world, you are the best world'
pattern = re.compile(r'world')
subbed_String = pattern.sub('planet',test_string)
print(subbed_String)

urls = """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group())
subbed_url = pattern.sub(r"\2\3",urls)
print(subbed_url)