import json


def main():
    f = open('sample.json')
    data = json.load(f)
    teams = import_interviewee(data)
    #teams = import_interviewer(data, teams)
    f.close()

def add(team, availability):
    for i in range(len(availability)):
        team[i] += availability[i]
    return team

def subtract(team, availability):
    for i in range(len(availability)):
        if team[i] > 0:
            team[i] -= availability[i]
    return team

def import_interviewee(data):
    list1 = [0]*30
    list2 = [0]*30
    list3 = [0]*30
    list4 = [0]*30
    list5 = [0]*30
    teams = {'team1':list1, 'team2':list2, 'team3':list3, 'team4':list4, 'team5':list5}
    interviewee = data['interviewee']
    for person in interviewee:
        availability = person['time']
        interests = person["interests"]
        for team in teams.keys():
            if team in interests:
                teams[team] = add(teams[team], availability)
    print("interviews needed:")
    for team, list in teams.items():
        print(*list, sep = ', ')
    return teams

def import_interviewer(data, teams):
    interviewee = data['interviewee']
    interviewer = data['interviewer']
    for person in interviewer:
        availability = person['time']
        team = person["team"]
        teams[team] = subtract(teams[team], availability)
    print("after")
    for team, list in teams.items():
        print(*list, sep = ', ')
    return teams

if __name__ == '__main__':
    main()
