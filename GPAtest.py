# Seneiya Cooke
# GPAtest.py
# take in student names and GPAs then test if the student qualifies for the deans list or the honor roll. It stops processing when a last name of 'ZZZ' is entered.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit)")
    if last_name == 'ZZZ' or last_name == 'zzz':
        break
    first_name = input("Enter the student's first name")
    gpa = float(input("Enter the student's GPA"))
    
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll.")
    else:
        print(first_name + " " + last_name + " does not qualify for the Dean's List or the Honor Roll.")