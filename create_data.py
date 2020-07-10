import random
from operator import itemgetter
import json
import uuid

def create_interviewee(data, n):
    for i in range(n):
        int(i)
        person = {}

        one_count = random.randint(5, 10)
        zero_count = 30 - one_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        time = []
        for a in range(5):
            row = []
            for b in range(6):
                int(a)
                int(b)
                row.append(my_list.pop())
            time.append(row)

        person['time'] = time

        person['_id'] = uuid.uuid4().hex
        person['name'] = 'interviewee'
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
        data.append(person)

def create_interviewer(data, n):
    team_list = [1,2,3,4,5,6]*((int)(n/6)+1)
    team_list = team_list[:n]
    random.shuffle(team_list)
    for i in range(n):
        person = {}
        #person_with_id = {}
        one_count = random.randint(5, 15)
        zero_count = 30 - one_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        time = []
        for a in range(5):
            row = []
            for b in range(6):
                int(a)
                int(b)
                row.append(my_list.pop())
            time.append(row)

        person['time'] = time

        person['_id'] = uuid.uuid4().hex
        person['name'] = 'interviewer'
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

        data.append(person)

def main():
    data = []
    create_interviewee(data, 20)
    create_interviewer(data, 15)

    with open('data.json', 'w') as file:
        file.write(json.dumps(data))
    
    for person in data:
        print(person)



if __name__ == '__main__':
    main()
