# Define a function that accepts a percentage as an argument and returns a letter grade (A+, A, A-, B+, etc) for that percentage.

# Prompt your user to enter a percentage and display a message showing them the equivalent letter grade.

def grade_cal():
    print("This is your grade in %")
    percent_outcome = input()
    if int(percent_outcome) >= 99:
        return 'A+'
    elif int(percent_outcome) >= 89:
        return 'A'
    elif int(percent_outcome) >= 85:
        return 'A-'
    elif int(percent_outcome) >= 79:
        return 'B+'
    elif int(percent_outcome) >= 75:
        return 'B'
    elif int(percent_outcome) >= 70:
        return 'B-'
    elif int(percent_outcome) >= 65:
        return 'C+'
    elif int(percent_outcome) >= 63:
        return 'C'
    elif int(percent_outcome) >= 59:
        return 'C-'
    elif int(percent_outcome) >= 55:
        return 'D+'
    elif int(percent_outcome) >= 52:
        return 'D'
    elif int(percent_outcome) >= 50:
        return 'D-'
    else:
        return 'F'
print("The grade is: {}.".format(grade_cal()))
            