import re
line = "should we use regex abdul@ansari.com often? let me know at  321dsasdsa@dasdsa.com.lol"
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
print(match)