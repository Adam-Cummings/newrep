def getPersonTestData():
    return '[{"EmployeeID":"33", "Name":"James", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"7", "EmploymentType":"0"}]'


def getPersonSkillTestData():
        return '[{"EmployeeSkillID":"35", "EmployeeID":"33", "SkillID":"30", "SkillLevel":"3", "CategoryID":"31"}]'


def getProjectTestData():
        return '[{"ProjectID":"39", "Name":"testproject30s", "Client":"adamisclient", "Status":"0", "NumberOfPeople":"3", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}]'


def getProjectSkillTestData():
        return '[{"ProjectSkillID":"40", "ProjectID":"39", "SkillID":"30", "LevelMin":"3", "LevelMax":"5", "CategoryID":"31"}]'



"""
2 projects
4 employees
projects: 2 employees pass, 1 fails, 1 unavailable
this shows that 1 person is matched to many projects and also that projects dont take everyone

"""