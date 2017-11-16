import os

class GenSession:
    def genSessions(self, sessionRootDir, channelist, folderDataTemplate, defaultTemplate):
        for channel in channelist:
            os.chdir(sessionRootDir)

            channelName = channel['channelName']
            self.mkdir(channelName)
            channelDir = os.getcwd() + '\\' + channelName
            os.chdir(channelDir)

            serverList = channel['serverList']
            for server in serverList:
                serverName = server['serverName']
                self.mkdir(serverName)
                serverDir = os.getcwd() + '\\' + serverName

                sessionList = server['sessionList']
                for session in sessionList:
                    hostName = session['hostName']
                    userName = session['userName']
                    sessionName = session['sessionName']
            
                    sessionFileStr = ''
                    for sessionPropertyDict in defaultTemplate:
                        for key in sessionPropertyDict:
                            sessionFileStr += key
                            if key == 'S:"Username"':
                                sessionFileStr += '=' + userName + '\n'
                            elif key == 'S:"Hostname"':
                                sessionFileStr += '=' + hostName + '\n'
                            else:
                                if sessionPropertyDict[key] != '=':
                                    sessionFileStr += '=' + sessionPropertyDict[key]

                    sessionDir= serverDir + '\\' + channelName + '-' + serverName + '@' + sessionName + '(' + hostName + ')' + '.ini'
                    fp = open(sessionDir, 'w', encoding = 'utf-8')  
                    fp.write(sessionFileStr)
                    fp.close()

                self.genFolderData(serverDir, folderDataTemplate)

        self.genFolderData(os.getcwd(), folderDataTemplate)
        self.genFolderData(os.path.abspath(os.path.join(os.getcwd(), "..")), folderDataTemplate)

    def genFolderData(self, path, folderDataTemplate):
        folderList, sessionList = self.getPathList(path)
        if '__FolderData__.ini' in sessionList:
            sessionList.remove('__FolderData__.ini')

        sessions = []
        for session in sessionList:
            param = session.split('.', 1)
            sessions.append(param[0])

        folderListStr = self.genStrFromList(folderList)
        sessionListStr = self.genStrFromList(sessions)

        folderFileStr = ''
        for folderPropertyDict in folderDataTemplate:
            for key in folderPropertyDict:
                folderFileStr += key
                if key == 'S:"Folder List"':
                    folderFileStr += '=' + folderListStr
                elif key == 'S:"Session List"':
                    folderFileStr += '=' + sessionListStr
                else:
                    if folderPropertyDict[key] != '=':
                        folderFileStr += '=' + folderPropertyDict[key]

        folderName = path + '\\' + '__FolderData__.ini'
        fp = open(folderName, 'w', encoding = 'utf-8')
        fp.write(folderFileStr)
        fp.close()

    def mkdir(self, path):
        path = path.strip()
        path = path.rstrip("\\")

        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            
    def getPathList(self, path):
        folderListStr = []
        sessionListStr = []
        params = os.listdir(path)
        for param in params:
            if(os.path.isdir(path + '\\' + param)):
                folderListStr.append(param)
            if(os.path.isfile(path + '\\' + param)):
                sessionListStr.append(param)

        return folderListStr, sessionListStr

    def genStrFromList(self, tmplist):
        tmpStr = ''
        for val in tmplist:
            tmpStr += val + ':'

        tmpStr += '\n'
        return tmpStr
    
GenSession = GenSession()