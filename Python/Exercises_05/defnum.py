#This block of code is iterating through a list looking for a number

def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
        #Return False instead of none
            return False
    
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)