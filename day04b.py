def every(str,set):
    return True in [c in str for c in set]

def between(num,fro,to):
    return int(num)>=fro and int(num)<=to 

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
rules={
     'byr': lambda v:between(str(v),1920,2002) 
    ,'iyr': lambda v:between(str(v),2010,2020)
    ,'eyr': lambda v:between(str(v),2020,2030)
    ,'hgt': lambda v:v[-2:]=='in' and between(str(v[:-2]),59,76) or 
                     v[-2:]=='cm' and between(str(v[:-2]),150,193)
    ,'hcl': lambda v:len(v)==7 and v[0]=='#' and every(v[1:],"0123456789abcdef")
    ,'ecl': lambda v:v in ['amb','blu','brn','gry','grn','hzl','oth']
    ,'pid': lambda v:len(v)==9 and every(v,'0123456789')
}
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
        else:
            if not rules[np](ppf[np]):
                invalid=True
    if not invalid:
        num_valid+=1
print(num_valid)