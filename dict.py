students = {
    "Naina": {"Math": 85, "Physics": 90, "Chemistry": 78},
    "Riya": {"Math": 92, "Physics": 88, "Chemistry": 95},
    "Aarav": {"Math": 79, "Physics": 85, "Chemistry": 80}
}

print("Naina's Physics marks:", students["Naina"]["Physics"])

students["Kabir"] = {"Math": 88, "Physics": 90, "Chemistry": 85}
students["Riya"]["Math"] = 95

print("\nStudent Scores:")
for student, scores in students.items():
    print(f"\n{student}'s Scores:")
    for subject, score in scores.items():
        print(f"{subject}: {score}")

if "Aarav" in students:
    print("\nAarav's record found!")

print("\nAll students:", list(students.keys()))