# 1. Python List Transformation
# Objective: The aim of this assignment is to practice list operations and transformations.
# Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.

# # Task 1: Given the list of grades. Sort the grades in descending order and print the sorted list.

# Task 2: Calculate the average grade and print it.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

total = sum(grades)
number = len(grades)
average = total / number
print("Average:", average)
