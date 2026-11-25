collaboratorsList = []

class TestClass:
    
    def newRepository(self,repositoryName, description, repositoryOwner):
        tempList = [repositoryName,description,repositoryOwner]
        return tempList
    def addCollaborator(self, collaboratorName):
        collaboratorsList.append(collaboratorName)
        
    def listCollaborators(self):
        return collaboratorsList
    
    def lookupCollaborator(self):
        return "Garrett Capps"
