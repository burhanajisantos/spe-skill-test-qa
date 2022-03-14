n=int(input('masukkan angka : '))
count=0
i=2
while (count<n):
    faktor=0
    for j in range (1,i+1):
        if i%j==0:
            faktor+=1
    if faktor < 3:
        print(i, end=',')
        count+=1
    i+=1