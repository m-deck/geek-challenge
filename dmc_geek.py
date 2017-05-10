def prob_imperfect(p, num_games):
    
    return (1.0 - p ** num_games)

def find_closest(dict_solutions, target):
    
    adjusted_dict = {}
    for key in dict_solutions:
        adjusted_dict[key] = abs(dict_solutions[key] - target)
    
    return min(adjusted_dict, key=adjusted_dict.get)

def solve_p(n_list=([63] * 50), target=0.5, test_values=100000):
    
    num_brackets = len(n_list)
    candidates = {}
    
    for i in [float(j) / test_values for j in range(0,test_values,1)]:
        
        temp_val = 1.0

        for b in n_list:
            
            temp_val = temp_val * prob_imperfect(i, b)
        
        candidates[i] = 1.0 - temp_val

    return find_closest(candidates,target)
