import re
test_string = 'hello 123_ heyho hohey'
pattern1 = re.compile(r'\d')
pattern2 = re.compile(r'\D')
pattern3 = re.compile(r'\s')
pattern4 = re.compile(r'\S')
pattern5 = re.compile(r'\w')
pattern6 = re.compile(r'\W')
pattern7 = re.compile(r'\bhey')
pattern8 = re.compile(r'\Bhey')

matches1 = pattern1.finditer(test_string)
matches2 = pattern2.finditer(test_string)
matches3 = pattern3.finditer(test_string)
matches4 = pattern4.finditer(test_string)
matches5 = pattern5.finditer(test_string)
matches6 = pattern6.finditer(test_string)
matches7 = pattern7.finditer(test_string)
matches8 = pattern8.finditer(test_string)


for match1 in matches1:
    print(match1)
for match2 in matches2:
    print(match2)
for match3 in matches3:
    print(match3)
for match4 in matches4:
    print(match4)
for match5 in matches5:
    print(match5)
for match6 in matches6:
    print(match6)
for match7 in matches7:
    print(match7)
for match8 in matches8:
    print(match8)