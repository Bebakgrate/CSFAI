first_list=[0,1,2,3,4,5,6,7,8,9]
inverse_list=[]
index=9
while index >=0:
    inverse_list.append(first_list.pop(index))
    index-=1
##print(first_list)
#print(inverse_list)
def reverse_array(first_list):
    inverse_list=[]
    index=len(first_list)-1

    while index>=0:
        inverse_list.append(first_list.pop(index))
        index-=1
    return inverse_list
first_list=[0,1,2,3,4,5,6,7,8,9]
#print(result)

def squarefunction(firstnumber:int)->int:
    square=firstnumber**firstnumber
    return square
firstnumber=6
#print(squarefunction(firstnumber))

## sets and tuples
