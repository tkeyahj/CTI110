# T’Keyah Jefferies
# 11-5-2025
# P4HW1 - Score List with Validation and Grading
# This program asks how many test scores the user wants to enter, validates each
# score (must be 0..100), stores them, drops the lowest score, calculates the
# average of the remaining scores, and reports the letter grade for that average.

'''
PSEUDOCODE (Detailed Algorithm)
--------------------------------
1) Print a short title banner (optional for readability).
2) Prompt the user: "How many scores do you want to enter?" -> num_scores (int)
   - If the user enters a number < 1, keep asking until a valid positive integer is provided.
3) Initialize an empty list called scores.
4) For i from 1 to num_scores (inclusive):
     a) Prompt: "Enter score #i:" -> s (as float or int)
     b) While s is not between 0 and 100 inclusive:
           - Print "INVALID Score entered!!!!"
           - Print "Score should be between 0 and 100"
           - Prompt again for "Enter score #i:" -> s
     c) Append s to scores.
5) After all scores are collected:
     a) Determine lowest = min(scores).
     b) Create a shallow copy modified_scores = scores.copy().
     c) Remove exactly one occurrence of the lowest score from modified_scores.
6) Compute average of modified_scores:
     - If modified_scores is not empty:
           avg = sum(modified_scores) / len(modified_scores)
       Else (edge case if only one score was entered):
           avg = 0.0
7) Determine the letter grade from avg using standard scale:
     - 90–100 => 'A'
     - 80–89.99 => 'B'
     - 70–79.99 => 'C'
     - 60–69.99 => 'D'
     - below 60 => 'F'
     (If modified_scores is empty, set grade = 'N/A')
8) Display a formatted results section showing:
     - The original scores list
     - Lowest score
     - List after dropping the lowest score
     - Average (to two decimal places)
     - Letter grade
9) End.
'''

def get_positive_int(prompt: str) -> int:
    """Prompt until the user provides an integer >= 1."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter a whole number that is 1 or greater.")
        except ValueError:
            print("Please enter a valid whole number (e.g., 3).")

def get_valid_score(prompt: str) -> float:
    """Prompt until the user provides a score between 0 and 100 inclusive."""
    while True:
        try:
            s = float(input(prompt))
            if 0 <= s <= 100:
                return s
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100.\n")
        except ValueError:
            print("\nINVALID input. Please enter a numeric score between 0 and 100.\n")

def letter_grade_from_average(avg: float) -> str:
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=== P4HW1: Score List, Average, and Letter Grade ===\n")

    num_scores = get_positive_int("How many scores do you want to enter? ")
    scores = []

    for i in range(1, num_scores + 1):
        score = get_valid_score(f"Enter score #{i}: ")
        scores.append(score)

    print("\n---------- Results ----------")
    print(f"Scores entered: {scores}")

    lowest = min(scores)
    print(f"Lowest score: {lowest}")

    modified_scores = scores.copy()
    # Remove one occurrence of the lowest score
    modified_scores.remove(lowest)
    print(f"Modified list (lowest removed): {modified_scores}")

    if modified_scores:
        avg = sum(modified_scores) / len(modified_scores)
        print(f"Average of modified list: {avg:.2f}")
        grade = letter_grade_from_average(avg)
        print(f"Letter grade: {grade}")
    else:
        # Edge case: only one score was entered
        print("Average of modified list: N/A (no scores remain after dropping the lowest)")
        print("Letter grade: N/A")

    print("-----------------------------")

if __name__ == '__main__':
    main()
