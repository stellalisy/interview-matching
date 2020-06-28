import random
from operator import itemgetter
import json
import copy

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
                #info['num_int'] += 1
                #info['availability'][i] -= 1
                #info['interviews'].append(i)
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
                        p['availability'][i] -= 1
                        p['interviews'].append(i)
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
                        p['availability'][i] -= 1
                        p['interviews'].append(i)
                person['final_time'] = i
                num_match += 1
                break
    return num_match


def match_all(interviewee, interviewer):
    print("match all")
    matched = []
    itr = 0
    for person in interviewee:
        matched.append(person['final_time'])
    print(matched)
    while 100 in matched and itr < 100:
        simple_match(interviewee, interviewer)
        itr += 1
    print(itr)
    for person in interviewee:
        print(person)

def main():
    with open('data.txt', 'r') as file:
        data = json.load(file)

    interviewee = data['interviewee']
    interviewer = data['interviewer']

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

    print("num_match={}, itr={}".format(num_match,itr))
    interviewee = list(best_case.values())[0][0]
    interviewer = list(best_case.values())[0][1]

    print('interviewees:')
    for person in interviewee:
        print(person)
    print('interviewers:')
    for person in interviewer:
        print(person)


if __name__ == '__main__':
    main()
