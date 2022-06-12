import API
from datetime import datetime

client = API.client

now = datetime.now()

print(now)

def get_first_fact(text): 
    with open(text, 'r') as f: 
        line = f.readline()
        rest_lines = f.readlines()
    with open(text, 'w') as f: 
        f.writelines(rest_lines)
    return line

print(get_first_fact('capybara_facts.txt'))