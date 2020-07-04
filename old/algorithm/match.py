import random
from operator import itemgetter
import json
import copy
import statistics

def interviewee_time(interviewee):
    print("interviewee time:")
    time = [0]*30
    demand = {}
    demand[1] = [0]*30
    demand[2] = [0]*30
    demand[3] = [0]*30
    demand[4] = [0]*30
    demand[5] = [0]*30
    for person in interviewee:
        team1 = person['interests'][0]
        team2 = person['interests'][1]
        time = person['time']
        for i in range(len(time)):
            demand[team1][i] = demand[team1][i] + time[i]
            demand[team2][i] = demand[team1][i] + time[i]
    for team in demand:
        print(demand[team])
    return demand

def interviewer_by_team(interviewer):
    print("interviewer by team")
    teams = {}
    teams[1] = []
    teams[2] = []
    teams[3] = []
    teams[4] = []
    teams[5] = []
    for info in interviewer:
        #info = list(person.values())[0]
        teams[info['team']].append(person)
    for team in teams:
        print("{}: {}".format(team,teams[team]))

def interviewer_time(interviewer):
    print("interviewer time")
    time = [0]*30
    availability = {}
    availability[1] = [0]*30
    availability[2] = [0]*30
    availability[3] = [0]*30
    availability[4] = [0]*30
    availability[5] = [0]*30
    for info in interviewer:
        #info = list(person.values())[0]
        time = info['availability']
        for i in range(len(time)):
            availability[info['team']][i] = availability[info['team']][i] + time[i]
    for team in availability:
        print(availability[team])
    return availability

def is_available(interviewer, team, i):
    order = list(range(0,len(interviewer)))
    random.shuffle(order)
    #for i in order:
    #    person = interviewer[i]
    interviewer_sorted = sorted(interviewer, key=lambda k: k['num_int'])
    for info in interviewer_sorted:
        #info = list(person.values())[0]
        if info['team'] == team and info['availability'][i] == 1 and info['num_int'] < info['max_int']:
            return info['ID']
    return 0

def simple_match(interviewee, interviewer):
    num_match = 0
    interviewee_sorted = sorted(interviewee, key=lambda k: k['num_slots'])
    for person in interviewee_sorted:
        interest1 = person['interests'][0]
        interest2 = person['interests'][1]
        time = person['time']
        order = list(range(0,len(time)))
        random.shuffle(order)
        for i in order:
            if time[i] == 1 and is_available(interviewer, interest1, i) != 0 and is_available(interviewer, interest2, i) != 0:
                id1 = is_available(interviewer, interest1, i)
                id2 = is_available(interviewer, interest2, i)
                for p in interviewer:
                    if id1 == list(p.values())[0] or id2 == list(p.values())[0]:
                        p['num_int'] += 1
                        p['availability'][i] += 2
                        p['interviews'][i] = person['ID']
                person['final_time'] = i
                num_match += 1
                break
    return num_match

def random_match(interviewee, interviewer):
    num_match = 0
    interviewee_sorted = random.sample(interviewee, len(interviewee))
    for person in interviewee_sorted:
        interest1 = person['interests'][0]
        interest2 = person['interests'][1]
        time = person['time']
        order = list(range(0,len(time)))
        random.shuffle(order)
        for i in order:
            if time[i] == 1 and is_available(interviewer, interest1, i) != 0 and is_available(interviewer, interest2, i) != 0:
                id1 = is_available(interviewer, interest1, i)
                id2 = is_available(interviewer, interest2, i)
                for p in interviewer:
                    if id1 == list(p.values())[0] or id2 == list(p.values())[0]:
                        p['num_int'] += 1
                        p['availability'][i] += 2
                        p['interviews'][i] = person['ID']
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
    e = list(best_case.values())[0][0]
    r = list(best_case.values())[0][1]
    return [e, r, num_match]

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)

    interviewee = data['interviewee']
    interviewer = data['interviewer']

    min_std = 10000
    max_match = 0
    best = []
    for i in range(100):
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
        mean_loss = loss/num_p
        #print(mean_loss)
        if num_match >= max_match and mean_loss < min_std:
            best = [interviewee_matched, interviewer_matched]
            min_std = mean_loss
            max_match = num_match


    interviewee = best[0]
    interviewer = best[1]
    print('interviewees:')
    for person in interviewee:
        print(person)
    print('interviewers:')
    for person in interviewer:
        print(person)
    print("num_match={}, std={}".format(max_match, min_std))

    all_data = {'interviewee': interviewee, 'interviewer':interviewer}
    with open('matched.json', 'w') as file:
        file.write(json.dumps(all_data))


if __name__ == '__main__':
    main()
