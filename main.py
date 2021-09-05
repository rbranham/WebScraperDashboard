import json;
import pandas as pd

def loadTeams():
    """ Function to load teams, currently pulls from mock data, eventually could pull from an API"""
    return json.load(open('sample_json/teams.json'))


def loadConferenceStats(confId: int):
    """ Function to load stats, currently returns mock data"""
    return json.load(open('sample_json/conference_one.json'))

def replaceTeamID(statDF, teamDF):
    """ Function to replace team ids with their name"""
    statDF['teamId'] = statDF['teamId'].replace(dict(zip(teamDF.id, teamDF.teamName)))
    return statDF

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Main function"""
    statsList = pd.DataFrame.from_dict(loadConferenceStats(1))
    teamList = pd.DataFrame.from_dict(loadTeams())

    statsList = replaceTeamID(statsList, teamList)
    print(statsList)


    # teams = loadTeams()
    # for team in teams:
    #     print(team)

