user_prompt = input('Add a new member: ')
with open('../files/members.txt', 'a') as file:
    file.write(user_prompt)
    file.close()

   