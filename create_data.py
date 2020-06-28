import random
from operator import itemgetter

def create_interviewee(n):
    print("interviewees")
    interviewee = []
    for i in range(n):
        person = {}

        zero_count = random.randint(0, 25)
        one_count = 30 - zero_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        person['ID'] = random.randint(10000,19999)
        person['name'] = 'name'
        person['interests'] = random.sample(range(1, 6), 2)
        person['time'] = my_list
        person['final_time'] = 100
        person['num_slots'] = one_count
        interviewee.append(person)

        print(person)
    return interviewee

def create_interviewer(n):
    print("interviewers")
    interviewer = []
    for i in range(n):
        person = {}
        person_with_id = {}
        zero_count = random.randint(0, 20)
        one_count = 30 - zero_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)

        ID = random.randint(20000,29999)
        person['ID'] = ID
        person['name'] = 'name'
        person['team'] = random.randint(1,5)
        person['availability'] = my_list
        person['num_int'] = 0
        person['max_int'] = 5
        person_with_id[ID] = person

        interviewer.append(person_with_id)

        print(person_with_id)
    return interviewer

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
    for person in interviewer:
        info = list(person.values())[0]
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
    for person in interviewer:
        info = list(person.values())[0]
        time = info['availability']
        for i in range(len(time)):
            availability[info['team']][i] = availability[info['team']][i] + time[i]
    for team in availability:
        print(availability[team])
    return availability

def is_available(interviewer, team, i):
    for person in interviewer:
        info = list(person.values())[0]
        if info['team'] == team and info['availability'][i] == 1:
            if info['num_int'] < info['max_int']:
                info['num_int'] += 1
                info['availability'][i] -= 1
            return info['ID']
    return 0



def simple_match(interviewee, interviewer):
    print("simple match")
    #teams = interviewer_by_team(interviewer)
    #interviewee_sorted = sorted(interviewee, key=itemgetter(-'num_slots'))
    interviewee_sorted = sorted(interviewee, key=lambda k: k['num_slots'])
    for person in interviewee_sorted:
        interest1 = person['interests'][0]
        interest2 = person['interests'][1]
        time = person['time']
        order = list(range(0,30))
        random.shuffle(order)
        for i in order:
            if time[i] == 1 and is_available(interviewer, interest1, i) != 0 and is_available(interviewer, interest2, i) != 0:
                person['final_time'] = i
                break
        print(person)
    #matched = []
    #itr = 0
    #for person in interviewee:
    #    matched.append(person['final_time'])
    #    print(person)
    #print(matched)

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
    interviewee = create_interviewee(20)
    #interviewee_time(interviewee)
    interviewer = create_interviewer(15)
    #interviewer_time(interviewer)
    #interviewer_by_team(interviewer)
    simple_match(interviewee, interviewer)


if __name__ == '__main__':
    main()
