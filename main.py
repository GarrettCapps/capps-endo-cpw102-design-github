from classes import testClass


def main():
    repoList = []
    repository = testClass.TestClass()
    
    print("Name of repository")
    name = input()
    print("Description for repository")
    description = input()
    print("Name of owner of repository")
    owner = input()
    repoList.append(repository.newRepository(name,description,owner))

    testName = input()
    repository.addCollaborator(testName)




main()