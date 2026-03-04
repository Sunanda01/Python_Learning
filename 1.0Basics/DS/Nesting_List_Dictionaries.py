#Nested List In Dictionary
fruit_list=['Apple','Mango','Guava','Orange','Grapes']
fruit_dict={'category':'fruits','origin':'India','fruits':fruit_list}
print(fruit_dict)

##Nested Dictionary In List
fruit_dict1={'category':'fruits','origin':'India'}
fruit_list1=['Apple','Mango','Guava','Orange','Grapes',fruit_dict1]
vegetable_dict={'category':'fruits','origin':'India'}
fruit_list1.append(vegetable_dict)
print(fruit_list1)