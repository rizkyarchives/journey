import data_manager

sheet = data_manager.DataManager()

print("Welcome to Rizky's Flight Club.\nWe find the best flight deals and email you.")
first_name = input('What is your first name?\n').capitalize()
last_name = input('What is your last name?\n').capitalize()
inputting_email = True
while inputting_email:
    email1 = input('What is your email?\n')
    email2 = input('Confirm your email again!\n')
    if email1 == email2:
        inputting_email = False
    else:
        print("Email not confirmed! Retrying...")

sheet.post_customer_data(first_name=first_name, last_name=last_name, email=email2)
print("Finished, You're in the club!")



