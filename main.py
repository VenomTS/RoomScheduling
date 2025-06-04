import pulp
from Courses import courses as courseData
from Rooms import rooms as roomData
from Cleaner import processCourses

def readList(source, destination):
    with open(source, 'r') as file:
        for line in file:
            destination.append(line.strip())

courses = []
rooms = []

readList("Data/CourseList.txt", courses)
readList("Data/RoomList.txt", rooms)

processCourses(courseData)

# Return true if 2 courses overlap
def hasOverlap(course1, course2):
    return course1["Start"] <= course2["End"] and course2["Start"] <= course1["End"]

model = pulp.LpProblem("RoomScheduling", pulp.LpMinimize)

# Decision variable
x = pulp.LpVariable.dicts("Assignment", (courses, rooms), cat='Binary')

# Objective function
# Goal is to minimize the amount of unused seats for each course
model += pulp.lpSum(x[course][room] * (roomData[room] - courseData[course]["Seats"]) for course in courses for room in rooms)

# Constraints
# Every course must be assigned to at most 1 room
for course in courses:
    model += pulp.lpSum(x[course][room] for room in rooms) == 1

# Required seats for course must be <= roomCapacity
for course in courses:
    requiredSeats = courseData[course]["Seats"]
    for room in rooms:
        roomCapacity = roomData[room]
        model += (x[course][room] * requiredSeats <= roomCapacity)

# Room cannot be assigned to the 2 courses that overlap
n = len(courses)
for room in rooms:
    for i in range(n):
        course1 = courses[i]
        course1Data = courseData[course1]
        for j in range(i + 1, n):
            course2 = courses[j]
            course2Data = courseData[course2]
            if course1Data["Day"] == course2Data["Day"] and hasOverlap(course1Data, course2Data):
                model += x[course1][room] + x[course2][room] <= 1

# Solve
model.solve()

# Print the model status
print(f"Status: {pulp.LpStatus[model.status]}")

assignedCoursesFile = open("assigned.txt", 'w')
unassignedCoursesFile = open("missed.txt", 'w')
testFile = open("testFile.txt", 'w')

# Save data in file so it can be read out
for course in courses:
    isAssigned = False
    for room in rooms:
        if pulp.value(x[course][room]) == 1:
            assignedCoursesFile.write(f"Course {course} assigned to {room} - {courseData[course]["Seats"]}/{roomData[room]}\n")
            testFile.write(f"{room} {courseData[course]["Day"]} {courseData[course]["Start"]} {courseData[course]["End"]}\n")
            isAssigned = True
    if not isAssigned:
        unassignedCoursesFile.write(f"Course {course} was not assigned to any room\n")

assignedCoursesFile.close()
unassignedCoursesFile.close()

