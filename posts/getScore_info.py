import re

class ScoreLive(object):
    def __init__(self):
        self.series_info = {}


    def getScore(self, data):
        # if  data['homeTeam']['teamColour']  and data['awayTeam']['teamColour'] and data['homeTeam']['logoUrl'] and data['awayTeam']['logoUrl']:
        if data['homeTeam'].has_key("teamColour"):

            self.series_info = {'series_id':data['series']['id'],
                                'match_id': data['id'],
                                'series_name': data['series']['shortName'],
                                'homeTeam': data['homeTeam']['shortName'],
                                'homeTeam_color': data['homeTeam']['teamColour'],
                                'homeTeam_logo': data['homeTeam']['logoUrl'],
                                'awayTeam':data['awayTeam']['shortName'],
                                'awayTeam_color': data['awayTeam']['teamColour'],
                                'awayTeam_logo':data['awayTeam']['logoUrl'],
                                'homeScore': data['scores']['homeScore'],
                                'homeOvers': data['scores']['homeOvers'],
                                'awayScore': data['scores']['awayScore'],
                                'awayOvers': data['scores']['awayOvers'],

                                }
        else:

            self.series_info = {'series_id': data['series']['id'],
                                'match_id': data['id'],
                                'series_name': data['series']['shortName'],
                                'homeTeam': data['homeTeam']['shortName'],
                                # 'homeTeam_color': '#ffa500',
                                'homeTeam_logo': 'http://127.0.0.1:8000/media/2016/06/23/2594.gif',
                                'awayTeam': data['awayTeam']['shortName'],
                                # 'awayTeam_color': '#ffa500',
                                'awayTeam_logo': 'http://127.0.0.1:8000/media/2016/06/23/2594.gif',
                                'homeScore': data['scores']['homeScore'],
                                'homeOvers': data['scores']['homeOvers'],
                                'awayScore': data['scores']['awayScore'],
                                'awayOvers': data['scores']['awayOvers'],

                                }

class TeamInfo(object):
    def __init__(self):
        self.teams = {}
    def getTeam(self, data):
        self.teamInfo = {

                        'hometeam':data['homeTeam']['shortName'],
                        # 'hometeam_full': re.sub('\Men$', '', data['homeTeam']['name']),
                        'hometeam_full': data['homeTeam']['name'],
                        'awayteam_full': data['awayTeam']['name'],
                        'homelogo': data['homeTeam']['logoUrl'],
                        'homecolor': data['homeTeam']['teamColour'],
                        'awayteam': data['awayTeam']['shortName'],
                        'awaylogo': data['awayTeam']['logoUrl'],
                        'awaycolor': data['awayTeam']['teamColour'],
                        'homeScore':data['scores']['homeScore'],
                        'awayScore': data['scores']['awayScore'],
                        'startDate': data['localStartDate'],
                        'result': data['matchSummaryText'],
                        'venue': data['venue']['name'],


                        }

class ScoreCard(object):
    def __init__(self):
        # self.scorecard = {}
        self.batsmen = []
        self.bowlers= []
        self.other_info= []


    def getScoreCard(self, data):
        for innings in data['innings']:
            self.batsmen.append(innings['batsmen'])
            self.bowlers.append(innings['bowlers'])
            self.other_info={
                'wicket' : innings['wicket'],
                'run': innings['run'],
                'over': innings['over'],
                'extra': innings['extra'],
                'bye': innings['bye'],
                'legBye': innings['legBye'],
                'wide': innings['wide'],
                'noBall': innings['noBall'],
            }
            # dict(zip('innings', innings))
