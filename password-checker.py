import string
import basic_check
import zxcvbn_imple

password = input("Enter the password: ")
print(basic_check.feedback(password))
zxcvbn_imple.zxcvbn_check(password)
