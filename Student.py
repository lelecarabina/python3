#Filename Student.java
#Written by Lele B.
#Written on Jul 14th, 2017
#Class #12299 - Lesson 10
#Re-written on 5/15/2019

class Student: 

    global name
    global id
    global gpa

    # constructor
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa
        
    
    #get name value to main()
    def getName(self):
        return self.name
        
        
    #get ID value to main()
    def getId(self):
        return self.id
        
 
    #get GPA value to main()
    def getGpa(self):
        return self.gpa
            
