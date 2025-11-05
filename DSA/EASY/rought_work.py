array = [4,1,100,3,1]

# Find if there is a duplicate in the array

def find_duplicates(array):
    hash_map = {}

    # key ? = number
    # Data? = Frequency of Occurance (how many times a value showed up)

    # hash_map[key] = hash_map[key] + 1 
    for num in array:
        if num in hash_map: # if hash_map[num] != 0
            #hash_map.update(num, hash_map.get(num) + 1) 
            return True
        else:
            hash_map.update(num,1)
    
    return False

#  # array = [3,1,2,3,100,2]  
# def remo_dups(arr): 
#     seen = {} 
#     res = [] 
#     for item in arr: 
#         if item not in seen: 
#             seen[item] = True # Mark as seen 
#             res.append(item) 
#             return res 
#     array = [3,1,2,3,100,2] 
        
# def main(): 
#     res = remo_dups(array)
#     print(f'Ori Array : {array}') 
#     print(f'Array with dups : {res}') 

# if __name__ == "__main__": main()


