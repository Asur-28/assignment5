# 5 . task 1 :


marks = {
    "Yash": 85,
    "Vasu": 78,
    "Sameer": 92,
    "Mohit": 88
}

name = input("Enter the student's name: ")

if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")



# 5. task 2:


numbers = list(range(1, 11))
print("Original list:", numbers)

first_five = numbers[:5]
print("Extracted first five elements:", first_five)


reversed_list = first_five[::-1]
print("Reversed extracted elements:", reversed_list)
