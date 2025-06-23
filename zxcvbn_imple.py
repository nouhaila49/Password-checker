from zxcvbn import zxcvbn

def zxcvbn_check(password ):        

    result = zxcvbn(password)

    print("Password Strength Score:", result['score'])

    print("Feedback:", result['feedback'])
    print("Entropy:", result['entropy'])
