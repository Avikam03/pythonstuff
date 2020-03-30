#question1
'''
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
'''

def duplicate_count(text):
    # Your code goes here
    list=[]
    text2 = text.lower()
    for i in text2:
        if i in list:
            break
        count=0
        for j in range(0,len(text2)):
            if i==text2[j]:
                count+=1
            if count >=2:
                list.append(i)
                break
    return len(list)
                
duplicate_count("avikammangla") 
     
