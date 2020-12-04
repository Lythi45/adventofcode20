passports=[]
passport=[]
for line in open("input04.txt",'r').readlines():
    if line=='\n':
        passports.append(passport)
        passport=[]
    else:
        passport+=line.split()
passports.append(passport)
necc_fields=['byr','iyr', 'eyr','hgt', 'hcl', 'ecl', 'pid']
num_valid=0
for pp in passports:
    ppf={}
    for ppparts in pp:
        pps=ppparts.split(':')
        ppf[pps[0]]=pps[1]
    invalid=False
    for np in necc_fields:
        if np not in ppf:
            invalid=True
    if not invalid:
        num_valid+=1
print(num_valid)