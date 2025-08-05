stu_dict={'name':'Shreya','class':'MBA','location':'BR' }
# stu_dict['name']='Rekha'
stu_dict['gender']='Female'
print(stu_dict)
stu_dict['address']={'streetName':'Chitrawani Road','city':'Purnea','state':'Bihar','pincode':854300}
stu_dict['address']['pincode']=854301
print(stu_dict)
# del stu_dict['class']
# print(stu_dict.pop('class'))
# print(stu_dict.popitem())
# stu_dict.clear()
print(stu_dict.keys())
print(stu_dict.values())
print(stu_dict.items())

for i in stu_dict.items():
    print(i)

for i in stu_dict['address'].items():
    print(i)

dict2=stu_dict.copy()
print(dict2)
print(len(dict2))

stu_dict['address']['zipCode']='A35X23'
print(stu_dict['address'])
# del stu_dict['address']['zipCode']
# stu_dict['address'].pop('zipCode')
# stu_dict['address'].popitem()

print(stu_dict)