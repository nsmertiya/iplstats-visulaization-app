'''
Script for Scraping Data from the IPL Website
'''
import pandas as pd
from config_file import batting_feature_mapping
from config_file import bowling_feature_mapping


def batsmen_stats_dataframe(feature,timeline):
    '''
    Function to return Batting Dataframe from the iplt20 website for the
    provided feature and timeline.

    Params:
    -------
        feature (string): The metrics('most runs','Most 6s') for retriving data
        timeline (String): The Year or 'all-time' for stats on the metrics.

    Returns:
    --------
        Dataframe containing top 100 records for the feature and timeline.
    '''
    feature = batting_feature_mapping[feature]
    url = f'https://www.iplt20.com/stats/{timeline}/{str(feature)}'
    html = pd.read_html(url,header = 0)
    df = html[0]
    raw = df.fillna(0)

    # Condition for removing '*' from Highest Score
    if 'HS' in raw.columns:
        raw.HS = raw.HS.replace('\*','',regex=True)
        raw['HS'] = raw.HS.astype(int)

    return raw


def bowlers_stats_dataframe(feature,timeline):
    '''
    Function to return Bowling Dataframe from the iplt20 website for the
    provided feature and timeline.

    Params:
    -------
        feature (string): The metrics('most wickets') for retriving data.
        timeline (String): The Year or 'all-time' for stats on the metrics.

    Returns:
    --------
        Dataframe containing top 100 records for the feature and timeline.
    '''
    feature = bowling_feature_mapping[feature]
    url = f'https://www.iplt20.com/stats/{timeline}/{str(feature)}'
    html = pd.read_html(url,header = 0)
    df = html[0]
    raw = df.fillna(0)

    return raw


def player_stats_dataframe(timeline):
    '''
    Function to return Bowling Dataframe from the iplt20 website for the
    provided feature and timeline.

    Params:
    -------
        feature (string): The metrics('most wickets') for retriving data.
        timeline (String): The Year or 'all-time' for stats on the metrics.

    Returns:
    --------
        Dataframe containing top 100 records for the feature and timeline.
    '''
    url = f"https://www.iplt20.com/points-table/men/{timeline}"
    #url = f'https://www.iplt20.com/stats/{timeline}/{str(feature)}'
    html = pd.read_html(url,header = 0)
    df = html[0]
    raw = df.fillna(0)

    return raw
