import re

def first_step(new_id):
    new_id = new_id.lower()
    return new_id

def second_step(new_id):
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    return new_id

def third_step(new_id):
    new_id = re.sub(r'\.\.+', '.', new_id)
    return new_id

def fourth_step(new_id):
    new_id = re.sub(r'^\.|\.$', '', new_id)
    return new_id
    

def fifth_step(new_id):
    if new_id == "":
        new_id = "a"
    return new_id

def sixth_step(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    return new_id

def seventh_step(new_id):
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    return new_id
        
def all_steps(new_id):
    new_id = first_step(new_id)
    new_id = second_step(new_id)
    new_id = third_step(new_id)
    new_id = fourth_step(new_id)
    new_id = fifth_step(new_id)
    new_id = sixth_step(new_id)
    new_id = seventh_step(new_id)
    return new_id

def solution(new_id):
    answer = ''
    answer = all_steps(new_id)
    return answer


