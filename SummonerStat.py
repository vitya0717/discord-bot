class SummonerStat:
    # print('Name: ', player['summonerName'])
    # print('Kills: ', player['kills'])
    # print('Deaths: ', player['deaths'])
    # print('Assists: ', player['assists'])
    # print('Champ: ', player['championName'])
    def __init__(self, name, kills, deaths, assists, champ):
        self.name = name
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.champ = champ

    def __str__(self):
        return f"Name: {self.name}, Kills: {self.kills}, Deaths: {self.deaths}, Assists: {self.assists}, Champion: {self.champ}"
