# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# November, 2022

# -------------------------- Task 1 ------------------------------

def read_student_records(file_name):
    
    # ------- creating an object of DrakeCourse class ---------
    drake_course = Drakecourse("CS65", 3.00, [])
    
    # ----------- read from text file ---------------
    file_handler = open(file_name, 'r')
    
    all_lines = file_handler.readlines()   # readlines method reads all lines as a list of strings
    
    print('Reading the following:')
    print(all_lines[0:6])
    print('Reading each line using for loop:')
    for each_line in all_lines:
        
        print(each_line)
    
    for all_lines in range(0,len(all_lines),6):
        
        print(all_lines)
    
    #i+5
        
        #first_name = drakecourse([1])
       # last_name  = drakeCourse([2])
      #  std_major  = drakeCourse([3])
      #  std_serial = zzzzzz([5])
      #  scores_str = drakeCourse([6])
        
        
        
    file_handler.close()
    
file_name = 'student_scores.txt'
    
read_student_records(file_name)