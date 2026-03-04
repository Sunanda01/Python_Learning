list1=['😄','😄','😄']
list2=['😄','😄','😄']
list3=['😄','😄','😄']
matrix=[list1,list2,list3]

print(f"{list1}\n{list2}\n{list3}")
flag=True
while flag:
    position=input("Enter the position to mark (11,12,12,21,22,23,31,32,33) =>\t")
    row_pos=int(position[0])
    col_pos=int(position[1])
    if(row_pos>3 or col_pos>3 or row_pos==0 or col_pos==0):
        print("INVALID POSITION!!!!!")
        flag=False
        break;
    row_selected=matrix[row_pos-1]
    row_selected[col_pos-1]='😍'
    print(f"{list1}\n{list2}\n{list3}")