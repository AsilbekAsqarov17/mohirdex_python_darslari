#Asilbek Asqarov
#Mohirdev python-darslari
#dars-36

#task1
def max_num(a, b, c):
    result = a  # Faraz qilamiz, birinchi son eng katta
    
    if b > result:
        result = b
    if c > result:
        result = c
        
    return result    

#task2
def uppercase_latter(word_list):
    index = 0
    for i in word_list:
        word_list[index] = i.capitalize()
        index +=1
    return word_list
      
#task3
def get_evens(num_list):
    even_nums = []
    for i in num_list:
        if i % 2 ==0:
            even_nums.append(i)
    return even_nums


#task4
def is_num_fib(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num
