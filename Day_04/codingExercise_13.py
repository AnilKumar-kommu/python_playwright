row1=['😃', '😃', '😃']
row2=['😃', '😃', '😃']
row3=['😃', '😃', '😃']
matrix=[row1,row2,row3] # nested list we can call
print(matrix)   #printed like this [['😃', '😃', '😃'], ['😃', '😃', '😃'], ['😃', '😃', '😃']]
print(f"{row1}\n{row2}\n{row3}")
position=input("Enter your location : ")
row_num=int(position[0])
col_num=int(position[1])
row_selection=matrix[row_num-1]
row_selection[col_num-1]='@'
print(f"{row1}\n{row2}\n{row3}")

