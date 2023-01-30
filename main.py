import discord

from dotenv import load_dotenv
from riotwatcher import LolWatcher

from SummonerStat import SummonerStat

load_dotenv()
DC_TOKEN = 'MTA2OTI2MzcxMDQzNjIxMjg1Ng.GH0xEF.D7i5jx7_N1f4Sbba63O-pB6Vr93ADmnke6fddc'
client = discord.Client(intents=discord.Intents.all())
lol_api = LolWatcher('RGAPI-85906373-08ff-4016-9926-fb28dd9cd526')
region = 'EUN1'


@client.event
async def on_message(text):
    chatMessage = str(text.content)
    info = []
    match_data = []
    player_ids = []
    output = ""
    if text.author == client.user:
        return
    if len(chatMessage) > 1 and chatMessage.startswith('?'):
        mitter100 = lol_api.summoner.by_name(region, chatMessage.split('?')[1])
        match_ids = lol_api.match.matchlist_by_puuid(region, mitter100['puuid'])
        for value in match_ids:
            match_data.append(lol_api.match.by_id(region, value))
        for player in match_data:
            player_ids.append(player['metadata']['participants'])
        for match in match_data:
            for player in lol_api.match.by_id(region, match['metadata']['matchId'])['info']['participants']:
                if player['summonerName'] == chatMessage.split('?')[1]:
                    info.append(SummonerStat(player['summonerName'], player['kills'], player['deaths'], player['assists'], player['championName']))
        for p in info:
            output += f"{info.index(p)+1}.Meccs\n{p.__str__()}\n"
        xd = ">>> "
        await text.channel.send(xd+output)
    elif len(chatMessage) > 1 and chatMessage == "!channels" and discord.utils.get(client.get_all_channels(), name="parancsok"):
        for c in client.get_all_channels():
            if c.name == "parancsok" and c.name == text.channel.name:
                print(c.name)
                await text.channel.send(f'jó hely')

client.run(DC_TOKEN)
