#Filename StudentFinder.java
#Written by Lele Carabina
#Written on Jul 14th, 2017
#Class #12299 - Lesson 10
#Re-written on 5/15/2019

from Student import Student
import random

# "Files" to hold Student's fields 'name' and 'gpa' info
gpas = [2.7, 3.0, 3.3, 3.7, 4.0]
names = ["Albert Einstein",
        "Ada Lovelace",
        "Blaise Pascal",
        "Bruna Louise",
        "Caroline Herschel",
        "Cecilia Payne-Gaposchkin",
        "Dorothy Hodgkin",
        "Douglas Junior",
        "Edwin Powell Hubble",
        "Elizabeth Blackburn",
        "Flossie Wong-Staal",
        "Frieda Robscheit-Robbins",
        "Geraldine Seydoux",
        "Gertrude B. Elion",
        "Ingrid Daubechies",
        "Irma Sanchez",
        "Jacqueline K. Barton",
        "Johannes Kepler",
        "Lene Vestergaard Hau",
        "Lord Kelvin",
        "Maria Mitchell",
        "Max Planck",
        "Nicolaus Copernicus",
        "Niels Bohr",
        "Patricia S. Goldman-Rakic",
        "Patty Jo Watson",
        "Richard Phillips Feynman",
        "Rita Levi-Montalcini",
        "Sarah Boysen",
        "Stephen Hawking",
        "Werner Karl Heisenberg",
        "Wilhelm Conrad Roentgen"]


#Print method
def contactPrint(arr):
    for x in range(len(arr)): 
        print("[{}] Name: {} - ID: {} - GPA: {}".format(x, arr[x].getName(), arr[x].getId(), arr[x].getGpa()))
    # end for loop
# end contactPrint()


def main():
    #vars used in object's initialization loop 
    gpasLen = len(gpas)
    numStudents = len(names)
    rand = int(((random.random() * gpasLen) + gpasLen) % gpasLen) #random number to select gpas from list
    #store students' names starting with searching key
    studentsNames = []
    
    #Create new Student object students
    students = [Student((),(),())] * numStudents
    
    # Initialize List of objects Student students with **CONSTRUCTOR** and Print original object students
    print("All Students:")
    for x in range(numStudents): 
        #'name' from array 'names', 'id' incremental 1101 + x, 'gpa' rand number that wraps around gpas length to restrict vals to only gpas' vals
        students[x] = Student(names[x], 1101 + x, gpas[rand])# constructor
    
    #print students list
    contactPrint(students)
    
    #prompt user for input
    key = input("\nEnter the first letter of student's name: ")
    
    #look for key in students.name list...
    for x in range(len(students)):
        #if key found...
        if students[x].name[0] == key.upper(): 
            #add student record to studentsNames list...
            studentsNames.append(students[x].name)               
    
    #loop through sorted list
    print("Students names starting with '{}'".format(key.upper()))
    for x in range(numStudents): 
        #end loop if no student's names matches key
        if studentsNames == "": 
            print("NOT FOUND")
            break
        # end if statement
        
        #print student records that matched key
        for name in studentsNames:  
            if name == students[x].name:
                print("     Name: {} -> ID: {} -> GPA: {}".format(students[x].name, students[x].id, students[x].gpa))    
            # end if statement            
        # end for each loop            
    # end for loop
    
    #message to user, ending program
    print("Program Ended.")

#call MAIN()
main()
