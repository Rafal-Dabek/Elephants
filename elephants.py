import enum
import math
import numbers
import sys

NUM_OF_LINES_IN_FILE = 4 #number of lines in file


def prepare_data_elephants(): #data preparation for further calculations 
    """Prepare data from input and permutation 

    Returns:
        dictionary: prepared data:  number and weights starting positions, destination and permutation postion of elephants 
    """
    data_elephants = {           
                        "number":    int(input()),                              # read 1st line and convert to int, number of elephants 
                        "weights":   [int(num)    for num in input().split()],  #read 2nd line, put that to list split line by spaces, convert splited parts to int 
                        "start_pos": [int(num) -1 for num in input().split()],  #read 3rd line, put that to list split line by spaces, convert splited parts to int - 1
                        "end_pos":   [int(num) -1 for num in input().split()],  #read 4th line, put that to list split line by spaces, convert splited parts to int - 1
                        "perm_pos":  [] #prepare for permutation 
                     }
    
    data_elephants['perm_pos'] = [-1] * (data_elephants['number']) #fill array with number - 1 
    
    for i in range(0, data_elephants['number']): #starting from 0 because we decreased count by one, in lines 13-14
        data_elephants['perm_pos'][data_elephants['end_pos'][i]] = data_elephants['start_pos'][i] #permutation 

    return data_elephants

def calculate_cost(elephants):
    """Calculate the optimal cost of moving all the elephants 

    Args:
        elephants (dictionary): description

    Returns:
        int: calculated cost
    """
    is_in_right_place = [False] * (elephants['number'])     # fill table with false 
    total_min_weight = min(elephants['weights'])            #find min weight of all elephants 

    result = 0                              #starting from 0 
    for i in range(elephants['number']):    #iterate up to number of elephants 
        if (not is_in_right_place[i]):      #check if elephant is in correct position 
            sum_weight_in_cycle = 0         #sum weights of current cycle
            current = i                     #current elephant 
            min_in_cycle = math.inf         #settig infinite value of weight for cycle 
            lenght_of_cycle = 0             #current lenght of cycle to calculate result

            while True:
                min_in_cycle = min(min_in_cycle, elephants['weights'][current])     #current minimal weight in cycle  
                sum_weight_in_cycle += elephants['weights'][current]                #sum current weights in cycle
                current = elephants['perm_pos'][current]                            #setting as current end position of elephant 
                is_in_right_place[current] = True                                       
                lenght_of_cycle += 1

                if current == i:
                    break
            result +=  min(sum_weight_in_cycle + (lenght_of_cycle - 2) * min_in_cycle, sum_weight_in_cycle + min_in_cycle + (lenght_of_cycle + 1) * total_min_weight )
    return result   

if __name__ == "__main__":
    
    data_elephants = prepare_data_elephants()
    replacement_cost = calculate_cost(data_elephants)
    
    print(f"Calculated result: {replacement_cost}")