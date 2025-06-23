from zxcvbn import zxcvbn

# Analyze a password
password = input("your password : ")
result = zxcvbn(password)

# Display the score (0 to 4, where 4 is the strongest)
print("Password Strength Score:", result['score'])

# Display feedback
print("Feedback:", result['feedback'])
