import pulp
from Courses import courses as courseData
from Rooms import rooms as roomData
from Cleaner import processCourses

# Original Data
courses = [
    "AID101", "AID304", "ARCH100", "ARCH101", "ARCH102", "ARCH106", "ARCH107", "ARCH108.1", "ARCH108.2", "ARCH109",
    "ARCH110", "ARCH201", "ARCH202.1", "ARCH202.2", "ARCH208.1", "ARCH208.2", "ARCH209", "ARCH210", "ARCH211", "ARCH303",
    "ARCH304", "ARCH307", "ARCH308", "ARCH311", "ARCH358", "ARCH360", "ARCH403", "ARCH405", "ARCH412", "ARCH414",
    "ARCH510", "ARCH569", "ARCH570", "BIO305", "BIO306", "BIO312", "BIO404", "BIO407", "BIO424", "BIO513", "BIO514",
    "BIO518", "BIO604", "BIO646", "BOS111.1", "BOS111.2", "BOS112.1", "BOS112.2", "BOS112.3", "BUS602", "CS103.1",
    "CS103.2", "CS105.1", "CS105.2", "CS207.1.1", "CS207.1.2", "CS303", "CS304", "CS306", "CS308", "CS310", "CS314",
    "CS404", "CS413", "CS417", "CS427", "CS509", "CS511", "CS600", "CULT101.1", "CULT101.2", "ECON108", "ECON112.1",
    "ECON112.2", "ECON202.1", "ECON202.2", "ECON204", "ECON221.1", "ECON221.2", "ECON311", "ECON320", "ECON404",
    "ECON430", "ECON506", "EDU102", "EDU103", "EDU323", "EDU583", "EE301", "EE305", "EE321", "EE325", "EE422", "EE429",
    "EE603", "ELIT100.1", "ELIT100.2", "ELIT100.3", "ELIT100.4", "ELIT100.5", "ELIT100.6", "ELIT103.1", "ELIT103.2",
    "ELIT200.1", "ELIT200.2", "ELIT200.3", "ELIT200.4", "ELIT200.5", "ELIT200.6", "ELIT200.7", "ELIT200.8", "ELIT200.9",
    "ELIT200.10", "ELIT200.11", "ELIT200.12", "ELIT200.13", "ELIT200.14", "ELIT201", "ELIT203", "ELIT208", "ELIT401",
    "ELIT406", "ELIT413", "ELIT415", "ELT105", "ELT212", "ELT322", "ELT323", "ELT562", "ELT565", "ELT660", "ELT670",
    "ENS201", "ENS203", "ENS204", "ENS206", "ENS207", "ENS209", "ENS211", "ENS309", "IBF105", "IBF205.1", "IBF205.2",
    "IBF208.1", "IBF208.2", "IBF310", "IBF401", "IBF407", "IBF409", "IBF410", "IBF507", "IBF562", "IE303", "IE305",
    "IE307", "IE425", "IE502", "IR100", "IR101", "IR212", "IR213", "IR214", "IR216", "IR304", "IR305", "IR467", "IR472",
    "IR478", "IR520", "IR651", "IR652", "ITA101", "ITA102", "LAW104", "LAW106", "LAW118", "LAW120", "LAW202", "LAW204",
    "LAW206", "LAW210", "LAW218", "LAW242", "LAW302", "LAW310", "LAW316", "LAW333", "LAW402", "LAW406", "LAW408",
    "LAW416", "LAW443", "LAW530", "MAC102", "MAN102", "MAN105", "MAN302", "MAN303", "MAN304", "MAN328", "MAN332",
    "MAN352", "MAN402", "MAN406", "MAN443", "MAN453", "MATH100.1", "MATH100.2", "MATH101.1", "MATH101.2.1", "MATH101.2.2",
    "MATH102.1.1", "MATH102.1.2", "MATH201.1.1", "MATH201.1.2", "MATH201.2.1", "MATH201.2.2", "MATH201", "MATH205",
    "MATH207", "MATH209.1", "MATH209.2", "MATH306", "MBA525", "MBA535", "MBA581", "ME206", "ME211", "ME304", "ME411",
    "ME413", "ME510", "ME580", "ME605", "NS103", "NS112", "NS122", "NS207", "NS209", "POLS101", "POLS211", "POLS302",
    "POLS304", "PSY103.1", "PSY103.2", "PSY105", "PSY303", "PSY308", "PSY310", "PSY311", "PSY312", "PSY329", "PSY336",
    "PSY402", "PSY406", "PSY412", "PSY414", "PSY424", "PSY457", "PSY458", "PSY490", "PSY496", "PSY519", "PSY524",
    "PSY529", "SE211", "SE308.1", "SE308.2", "SE407", "SOC102", "SOC311", "SOC503", "SPS312", "SPS509", "SPS603", "TLT114",
    "TLT212", "TLT214", "TLT312", "TLT317", "TLT319", "TLT411", "TLT427", "TT304", "TURK111.1", "TURK111.2", "TURK112.1",
    "TURK112.2", "TURK112.3", "TURK112.5", "TURK112.6", "TURK112.7", "TURK112.8", "TURK112.9", "VA104.1",
    "VA104.2", "VA211.1", "VA211.2", "VA217.1", "VA217.2", "VA217.3", "VA304", "VA306.1", "VA306.2", "VA310", "VA312.1",
    "VA312.2", "VA314", "VA323.1", "VA323.2", "VA324", "VA334", "VA341", "VA406", "VA416", "VA443", "VA455", "VA502",
    "VA517", "VA519"
]

rooms = [
    "AF1.3", "AF1.4", "AF1.10", "AF1.11", "AF1.17", "AF1.18", "AF1.22", "AF1.23",
    "AF1.25", "AF1.26", "AF2.3", "AF2.13", "AF2.14", "AF2.15", "BF1.1", "BF1.2",
    "BF1.8", "BF1.9", "BF1.10", "BF1.16", "BF1.17", "BF1.22", "BF1.23", "BF1.24",
    "BF1.25", "BF1.38", "BF2.1", "BF2.2", "BF2.4", "BF2.5", "BF2.6", "BF2.8",
    "BF2.14", "BF2.15", "BF2.16", "BF2.17",

    # Arch Rooms
    "AF2.16", "AF2.8", "AF3.7", "AF3.8", "AF3.10"
]

archRooms = ["AF2.16", "AF2.8", "AF3.7", "AF3.8", "AF3.10"]

processCourses(courseData)

# Return true if 2 courses overlap
def hasOverlap(course1, course2):
    return course1["Start"] <= course2["End"] and course2["Start"] <= course1["End"]

model = pulp.LpProblem("CourseScheduling", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("Assignment", (courses, rooms), cat='Binary')

# Objective Function
# Goal is to minimize the amount of unused seats for each course
# model += pulp.lpSum(x[course][room] * (roomData[room] - courseData[course]["Seats"]) for course in courses for room in rooms)

# Every course must be assigned to at most 1 room
for course in courses:
    if course.__contains__("ARCH"):
        model += pulp.lpSum(x[course][room] for room in archRooms) == 1
    else:
        model += pulp.lpSum(x[course][room] for room in rooms) == 1

# Required seats for course must be <= roomCapacity
for course in courses:
    requiredSeats = courseData[course]["Seats"]
    if course.__contains__("ARCH"):
        maxCapacity = max(roomData[room] for room in archRooms)
        if requiredSeats > maxCapacity:
            print(course)
        for room in archRooms:
            roomCapacity = roomData[room]
            model += (x[course][room] * requiredSeats <= roomCapacity)
    else:
        for room in rooms:
            if room in archRooms:
                continue
            maxCapacity = max(roomData[room] for room in rooms)
            if requiredSeats > maxCapacity:
                print(course)
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
print("Status:", pulp.LpStatus[model.status])

assignedCoursesFile = open("assigned.txt", 'w')
unassignedCoursesFile = open("missed.txt", 'w')

# Save data in file so it can be read out
for course in courses:
    isAssigned = False
    for room in rooms:
        if pulp.value(x[course][room]) == 1:
            assignedCoursesFile.write(f"Course {course} assigned to {room}\n")
            isAssigned = True
    if not isAssigned:
        unassignedCoursesFile.write(f"Course {course} was not assigned to any room\n")

assignedCoursesFile.close()
unassignedCoursesFile.close()

