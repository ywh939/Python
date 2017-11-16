# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

class ParseXml:
    def __init__(self):
        self._root = ""

    def loadXml(self, xmlDir):
        domTree = xml.dom.minidom.parse(xmlDir)
        self._root = domTree.documentElement

    def getSessionDir(self):
        sessionRoot = self._root.getElementsByTagName('sessionRoot')

        for rootDir in sessionRoot:
            if rootDir.hasAttribute('dir'):
                return rootDir.getAttribute('dir')

    def getServersList(self):
        channelist = []
        channels = self._root.getElementsByTagName('channel')
        for channel in channels:
            channelName = ''
            if channel.hasAttribute('name'):
                channelName = channel.getAttribute('name')

            serverList = []
            servers = channel.getElementsByTagName('server')
            for server in servers:
                serverName = ''
                if server.hasAttribute('name'):
                    serverName = server.getAttribute('name')
                
                sessionList = []
                sessions = server.getElementsByTagName('session')
                for session in sessions:
                    sessionName = ''
                    if session.hasAttribute('name'):
                        sessionName = session.getAttribute('name')

                    hostName = session.getElementsByTagName('hostName')[0].childNodes[0].data
                    #userName = server.getElementsByTagName('userName')[0].childNodes[0].data
                    sessionDict = {
                        'hostName' : hostName,
                        'userName' : 'root',
                        'sessionName' : sessionName
                    }
                    sessionList.append(sessionDict)

                serverDict = {
                    'serverName' : serverName,
                    'sessionList' : sessionList
                }
                serverList.append(serverDict)
            
            channelDict = {
                'channelName' : channelName,
                'serverList' : serverList,
            }
            channelist.append(channelDict)
        
        return channelist

ParseXml = ParseXml()