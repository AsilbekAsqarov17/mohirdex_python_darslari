#Asilbek Asqarov
#Mohirdev python-darslari
#dars-25
#Son topish o'yini
import random 

def find_num_pc():
    print("1 dan 10 gacha son o'yladim.Topishga harakat qiling")
    son = random.randint(1, 10)
    times_me = 1
    while True:
        guess = int(input("Taxmin: "))
        if son == guess:
            print(f"Siz topdingiz!, urinshlar: {times_me}")
            return times_me
        elif son >guess:
            print(f"O'ylangan son {guess} dan katta")
            times_me+=1
        else:
            print(f"Oylangan son {guess} dan kichik")
            times_me+=1
            

def find_num_mynum():
    times_pc = 1
    print("1 dan 10 gacha son o'ylang. Mentopishga harakat qilaman!")
    son = random.randint(1, 10)
    times_pc = 1
    a, b = 1,10
    while True:
        javob = input((f"Siz {son}sonini o'yladingiz! To'g'ri (T),men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)? "))
        if javob == 't' or javob =='T':
            print(f"Soningizni {times_pc}ta taxmin bilan topdim!")
            return times_pc
        elif javob == '+':
            a= son+1
        elif javob == '-':
            b = son - 1
        
        if a<b:
            son = random.randint(a, b)
            times_pc+=1
        elif a==b:
            son = a
            times_pc+=1
        else:
            print("Bunday bo'lishi mumkin emas!")
            break
            
def me_vs_programm():
    print("Keling o'ylangan sonni topish o'yanymiz!")
    while True:
        times_me = find_num_pc()
        times_pc = find_num_mynum()
        if times_me < times_pc:
            print("Siz yudingiz!")
        elif times_pc <times_me:
            print("Men yutdim!")
        elif times_me == times_pc:
            print("Durrang!")
        
        savol = input("Yana o'ynaymizmi: ha(1) / yo'q(0): ")
        if savol != '1':
            print("O'yin tugadi")
            break

me_vs_programm()
        
    
    
    
    
    
            
        