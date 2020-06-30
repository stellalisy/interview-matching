import random
from operator import itemgetter
import json

def create_interviewee(n):
    print("interviewees")
    interviewee = []
    id_list = random.sample(range(10000,20000), n)
    for i in range(n):
        person = {}

        one_count = random.randint(5, 10)
        zero_count = 30 - one_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        person['ID'] = id_list[i]
        person['name'] = 'name'
        person['interests'] = random.sample(range(1, 6), 2)
        person['time'] = my_list
        person['num_slots'] = one_count
        person['final_time'] = 100
        interviewee.append(person)
    return interviewee

def create_interviewer(n):
    print("interviewers")
    interviewer = []
    id_list = random.sample(range(10000,20000), n)
    team_list = [1,2,3,4,5]*((int)(n/5)+1)
    team_list = team_list[:n]
    random.shuffle(team_list)
    for i in range(n):
        person = {}
        #person_with_id = {}
        one_count = random.randint(5, 15)
        zero_count = 30 - one_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        ID = id_list[i]
        person['ID'] = ID
        person['name'] = 'name'
        person['team'] = team_list[i]
        person['availability'] = my_list
        person['max_int'] = random.randint(4, 6)
        person['num_int'] = 0
        person['num_slots'] = one_count
        person['interviews'] = {}
        #person_with_id[ID] = person

        interviewer.append(person)
    return interviewer

def main():
    interviewee = create_interviewee(20)
    interviewer = create_interviewer(15)
    all_data = {'interviewee': interviewee, 'interviewer':interviewer}
    with open('data.txt', 'w') as file:
        file.write(json.dumps(all_data))

    print('interviewees:')
    for person in interviewee:
        print(person)
    print('interviewers:')
    for person in interviewer:
        print(person)


if __name__ == '__main__':
    main()
