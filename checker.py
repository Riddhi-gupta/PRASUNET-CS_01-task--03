import re


def assess_password_strength(password):

    length_weight = 0.3
    case_weight = 0.2
    number_weight = 0.2
    special_weight = 0.3

    # Initial score
    score = 0
    feedback = []

    # set Length criteria
    if len(password) >= 6:
        score += length_weight
        feedback.append("Good length")
    else:
        feedback.append("Password should be at least 6 characters long")

    # Case criteria
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += case_weight
        feedback.append("Good, It contains both uppercase and lowercase letters")
    else:
        feedback.append("Password should contain both uppercase and lowercase letters")

    # set a Number criteria
    if re.search(r'\d', password):
        score += number_weight
        feedback.append("Great job, It Contains numbers")
    else:
        feedback.append("Password should contain at least one number")

    # add Special character criteria
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += special_weight
        feedback.append("It Contains special characters")
    else:
        feedback.append("Password should contain at least one special character")

    # Normalize score to a 0-100 scale
    strength = int((score / (length_weight + case_weight + number_weight + special_weight)) * 100)

    # Add password strength category
    if strength >= 80:
        strength_category = "Very Strong"
    elif strength >= 60:
        strength_category = "Strong"
    elif strength >= 40:
        strength_category = "Moderate, For safety make password stronger"
    else:
        strength_category = "Weak"

    return {
        "strength": strength,
        "strength_category": strength_category,
        "feedback": feedback
    }


#main
password = input("Enter Password to check your score")
result = assess_password_strength(password)
print(f"Password Strength: {result['strength']}%")
print(f"Strength Category: {result['strength_category']}")
print("Feedback:")
for item in result['feedback']:
    print(f"- {item}")
