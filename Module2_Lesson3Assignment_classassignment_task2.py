# Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the #names of students who attended the last class.
#Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted #and attended in one if statement?
# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice attended class and submitted the assignment.")
else:
    print("Alice did not attended class and did not submitted the assignment.")