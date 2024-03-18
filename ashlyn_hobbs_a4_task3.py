# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# December, 2022

# -------------------------------  Task 3  -----------------------------------
def make_score_dictionary(scores_str):
      
    scores_dict = {}
    
    splitted_string = scores_str.split(", ")
    
    for i in range(0, len(splitted_string), 2):
        
        exam_name = splitted_string[i+0]
        score     = splitted_string[i+1]
        
        scores_dict[exam_name] = float(score)
        
    print(scores_dict)
    
    return scores_dict

scores_str  =  "a1, 9.5, a2, 10, a3, 10, l1, 9.5, l2, 9.5, l3, 10, q1, 8, q2, 9, q3, 10"

make_score_dictionary(scores_str)