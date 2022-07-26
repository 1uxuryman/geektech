import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'AV', text)
print(result)

result = re.match(r'Analytics', text)
print(result)

result = re.search(r'Analytics', text)
print(result)

result = re.search(r'AV', text)
print(result)

result = re.findall(r'AV', text)
print(result)

result = re.split(r'Vidhya', text)
print(result)

result = re.sub(r' ', r',', text)
print(result)

result = re.sub(r'a', r'o', text)
print(result)

with open("test_regs.txt", "r", encoding="utf-8") as file:
    content = file.read()
    beeline_numbers_list = re.findall(r'\+996 (?:77[0-9]|22[0-2]) [0-9 ]{8}', content)
    print(beeline_numbers_list)
    mega_numbers_list = re.findall(r'\+996 (?:55[0-9]|99[0579]|755) [0-9 ]{8}', content)
    print(mega_numbers_list)
    o_numbers_list = re.findall(r'\+996 (?:50[0-27-945]|70[0-9]) [0-9 ]{8}', content)
    print(o_numbers_list)

