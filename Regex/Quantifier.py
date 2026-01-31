import re
dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''
pattern = re.compile(r'\d{4}[-/]0[5-7][-/]\d{2}')
matches = pattern.finditer(dates)
for match in matches:
    print(match)