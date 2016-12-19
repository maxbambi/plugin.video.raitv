﻿# -*- coding: utf-8 -*-
import urllib2
import json

class RaiPlay:
    # From http://www.raiplay.it/mobile/prod/config/RaiPlay_Config.json
    baseUrl = "http://www.rai.it/"
    channelsUrl = "http://www.rai.it/dl/RaiPlay/2016/PublishingBlock-9a2ff311-fcf0-4539-8f8f-c4fee2a71d58.html?json"
    localizeUrl = "http://mediapolisgs.rai.it/relinker/relinkerServlet.htm?cont=201342"
    menuUrl = "http://www.rai.it/dl/RaiPlay/2016/menu/PublishingBlock-20b274b1-23ae-414f-b3bf-4bdc13b86af2.html?homejson"
    palinsestoUrl = "http://www.rai.it/dl/palinsesti/Page-e120a813-1b92-4057-a214-15943d95aa68-json.html?canale=[nomeCanale]&giorno=[dd-mm-yyyy]"
    AzTvShowPath = "/dl/RaiTV/RaiPlayMobile/Prod/Config/programmiAZ-elenco.json"
    nothumb = "http://www.rai.it/cropgd/256x-/dl/components/img/imgPlaceholder.png"
    
    def getCountry(self):
        response = urllib2.urlopen(self.localizeUrl).read()
        return response
        
    def getChannels(self):
        response = json.load(urllib2.urlopen(self.channelsUrl))
        return response["dirette"]
        
    def getProgrammes(self, channelName, epgDate):
        channelTag = channelName.replace(" ", "")
        url = self.palinsestoUrl
        url = url.replace("[nomeCanale]", channelTag)
        url = url.replace("[dd-mm-yyyy]", epgDate)
        response = json.load(urllib2.urlopen(url))
        return response[channelName][0]["palinsesto"][0]["programmi"]
        
    def getMainMenu(self):
        response = json.load(urllib2.urlopen(self.menuUrl))
        # TODO: these entries must be filtered in default
        return response["menu"]

    # RaiPlay Genere Page
    # RaiPlay Tipologia Page
    def getCategory(self, url):
        response = json.load(urllib2.urlopen(url))
        return response["blocchi"]
  
    # Raiplay Tipologia Item
    def getProgrammeList(self, url):
        response = json.load(urllib2.urlopen(url))
        return response
    
    #  PLR programma Page
    def getProgramme(self, url):
        response = json.load(urllib2.urlopen(url))
        return response["Blocks"]
    
    def getContentSet(self, url):
        response = json.load(urllib2.urlopen(url))
        return response["items"]
    
    def getVideoUrl(self, pathId):
        response = json.load(urllib2.urlopen(self.baseUrl + pathId))
        url = response["video"]["contentUrl"]
        return url
