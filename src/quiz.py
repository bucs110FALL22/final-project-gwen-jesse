from riddles import riddles 
    
def check_ans(question, answer, attempts, score):
    if {attempts} == 0:
      return False 
    if  riddles[question]['answer'] == answer:
        print(f"Correct Answer! Your score is {score + 1}")
        return True
    else:
        print(f"Wrong, You have {attempts - 1} left \nTry again")
        return False
 

def print_dictionary():
    for riddles_id, question_answer in riddles.items():
        for key in question_answer:
            print(key + ':', question_answer[key])


while True:
    score = 0
    for question in riddles:
        attempts = 4
        while attempts > 0:
            print(riddles[question]['question'])
            answer = input("Enter Answer: ")
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1 
            
           
          
            


