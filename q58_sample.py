# This code simulates a communication scenario involving students and a teacher.
initial_number_of_students = 14
# Set the initial state of the number of people (a, b, c's number + number of calls made by the teacher)
status = [[initial_number_of_students, 0, 0, 0]]
elapsed_time = 0  # Time elapsed

while len([s for s in status if s[1] == initial_number_of_students]) == 0:
    # Repeat until all students who do not need contact (b) are accounted for
    next_status = []
    
    for s in status:
        for b in range(s[1] + 1):
            # Number of students who do not need contact contacting other students
            for c in range(s[2] + 1):
                # Number of students who need contact contacting others
                if s[2] > 0:  # If there are students able to make calls
                    # Student to teacher contact
                    if s[0] - b - c + 1 >= 0:
                        next_status.append([s[0] - b - c + 1, s[1] + c, s[2] + b - 1, s[3] + 1])
                
                # Teacher not present
                if s[0] - b - c >= 0:
                    next_status.append([s[0] - b - c, s[1] + c, s[2] + b, s[3]])
                
                # Teacher to student contact
                if s[0] - b - c - 1 >= 0:
                    next_status.append([s[0] - b - c - 1, s[1] + c + 1, s[2] + b, s[3] + 1])
    
    status = list(set(map(tuple, next_status)) - set(map(tuple, status)))
    elapsed_time += 1

# Display the elapsed time
print(elapsed_time)
# Among the shortest, display the one with the minimum number of calls made by the teacher
print(min([s for s in status if s[1] == initial_number_of_students], key=lambda x: x[3]))
