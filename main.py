import json
import pandas as pd

def loadTeams():
    """ Function to load teams, currently pulls from mock data, eventually could pull from an API"""
    return json.load(open('sample_json/teams.json'))


def replaceTeamID(statDF, teamDF):
    """ Function to replace team ids with their name"""
    statDF['teamId'] = statDF['teamId'].replace(dict(zip(teamDF.id, teamDF.teamName)))
    return statDF


def loadSeasons():
    """ Function to load seasons """
    return json.load(open('sample_json/seasons.json'))


def replaceSeasonId(statDF, seasonDF):
    """ Function to replace season ids with their year string """
    statDF['seasonId'] = statDF['seasonId'].replace(dict(zip(seasonDF.id, seasonDF.seasonString)))
    return statDF


def loadConferenceStats(confId: int):
    """ Function to load stats, currently returns mock data"""
    return json.load(open('sample_json/conference_one.json'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Main function"""
    statsList = pd.DataFrame.from_dict(loadConferenceStats(1))
    teamList = pd.DataFrame.from_dict(loadTeams())
    seasonList = pd.DataFrame.from_dict(loadSeasons())
    # print(seasonList)

    statsList = replaceTeamID(statsList, teamList)
    statsList = replaceSeasonId(statsList, seasonList)
    print(statsList)


    # teams = loadTeams()
    # for team in teams:
    #     print(team)

