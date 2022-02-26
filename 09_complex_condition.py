# a student makes honour roll if their average is >=85
#and their lowest grade is not below 75
gpa = float(input('what is your grade point average? '))
lowest_grade = float(input('what was your lowest grade? '))

if gpa >=85 and lowest_grade >=75:
    honour_roll = True 
else:
    honour_roll = False
    print("you didn't make the honour role")

# Somwhere different in your code
if honour_roll:
    print ('you made the honour roll')
