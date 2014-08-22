def getPersonTestData():
    return \
        '[{"EmployeeID":"99", "Name":"Mitch McUnavailable", "Availability":"1", "AvailabilityDate":"2011-05-05", "Position":"9", "EmploymentType":"0"}, ' \
        \
        '{"EmployeeID":"11", "Name":"Terrence", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"6", "EmploymentType":"0"}, ' \
        '{"EmployeeID":"12", "Name":"Quentin", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"6", "EmploymentType":"0"}, ' \
        '{"EmployeeID":"13", "Name":"Humphrey", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"6", "EmploymentType":"0"}, ' \
        \
        '{"EmployeeID":"01", "Name":"James [position 9]", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"9", "EmploymentType":"0"}, ' \
        '{"EmployeeID":"02", "Name":"Katherine [position 8]", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"8", "EmploymentType":"0"}, ' \
        '{"EmployeeID":"03", "Name":"Lisa [position 6]", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"6", "EmploymentType":"0"}, ' \
        '{"EmployeeID":"04", "Name":"Matthew [position 7]", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"7", "EmploymentType":"0"}, ' \
        \
        '{"EmployeeID":"21", "Name":"Florence", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"3", "EmploymentType":"0"}, ' \
        '{"EmployeeID":"22", "Name":"Guinevere", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"3", "EmploymentType":"0"}]'




def getPersonSkillTestData():
    return \
        '[{"EmployeeSkillID":"99", "EmployeeID":"99", "SkillID":"30", "SkillLevel":"5", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"35", "EmployeeID":"01", "SkillID":"30", "SkillLevel":"4", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"36", "EmployeeID":"02", "SkillID":"30", "SkillLevel":"4", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"37", "EmployeeID":"03", "SkillID":"30", "SkillLevel":"4", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"38", "EmployeeID":"04", "SkillID":"30", "SkillLevel":"4", "CategoryID":"31"}, ' \
        \
        '{"EmployeeSkillID":"50", "EmployeeID":"11", "SkillID":"30", "SkillLevel":"2", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"51", "EmployeeID":"12", "SkillID":"30", "SkillLevel":"1", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"52", "EmployeeID":"13", "SkillID":"30", "SkillLevel":"2", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"52", "EmployeeID":"13", "SkillID":"31", "SkillLevel":"2", "CategoryID":"31"}, ' \
        \
        '{"EmployeeSkillID":"52", "EmployeeID":"21", "SkillID":"30", "SkillLevel":"3", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"52", "EmployeeID":"21", "SkillID":"40", "SkillLevel":"3", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"52", "EmployeeID":"22", "SkillID":"30", "SkillLevel":"3", "CategoryID":"31"}, ' \
        '{"EmployeeSkillID":"52", "EmployeeID":"22", "SkillID":"40", "SkillLevel":"2", "CategoryID":"31"}]'


def getProjectTestData():
    return '[{"ProjectID":"39", "Name":"Project Mystery [Skill 30 Level 5 required]", "Client":"Mr Client", "Status":"0", "NumberOfPeople":"3", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}, ' \
           '{"ProjectID":"40", "Name":"Project X [Skill 30 Level 1-2 required]", "Client":"Zarglax, Destroyer of Worlds", "Status":"0", "NumberOfPeople":"3", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}, ' \
           '{"ProjectID":"41", "Name":"Project Banal [Skill 30 Level 4 required]", "Client":"The Best Client", "Status":"0", "NumberOfPeople":"3", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}, ' \
        '{"ProjectID":"42", "Name":"Happy Balloon Fun Time Testing Conglomerate [Skill ID 30: Level 3 and Skill ID 40: Level 3 required]", "Client":"The client will be revealed on live TV", "Status":"0", "NumberOfPeople":"2", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}, ' \
        '{"ProjectID":"43", "Name":"Let\'s Be Friends [Skill ID 30: Level 3 and Skill ID 40: Level 2-3 required]", "Client":"Dr Death", "Status":"0", "NumberOfPeople":"2", "StartDate":"2013-05-12", "EndDate":"2013-05-20"}]'

def getProjectSkillTestData():
    return '[{"ProjectSkillID":"98", "ProjectID":"39", "SkillID":"30", "LevelMin":"5", "LevelMax":"5", "CategoryID":"31"}, ' \
           '{"ProjectSkillID":"97", "ProjectID":"40", "SkillID":"30", "LevelMin":"1", "LevelMax":"2", "CategoryID":"31"}, ' \
           '{"ProjectSkillID":"99", "ProjectID":"41", "SkillID":"30", "LevelMin":"4", "LevelMax":"4", "CategoryID":"31"}, ' \
           '{"ProjectSkillID":"99", "ProjectID":"42", "SkillID":"30", "LevelMin":"3", "LevelMax":"3", "CategoryID":"31"}, ' \
           '{"ProjectSkillID":"99", "ProjectID":"42", "SkillID":"40", "LevelMin":"3", "LevelMax":"3", "CategoryID":"31"}, ' \
           '{"ProjectSkillID":"99", "ProjectID":"43", "SkillID":"30", "LevelMin":"3", "LevelMax":"3", "CategoryID":"31"}, ' \
           '{"ProjectSkillID":"99", "ProjectID":"43", "SkillID":"40", "LevelMin":"2", "LevelMax":"3", "CategoryID":"31"}]'