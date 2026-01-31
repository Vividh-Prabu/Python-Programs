import re
my_string = """
hello world
1223
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
