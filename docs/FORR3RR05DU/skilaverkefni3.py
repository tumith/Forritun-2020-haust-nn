"""
1. Útskýrðu stuttlega tímaflækjurnar hér fyrir neðan.  Nefndu dæmi um reiknirit sem hafa eftirfarandi tímaflækjur.
    a. big O er notað í Classify algorithms samkvæmt hvernig keyrslu tímin er og geymslu kröfur stækar eins og input stærð stækar
    b. Margfalda 2 n-digit númer af einföldu algorithma; svona algortihma eins og bubble sort, selection sort og insertion sort; mörk á eitthverju á sumum venjulegri sorting algorithms eins og quicksort, Shellsort og tree sort
    c. keyrslu tímin stækar í hlutfalli við n

"""

#2
  
def bubble_sort(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                bubble_sort(listt) 
        except IndexError: 
            pass
    return listt 
  #1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 20 21 22 23 25 26 27 28 29 30
listt = [10, 5, 2, 4, 1, 3, 6, 9, 8 , 7, 20, 12, 14, 15, 13, 16, 18, 19, 17, 30, 25, 21, 23, 26, 22, 27, 29, 28, 24] 
bubble_sort(listt) 
  
print("Sorted array:"); 
for i in range(0, len(listt)): 
    print(listt[i], end=' ') 


#endur taka til að læra betur
def bubble_sorta(list1)
for e, tal in enumerate(list1):
    try:
        if list1[e+1] < tal:
            list1[e] = list1[e+1]
            list1[e+1] = tal
            bubble_sorta(list1)
        except IndexError:
            pass
    return list1

list1 = [10, 5, 2, 4, 1, 3, 6, 9, 8 , 7, 20, 12, 14, 15, 13, 16, 18, 19, 17, 30, 25, 21, 23, 26, 22, 27, 29, 28, 24] 
bubble_sort(list1)

print("Sorted array: ")
for e in range(0, len(list1)):
    print(list1[e], end=' ')