import string

def check_common_password(password):
    with open ('10_million_password_list_top_1000000.txt', 'r') as f:
        common = f.read().splitlines()
    if password in common:
        return True
    return False

def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digits]

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    score +=sum(characters)
    if score < 5:
        return "Weak", score
    elif score == 5:
        return "Okay", score
    else:
        return "Strong", score
    

def feedback(password):
    if check_common_password(password):
        return "This password is commonly used by other users!"
    strength, score = password_strength(password)
    feedback = f"Password strength: {strength} (Score: {score}/6)\n"
    if score < 4:
        feedback += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback += "- Make your password longer (more than 8 characters). \n"
        if not any(c.isupper() for c in password):
            feedback += "- Include uppercase letters.\n"
        if not any(c.islower() for c in password):
            feedback += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Add numbers.\n"
    return feedback

