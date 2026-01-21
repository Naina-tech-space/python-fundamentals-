marks = (85, 90, 78, 92, 88)

print("First subject marks:", marks[0])
print("How many times 90 appeared:", marks.count(90))
print("Index of 92:", marks.index(92))

print("\nAll marks:")
for mark in marks:
    print(mark)

extra_marks = (95, 89)
combined_marks = marks + extra_marks
print("\nCombined marks:", combined_marks)

math, physics, chemistry, english, biology = marks
print("\nUnpacked marks - Math:", math, "Physics:", physics)