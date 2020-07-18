import random
from operator import itemgetter
import json
import copy
import statistics

def get_roles(data):
    interviewee = []
    interviewer = []

    for user in data:
        if user['role'] == 'Interviewee':
            num_slots = 0
            availability = []
            for day in user['time']:
                availability.extend(day)
                num_slots += sum(day)
            user['time'] = availability
            user['num_slots'] = num_slots
            #user.pop('password', None)
            interviewee.append(user)
        elif user['role'] == 'Interviewer':
            num_slots = 0
            availability = []
            for day in user['time']:
                availability.extend(day)
                num_slots += sum(day)
            user['time'] = availability
            user['num_slots'] = num_slots
            user['max_int'] = int(user['max_int'])
            #user.pop('password', None)
            interviewer.append(user)
        
    for person in interviewee:
        person['final_time'] = 100
    for person in interviewer:
        person['num_int'] = 0
        person['interviews'] = {}

    return [interviewee,interviewer]

def is_available(interviewer, team, i):
    order = list(range(0,len(interviewer)))
    random.shuffle(order)
    interviewer_sorted = sorted(interviewer, key=lambda k: k['num_int'])
    for info in interviewer_sorted:
        #print("interviewer: {}".format(info['team']))
        if info['team'] == team and info['time'][i] == 1 and info['num_int'] < info['max_int']:
            return info['_id']
    return 0

def simple_match(interviewee, interviewer):
    num_match = 0
    interviewee_sorted = sorted(interviewee, key=lambda k: k['num_slots'])
    for person in interviewee_sorted:
        interest1 = person['interest1']
        interest2 = person['interest2']
        time = person['time']
        order = list(range(0,len(time)))
        random.shuffle(order)
        for i in order:
            id1 = is_available(interviewer, interest1, i)
            id2 = is_available(interviewer, interest2, i)
            if time[i] == 1 and id1 != 0 and id2 != 0:
                for p in interviewer:
                    if id1 == p['_id'] or id2 == p['_id']:
                        p['num_int'] += 1
                        p['time'][i] += 2
                        p['interviews'][i] = [person['_id'], person['name']]
                person['final_time'] = i
                num_match += 1
                break
    return num_match

def random_match(interviewee, interviewer):
    num_match = 0
    interviewee_sorted = random.sample(interviewee, len(interviewee))
    for person in interviewee_sorted:
        interest1 = person['interest1']
        interest2 = person['interest2']
        time = person['time']
        order = list(range(0,len(time)))
        random.shuffle(order)
        for i in order:
            id1 = is_available(interviewer, interest1, i)
            id2 = is_available(interviewer, interest2, i)
            if time[i] == 1 and id1 != 0 and id2 != 0:
                for p in interviewer:
                    if id1 == p['_id'] or id2 == p['_id']:
                        p['num_int'] += 1
                        p['time'][i] += 2
                        p['interviews'][i] = [person['_id'], person['name']]
                person['final_time'] = i
                num_match += 1
                break
    return num_match

def iterated_match(interviewee, interviewer):
    itr = 0
    num_match = 0
    n = len(interviewee)
    best_case = {}
    best_match = 0

    temp_interviewee = copy.deepcopy(interviewee)
    temp_interviewer = copy.deepcopy(interviewer)
    num_match = simple_match(temp_interviewee, temp_interviewer)

    best_case[num_match] = [temp_interviewee, temp_interviewer]
    best_match = num_match

    while num_match != n and itr < 50:
        temp_interviewee = copy.deepcopy(interviewee)
        temp_interviewer = copy.deepcopy(interviewer)
        num_match = simple_match(temp_interviewee, temp_interviewer)
        #print("num_match={}, itr={}".format(num_match,itr))
        if num_match > best_match:
            best_case[num_match] = [temp_interviewee, temp_interviewer]
            best_case.pop(best_match, None)
            best_match = num_match
        itr += 1

    while num_match != n and itr < 100:
        temp_interviewee = copy.deepcopy(interviewee)
        temp_interviewer = copy.deepcopy(interviewer)
        num_match = random_match(temp_interviewee, temp_interviewer)
        #print("num_match={}, itr={}".format(num_match,itr))
        if num_match > best_match:
            best_case[num_match] = [temp_interviewee, temp_interviewer]
            best_case.pop(best_match, None)
            best_match = num_match
        itr += 1

    #print("num_match={}, itr={}".format(num_match,itr))
    ee = list(best_case.values())[0][0]
    er = list(best_case.values())[0][1]
    return [ee, er, num_match]

def main():
    with open('from_mongo.json', 'r') as file:
        data = json.load(file)

    people = get_roles(data)
    interviewee = people[0]
    interviewer = people[1]

    min_std = 10000
    max_match = 0
    best = []
    for i in range(100):
        int(i)
        temp_interviewee = copy.deepcopy(interviewee)
        temp_interviewer = copy.deepcopy(interviewer)

        info = iterated_match(temp_interviewee, temp_interviewer)
        interviewee_matched = info[0]
        interviewer_matched = info[1]
        num_match = info[2]
        loss = 0
        num_p = 0
        for person in interviewer_matched:
            if len(person['interviews']) > 1:
                loss += statistics.pstdev(list(person['interviews'].keys()))
                num_p += 1
        if (num_p != 0):
            mean_loss = loss/num_p
        else:
            mean_loss = 0


        if num_match >= max_match and mean_loss < min_std:
            best = [interviewee_matched, interviewer_matched]
            min_std = mean_loss
            max_match = num_match
            print("{}: {}, {}".format(i,num_match, mean_loss))


    interviewee = best[0]
    interviewer = best[1]

    for person in interviewer:
        int_list = []
        for key, value in person['interviews'].items():
            int_list.append([key,value])
        int_list = sorted(int_list, key=lambda x: x[0])
        person['interviews'] = int_list
    print("num_match={}, std={}".format(max_match, min_std))

    all_data = interviewee
    all_data.extend(interviewer)

    with open('matched.json', 'w') as file:
        file.write(json.dumps(all_data))


if __name__ == '__main__':
    main()