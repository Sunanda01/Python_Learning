'''
Pattern 3
* * * * * 
* * * *
* * *
* *
*
'''
# for i in range (1,6):
#     for j in range(i,6):
#         print('*',end=" ")
#     print('\n')

for i in range (5,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()