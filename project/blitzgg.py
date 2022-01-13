import scrapy
import re, json
from datetime import datetime
from requests import get
from scrapy import Selector
from collections import deque
from .timeline import parse_timeline
from urllib.parse import unquote
from selenium import webdriver

class BLITZGGSpider(scrapy.Spider):

    name = "blitzgg"
    handle_httpstatus_list = [500]
    custom_settings = {
        'HTTPERROR_ALLOWED_CODES': [500]
    }

    # SELENIUM CHANGES START 1
    driver = webdriver.Chrome('./chromedriver')
    # SELENIUM CHANGES END 1

    def start_requests(self):

        with open('trackingthepros2.json') as fd:
            proplayers = json.load(fd)

        # load selenium webdriver

        for player_dict in proplayers:
            for x in player_dict.values():
                for player, area, rank in x:
                    if area != '[KR]':
                        continue

                    # url_player = f'https://blitz.gg/lol/profile/kr/{player}'
                    url_player = f"https://beta.iesdev.com/api/lolapi/kr/accounts/name/{player}?force=false"
                    yield scrapy.Request(url=url_player, callback=self.parse_player, meta={'player_name': player})



    def parse_player(self, response):

        playerid = response.json()['data']['accountId']
        '''
        for script in response.css('body script::text').getall():
            if not script.strip().startswith('window.__PRELOADED_STATE__'):
                continue
            s = re.search('(accountId":")([\w]+)(")', script)
            if s:
                playerid = s.group(2)

        if not playerid:
            return None
        '''

        query_url = f'https%3A%2F%2Fbeta.iesdev.com%2Fgraphql%3Fquery%3Dquery%20matches(%24region%3ARegion!%2C%24accountId%3AString!%2C%24first%3AInt%2C%24role%3ARole%2C%24queue%3AQueue%2C%24championId%3AInt)%7Bmatches(region%3A%24region%2CaccountId%3A%24accountId%2Cfirst%3A%24first%2Crole%3A%24role%2Cqueue%3A%24queue%2CchampionId%3A%24championId)%7Bid%20riotMatchId%20gameCreation%20duration%20queue%20region%20leaguePatch%7BmajorVersion%20minorVersion%7DplayerMatches%7BaccountId%20league_profile(region%3A%24region)%7BsummonerName%7DteamId%20role%20champion%7Bid%20name%20normalizedName%7DmatchStatsFromClient%7Blp%7DplayerMatchStats%7BgoldEarned%20goldSpent%20win%20kills%20assists%20deaths%20time_cc_others%20total_time_cc_dealt%20wards_purchased%20wardsPlaced%20wardsKilled%20damageDealt%20damage_to_champions%20damage_to_towers%20damage_to_objectives%20damageSelfMitigated%20damage_taken%20damage_healed%20damage_physical_dealt%20damage_magic_dealt%20damage_true_dealt%20minions_killed_neutral%20minions_killed_enemy_jungle%20minions_killed_team_jungle%20minions_killed_total%20killingSprees%20doubleKills%20tripleKills%20quadraKills%20pentaKills%20first_blood%20firstInhibitorKill%20firstTowerKill%20champLevel%20largest_critical%20largestKillingSpree%20largestMultiKill%20turrets_killed%20perkPrimaryStyle%20perkSubStyle%20perks%20spells%20items%20visionScore%7D%7D%7D%7D%26variables%3D%7B%22region%22%3A%22KR%22%2C%22accountId%22%3A%22{playerid}%22%2C%22first%22%3A500%2C%22queue%22%3A%22RANKED_SOLO_5X5%22%7D'

        yield scrapy.Request(url=unquote(query_url), callback=self.query_matches, meta={'playerid':playerid,
                                                                                        'player_name': response.meta['player_name']})

    def query_matches(self, response):

        data = response.json()['data']['matches']
        player_name = response.meta['player_name']
        playerid = response.meta['playerid']
        matchids = [z['riotMatchId'] for z in data]

        for matchid in matchids:
            url = f'https://blitz.gg/lol/match/kr/{player_name}/{matchid}'
    #         yield scrapy.Request(url=url, callback=self.parse_match, meta={'playerid': playerid, 'matchid': matchid,
    #                                                                         'player_name': player_name, 'handle_httpstatus_list': [500]})
    #
    # def parse_match(self, response):

    # SELENIUM CHANGES START 2
            driver.get(url)

            selenium_response = driver.page_source

            dic = {'player_name': player_name,
                    'playerid': playerid,
                    'matchid': matchid,
                    'timeline': parse_timeline(selenium_response)}
    # SELENIUM CHANGES END 2

        yield dic

        '''
        for player_name in response.css('p.bkcvUa::text').getall():
            url = f"https://blitz.gg/lol/match/kr/{player_name}/{response.meta['matchid']}"
            yield scrapy.Request(url=url, callback=self.parse_match, meta={'playerid': player,
                                                                            'matchid': response.meta['matchid'],
                                                                            'player_name': player_name})
        '''

        for player in response.css('p.bkcvUa::text').getall():
            '''url_player = f'https://blitz.gg/lol/profile/kr/{player}'''
            url_player = f"https://beta.iesdev.com/api/lolapi/kr/accounts/name/{player}?force=false"
            yield scrapy.Request(url=url_player, callback=self.parse_player, meta={'player_name': player})
