import sys

a = sys.stdin.readline().rstrip()

dict = {}

dict['A+']=4.3
dict['A0']=4.0
dict['A-']=3.7
dict['B+']=3.3
dict['B0']=3.0
dict['B-']=2.7
dict['C+']=2.3
dict['C0']=2.0
dict['C-']=1.7
dict['D+']=1.3
dict['D0']=1.0
dict['D-']=0.7
dict['F']=0.0

if a in dict:
    print(dict[a])
