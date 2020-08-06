import random
from operator import itemgetter
import json
import uuid
from passlib.hash import sha256_crypt
import math

def create_interviewee(data, n, days, hours):
    for i in range(n):
        int(i)
        person = {}

        min_one = math.floor(days*hours/5)
        max_one = math.floor(days*hours/2)
        one_count = random.randint(min_one, max_one)
        zero_count = days * hours - one_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        time = []
        for a in range(days):
            row = []
            for b in range(hours):
                int(a)
                int(b)
                row.append(my_list.pop())
            time.append(row)

        person['time'] = time

        person['_id'] = uuid.uuid4().hex
        person['email'] = person['_id'] + '@gmail.com'
        person['name'] = 'name(interviewee)'
        person['year'] = '2023'
        interests = random.sample(range(1, 7), 2)
        interest1 = interests[0]
        interest2 = interests[1]
        if interest1 == 1:
            person['interest1'] = 'Logistics'
        if interest1 == 2:
            person['interest1'] = 'Social/PR'
        if interest1 == 3:
            person['interest1'] = 'Sponsors'
        if interest1 == 4:
            person['interest1'] = 'Website'
        if interest1 == 5:
            person['interest1'] = 'Design'
        if interest1 == 6:
            person['interest1'] = 'Membership'

        if interest2 == 1:
            person['interest2'] = 'Logistics'
        if interest2 == 2:
            person['interest2'] = 'Social/PR'
        if interest2 == 3:
            person['interest2'] = 'Sponsors'
        if interest2 == 4:
            person['interest2'] = 'Website'
        if interest2 == 5:
            person['interest2'] = 'Design'
        if interest2 == 6:
            person['interest2'] = 'Membership'

        person['role'] = 'Interviewee'
        person['password'] = sha256_crypt.hash('123')
        data.append(person)

def create_interviewer(data, n, days, hours):
    team_list = [1,2,3,4,5,6]*((int)(n/6)+1)
    team_list = team_list[:n]
    random.shuffle(team_list)
    for i in range(n):
        person = {}
        min_one = math.floor(days*hours/5)
        max_one = math.floor(days*hours/3*2)
        one_count = random.randint(min_one, max_one)
        zero_count = days * hours - one_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        time = []
        for a in range(days):
            row = []
            for b in range(hours):
                int(a)
                int(b)
                row.append(my_list.pop())
            time.append(row)

        person['time'] = time

        person['_id'] = uuid.uuid4().hex
        person['email'] = person['_id'] + '@gmail.com'
        person['name'] = 'name(interviewer)'
        team = team_list[i]
        if team == 1:
            person['team'] = 'Logistics'
        if team == 2:
            person['team'] = 'Social/PR'
        if team == 3:
            person['team'] = 'Sponsors'
        if team == 4:
            person['team'] = 'Website'
        if team == 5:
            person['team'] = 'Design'
        if team == 6:
            person['team'] = 'Membership'

        person['max_int'] = str(random.randint(4, 6))

        person['role'] = 'Interviewer'
        person['password'] = sha256_crypt.hash('123')
        data.append(person)

def create_admin(data, days, hours):
    person = {}
    person['_id'] = uuid.uuid4().hex
    person['email'] = 'admin@g'
    person['name'] = 'admin'
    person['password'] = sha256_crypt.hash('123')
    person['role'] = 'Admin'
    person['event'] = 'HopHacks Fall 2020 Interview'
    person['start_date'] = '2020-07-27'
    person['end_date'] = '2020-07-30'
    person['start_time'] = 31
    person['end_time'] = 38
    person['days'] = 4
    person['hours'] = 7
    data.append(person)


def main():
    data = []
    days = 4
    hours = 7
    create_interviewee(data, 20, days, hours)
    create_interviewer(data, 15, days, hours)
    create_admin(data, days, hours)

    with open('data.json', 'w') as file:
        file.write(json.dumps(data))
    
    for person in data:
        print(person)



if __name__ == '__main__':
    main()
