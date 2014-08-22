__author__ = 'team3.aka.the.best.team'

import web
import urllib2
import unpacker
from test_data import getPersonTestData, getPersonSkillTestData, getProjectTestData, getProjectSkillTestData

urls = (
    '/match', 'match',
    '/match/project/(.*)', 'matchProjectSingle',
    '/getPerson', 'getPerson',
    '/getPersonSkill', 'getPersonSkill',
    '/getProject', 'getProject',
    '/getProjectSkill', 'getProjectSkill'
)

app = web.application(urls, globals())


class matchProjectSingle:
    def GET(self, projectId):
        theMatch = match()
        return theMatch.doEverything(projectId, -1)


class getPerson:
    def GET(self):
        return getPersonTestData()


class getPersonSkill:
    def GET(self):
        return getPersonSkillTestData()


class getProject:
    def GET(self):
        return getProjectTestData()


class getProjectSkill:
    def GET(self):
        return getProjectSkillTestData()


def removeUnicodeChars(list):
    newlist = []
    for item in list:	#iterate over the individual tuples
        try:
            item = item.decode('unicode_escape').encode('ascii','ignore') # remove the unicode
        except AttributeError: # catch for non-unicode chars
            item = item
        newlist.append(item) # append to the new list (does not seem to like it when trying to change it in the old list)
    return newlist


class match:
    def GET(self):
        return self.doEverything(-1, -1)

    def doEverything(self, projectId, personId):
        """get all the info as lists"""
        #get persons
        personsString = self.getAllPersons()
        personsList = unpacker.makePersonsStringIntoObjects(personsString)
        #get personSkills
        personSkillsString = self.getAllPersonSkills()
        personSkillsList = unpacker.makePersonSkillsStringIntoObjects(personSkillsString)
        #get projects
        projectsString = self.getAllProjects(projectId)
        projectsList = unpacker.makeProjectsStringIntoObjects(projectsString)
        #get projectSkills
        projectSkillsString = self.getAllProjectSkills()
        projectSkillsList = unpacker.makeProjectSkillsStringIntoObjects(projectSkillsString)

        #get the skills for the person
        for person in personsList:
            person.setPersonSkills(personSkillsList)
        for project in projectsList:
            project.setProjectSkills(projectSkillsList)
        #for each project, find people with skills
        self.match(projectsList, personsList)
        #return everything in a nice format
        return self.displayInfo(projectsList, projectId, personId)

    def displayInfo(self, projectsList, projectId, personId):
        output = ''
        if projectId == -1:
            for project in projectsList:
                output += project.outputInfo()
        else:
            for project in projectsList:
                if project.id == projectId:
                    output += project.outputInfo()
        return output

    def match(self, projectsList, personsList):
        """by this point we have all the info in objects and we want to match people to projects"""
        for project in projectsList:
            for person in personsList:
                if ((person.availability is None) or (person.availability == '0'))\
                   and (person.compare(project.skills)):
                    project.capablePersons.append(person)

    def getAllPersons(self):
        return urllib2.urlopen('http://localhost:8080/getPerson').read()

    def getAllPersonSkills(self):
        return urllib2.urlopen('http://localhost:8080/getPersonSkill').read()

    def getAllProjects(self, projectId):
        return urllib2.urlopen('http://localhost:8080/getProject').read()
    #def getAllProjects(self, projectId):
    #    if projectId == -1:
    #        return urllib2.urlopen('http://localhost:8080/getProject').read()
    #    else:
    #        return urllib2.urlopen('http://localhost:8080/getProject/' + str(projectId)).read()

    def getAllProjectSkills(self):
        return urllib2.urlopen('http://localhost:8080/getProjectSkill').read()


class Person:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.availability = None
        self.availabilityDate = ''
        self.position = -1
        self.employeeType = ''
        #this will be a list of PersonSkills
        self.skills = []

    def setPersonSkills(self, personSkillsList):
        """creates a list of skills that this person has"""
        for personSkill in personSkillsList:
            # personSkillsList
            if self.id == personSkill.personId:
                self.skills.append(personSkill)

    def compare(self, skillList):
        """if the person has the required skills return True, skillList will be a list of projectSkills"""
        for projectSkill in skillList:
            gotSkill = False
            if (projectSkill.levelMin == '0') and not (self.haveSkillAtAnyLevel(projectSkill)):
                gotSkill = True
            for personSkill in self.skills:
                if self.isRightSkill(projectSkill, personSkill)\
                    and (projectSkill.levelMin <= personSkill.level) and (projectSkill.levelMax >= personSkill.level):
                    gotSkill = True
            if gotSkill == False:
                return False
        return True

    def isRightSkill(self, projectSkill, personSkill):
        return (personSkill.categoryId == projectSkill.categoryId) and (personSkill.skillId == projectSkill.skillId)

    def haveSkillAtAnyLevel(self, projectSkill):
        """ returns true if the person has the skill"""
        retVal = False
        for personSkill in self.skills:
            if self.isRightSkill(projectSkill, personSkill):
                retVal = True
        return retVal


class Skill:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.categoryId = -1


class PersonSkill:
    def __init__(self):
        self.id = -1
        self.personId = -1
        self.skillId = -1
        self.level = -1
        self.categoryId = -1


class Project:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.client = ''
        self.startdate = ''
        self.enddate = ''
        self.status = ''
        self.numberOfPeople = 1
        self.skills = []
        self.capablePersons = []

    def setProjectSkills(self, projectSkillsList):
        """sets all the skills for this project, puts a list of projectSkills on each project object"""
        for projectSkill in projectSkillsList:
            if self.id == projectSkill.projectId:
                self.skills.append(projectSkill)

    def outputInfo(self):
        output = '-----------------------------------------\n'
        output += 'Project ID: ' + str(self.id) + '\n'
        output += 'Project: ' + self.name + '\n'

        output += 'Client: ' + self.client + '\n\n'
        output += 'Capable people:\n'
        if len(self.capablePersons) < 1:     ######project.numberNeeded: # for underavailability
            output += 'Not enough capable people available\n\n'
        #sort list
        self.capablePersons = sorted(self.capablePersons, key=lambda personInList: personInList.position)
        for person in self.capablePersons:
            output += person.name + '\n'
        return output


class ProjectSkill:
    def __init__(self):
        self.id = -1
        self.projectId = -1
        self.skillId = -1
        self.levelMin = 0
        self.levelMax = 5
        self.categoryId = -1


class Category:
    def __init__(self):
        self.categoryId = -1
        self.name = ''

if __name__ == "__main__":
    app.run()