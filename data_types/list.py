courses = ["Math", "Physics", "Chemistry", "English"]

courses.append("Biology")
courses.insert(2, "Computer Science")
courses.remove("English")

print("First course:", courses[0])
print("All courses:", courses)

print("\nCourses offered:")
for course in courses:
    print("-", course)

print("\nFirst two courses:", courses[:2])

if "Physics" in courses:
    print("\nPhysics course is available!")