#Asilbek Asqarov
#Mohirdev python-darslari 
#dars-8

#task1
davlatlar = ["O'zbekiston", "Turkiya","Rassiya", "Eron", "Singapur"]
print(len(davlatlar))
print("Sorted:",sorted(davlatlar))
print("Reverse Sorted: ", sorted(davlatlar, reverse=True))
print("Original list: ",davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.reverse()
davlatlar.sort()
print("Sorted: ",davlatlar)
davlatlar.sort(reverse=True)
print("Reverse Sorted: ",davlatlar)

#task2
juft_sonlar = list(range(120, 1200, 2))
print("Juft Sonlar: ",juft_sonlar)
print("Sonlar yig'indisi: ",sum(juft_sonlar))
print("Max: ", max(juft_sonlar))
print("Min: ", min(juft_sonlar))
print("Difference: ", max(juft_sonlar) - min(juft_sonlar))
print("Numbers of elements: ",len(juft_sonlar))
print("First 20: ", juft_sonlar[:20])
print("last 20: ", juft_sonlar[-20:])
print("Middle 20: ", juft_sonlar[int(len(juft_sonlar)/2)-10:int(len(juft_sonlar)/2)+10 ])

#task3
taomlar = ["Manti","Osh","Choy","Norin","Non"]
print(taomlar)
nonushta= taomlar[:]
nonushta.remove("Manti")
nonushta.remove("Osh")
nonushta.remove("Norin")
print(nonushta)
nonushta.append("Tuxum")
nonushta.append("Shakar")
print("Nonushta: ",nonushta)
print("Taomlar: ", taomlar)
#nonushta = tuple(nonushta)
#'tuple' object does not support item assignment
nonushta[0] = "qaymoq va non"
print("List type: ",type(nonushta))
nonushta = tuple(nonushta)
print("List type changed to tuple: ", type(nonushta))





