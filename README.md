# PRASUNET-CS_01-task--03
Password Complexity Checker
Description- Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.


# Criteria 
Weights: Each criterion (length, case, number, special characters) has an associated weight to reflect its importance.

Initial Score: The initial score is set to 0, and it increases based on the satisfaction of the criteria.

Length Criteria: Checks if the password is at least 6 characters long.

Case Criteria: Checks if the password contains both uppercase and lowercase letters.

Number Criteria: Checks if the password contains at least one number.

Special Character Criteria: Checks if the password contains at least one special character.

Normalize Score: The score is normalized to a scale of 0-100.

Strength Category: The password's strength is categorized as "Very Strong", "Strong", "Moderate", or "Weak" based on the score.

Feedback: Provides specific feedback to the user about what aspects of their password could be improved.

# Input
Take input from the user that needs to be verified.
