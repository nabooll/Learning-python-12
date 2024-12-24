# Input the information
students_score = [80, 90, 95, 78, 89, 67, 59] # We can change the input based on your need too!
highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The Highest Score is {highest_score}")
