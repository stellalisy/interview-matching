import random
from operator import itemgetter
import json

def create_interviewee(n):
    print("interviewees")
    interviewee = []
    id_list = random.sample(range(10000,20000), n)
    for i in range(n):
        person = {}

        zero_count = random.randint(15, 25)
        one_count = 30 - zero_count
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
    for i in range(n):
        person = {}
        #person_with_id = {}
        zero_count = random.randint(10, 25)
        one_count = 30 - zero_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        ID = id_list[i]
        person['ID'] = ID
        person['name'] = 'name'
        person['team'] = random.randint(1,5)
        person['availability'] = my_list
        person['max_int'] = random.randint(4, 7)
        person['num_int'] = 0
        person['num_slots'] = one_count
        person['interviews'] = []
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
