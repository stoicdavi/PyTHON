#using for loop, concatination and extend
#add two names to the list and print invitation message to all the names
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'
#names += names1
names.extend(names1)
for index in range(2):
    names.append(input("Enter a name: "))
for name in names:
    massage = f'{name}! {msg}'
    print(massage)
