korean = 122
foreign = 11
batch = 20
number = list(range(1, korean+1))+list(range(201, foreign+201))
email = [f'{batch}-{str(n).zfill(3)}@ksa.hs.kr' for n in number]
print('\n'.join(email))
