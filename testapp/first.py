users={'amazon':'active','twitter':'inactive','google':'active','youtube':'inactive'}
for user,status in users.copy().items():
    if user == 'inactive':
        del users[user]
        print(users)

new_list={}
for user,status in  users.items():
    if status == 'active':
        new_list[user]=status
print(new_list)

