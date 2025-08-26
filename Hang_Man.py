import random

word_list=['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop']

#selecting a random word
word=random.choice(word_list)
print(f"word={word}")
lives=len(word)-1
print(f"lives={lives}")

temp_ans=""


while lives!=0:

    ans=input("Enter a character that you think is in the target word:\n")
    
    
    for w in word:
        
    
        if ans==w:
            temp_ans+=w
            break
        else:
            temp_ans+="_"
            break
        
    
        
    print(f"{temp_ans}           you have {lives} lives left")
    
            

