import random

word_list=['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop']

#selecting a random word
word=random.choice(word_list)
print(f"word={word}")
lives=6
print(f"lives={lives}")

Actual_ans=[]

while lives!=0:
    ans=input("Enter a character that you think is in the target word:")
    temp_ans=""
    for w in word:

        if ans==w:
            
            temp_ans+=w
            Actual_ans.append(w)
            
            
        elif w in Actual_ans:
            
            temp_ans +=w
        
        else:
            temp_ans+="_"
    if "_" not in temp_ans:
        print("You Win!, The word was :",word)
        break
    if ans not in Actual_ans:
        lives-=1
        if lives==0:
            print("You Lose!, The word was : ",word)
            break

            
    print(f"{temp_ans}           you have {lives} lives left")
        
            

