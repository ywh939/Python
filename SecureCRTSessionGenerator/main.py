from ParseXml import ParseXml
from LoadFile import LoadFile
from GenSession import GenSession


if __name__ == '__main__':

    ParseXml.loadXml("./config.xml")
    sessionRootDir = ParseXml.getSessionDir()
    channelist = ParseXml.getServersList()

    defaultFolderDataDir = sessionRootDir + '\\__FolderData__.ini'
    defaultPropertyDir = sessionRootDir + '\\Default.ini'

    folderDataTemplate, defaultTemplate = LoadFile.getFileProperty(defaultFolderDataDir, defaultPropertyDir)

    GenSession.genSessions(sessionRootDir, channelist, folderDataTemplate, defaultTemplate)