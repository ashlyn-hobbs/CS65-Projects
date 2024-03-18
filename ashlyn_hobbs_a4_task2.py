# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# December, 2022

# -----------------  Task 2  -----------------------
def make_student_id(major, serial_num, year):
    
    std_id = "%s-%04d-%4d" % (str.format(major), int(serial_num), int(year))
    
    print(std_id)
    
    return std_id

major = input("Enter a string acronym for your major: ")

serial_num = input("Enter an integer number ranging between 0 to 9999: ")

year = input("Enter your incoming year: ")

make_student_id(major, serial_num, year)