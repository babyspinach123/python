people = ['thomas','katie','jon','alison']
for name in people:
    print(name)

index = 0
# while index <= len(people):     this is wrong (no =)
while index < len(people):
    print(people[index])
    index = index + 1 