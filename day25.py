card_key=3469259
door_key=13170438

n=0
sub=1
while sub!=card_key:
    sub=(sub*7)%20201227
    n+=1

v=1
for i in range(n):
    v=(v*door_key)%20201227

print(v)


