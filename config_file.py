'''
MAIN_APP_PAGE_CONFIGURATION
'''
timeline_list = ['all-time','2008','2009','2010','2011','2012','2013','2014','2015','2016',
'2017','2018','2019','2020','2021']
#-------------------------------------------------------------------------------
'''
BATSMEN_APP_PAGE_CONFIGURATION
------------------------------
'''
batting_feature_mapping={
'Most Runs':'most-runs',
'Most Sixes':'most-sixes',
'Most Sixes Innings':'most-sixes-innings',
'Highest Score':'highest-scores',
'Best Strike Rate':'best-batting-strike-rate',
'Best Strike Rate Innings':'best-batting-strike-rate-innings',
'Best Average':'best-batting-average',
'Most 50s':'most-fifties',
'Most 100s':'most-centuries',
'Most 4s':'most-fours',
'Fastest 50':'fastest-fifties',
'Fastest 100':'fastest-centuries',
}

# Feature Keys for DataFrame
feature_plot_mapping = {
'Most Runs':'Runs',
'Most Sixes':'6s',
'Most Sixes Innings':'6s',
'Highest Score':'HS',
'Best Strike Rate':'SR',
'Best Strike Rate Innings':'SR',
'Best Average':'Avg',
'Most 50s':'50',
'Most 100s':'100',
'Most 4s':'4s',
'Fastest 50':'BF',
'Fastest 100':'BF',
}

# Batting Stats Features
batting_stats_features = ['Most Runs', 'Most Sixes', 'Most Sixes Innings',
 'Highest Score', 'Best Strike Rate', 'Best Strike Rate Innings',
  'Best Average', 'Most 50s', 'Most 100s', 'Most 4s',
   'Fastest 50', 'Fastest 100']
#-------------------------------------------------------------------------------

'''
BOWLERS_APP_PAGE_CONFIGURATION
------------------------------
'''

bowling_feature_mapping={
'Most Wickets':'most-wickets',
'Most Wickets in an Inning':'best-bowling-innings',
'Best Average':'best-bowling-average',
'Best Economy':'best-bowling-economy',
'Best Strike Rate':'best-bowling-strike-rate',
'Best Strike Rate Innings':'best-bowling-strike-rate-innings',
'Most Runs Conceded':'most-runs-conceded-innings',
'Hat Tricks':'hat-tricks-innings',
'Most Hat Tricks':'most-hat-tricks',
'Most Dots Bowled':'most-dot-balls',
'Most Maiden Overs':'most-maidens',
'Most 4 Wickets':'most-four-wickets',
}

bowlers_feature_plot_mapping={
'Most Wickets':'Wkts',
'Most Wickets in an Inning':'Wkts',
'Best Average':'Avg',
'Best Economy':'Econ',
'Best Strike Rate':'SR',
'Best Strike Rate Innings':'SR',
'Most Runs Conceded':'Runs',
'Hat Tricks':'HT',
'Most Hat Tricks':'HT',
'Most Dots Bowled':'Dots',
'Most Maiden Overs':'Maid',
'Most 4 Wickets':'4w',
}

bowling_stats_features = ['Most Wickets', 'Most Wickets in an Inning',
 'Best Average', 'Best Economy', 'Best Strike Rate', 'Best Strike Rate Innings',
  'Most Runs Conceded', 'Hat Tricks', 'Most Hat Tricks', 'Most Dots Bowled',
   'Most Maiden Overs', 'Most 4 Wickets']
#-------------------------------------------------------------------------------
