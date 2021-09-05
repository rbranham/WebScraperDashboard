import json
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

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


def addPercentage(statDF):
    """ Function to add column with win percentage"""
    statDF['win_pct'] = statDF['wins'] / (statDF['wins'] + statDF['losses'])
    return statDF




# Set up dataframe
statsDF = pd.DataFrame.from_dict(loadConferenceStats(1))
teamList = pd.DataFrame.from_dict(loadTeams())
seasonList = pd.DataFrame.from_dict(loadSeasons())

statsDF = replaceTeamID(statsDF, teamList)
statsDF = replaceSeasonId(statsDF, seasonList)
statsDF = addPercentage(statsDF)

statsDF = statsDF.sort_values(by='seasonId')

########################### Dash Code #####################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.line(statsDF, x="seasonId", y="win_pct", color="teamId")

app.layout = html.Div([
    dcc.Graph(
        id='line-graph',
        figure=fig
    )
])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Main function"""
    print(statsDF)
    app.run_server(debug=True)

    # teams = loadTeams()
    # for team in teams:
    #     print(team)

