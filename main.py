import json;


def loadTeams():
    """ Function to load teams, currently pulls from mock data, eventually could pull from an API"""
    return json.load(open('sample_json/teams.json'))


def loadConferenceStats(confId: int):
    """ Function to load stats, currently returns mock data"""
    return json.load(open('sample_json/conference_one.json'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for stat in loadConferenceStats(1):
        print(stat)


    # teams = loadTeams()
    # for team in teams:
    #     print(team)

