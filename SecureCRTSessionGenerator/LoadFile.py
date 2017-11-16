
class LoadFile:
    def __init__(self):
        self._folderProperty = []
        self._defaultProperty = []

    def getFileProperty(self, folderDataPath, defaultPath):
        self._folderProperty = self.loadFile(folderDataPath)
        self._defaultProperty = self.loadFile(defaultPath)
        return self._folderProperty, self._defaultProperty

    def loadFile(self, filePath):
        propertyList = []
        fp = open(filePath, 'r+', encoding = 'utf-8')
        lines = fp.readlines()
        for line in lines:
            line = line.encode('utf-8').decode('utf-8-sig')
            params = []
            if(line != ''):
                params = line.split('=', 1)
                if(len(params) == 1):
                    propertydic = {
                        params[0] : "="
                    }
                    propertyList.append(propertydic)
                else:
                    propertydic = {
                        params[0] : params[1]
                    }
                    propertyList.append(propertydic)
        
        fp.close()
        return propertyList


LoadFile = LoadFile()