import json

from riotwatcher import LolWatcher

import main

lol_api = LolWatcher('RGAPI-e49fca25-c68c-45fb-8be5-57242cae747f')

region = 'EUN1'

mitter100 = lol_api.summoner.by_name(region, main.getRequestedSummoner())

match_ids = lol_api.match.matchlist_by_puuid(region, mitter100['puuid'])
match_data = []

for value in match_ids:
    match_data.append(lol_api.match.by_id(region, value))
player_ids = []
for player in match_data:
    player_ids.append(player['metadata']['participants'])


def getMatchData():
    return match_data


def getPlayerIdsInMatch():
    return player_ids


def getMatchIds():
    return match_ids


def getRegion():
    return region


def getApi():
    return lol_api
