import random
Words=['сыр','колбаска','пирог','зефир','кот','крыса','мыло','кофе','звезда','бутерброд','кексик','шоколад','кетчуп','горчица']
S_slovo=[]
s=random.randint(0,13)
a=0
i=0
mistakes=0
for q in Words[s]:
    S_slovo.append('-')
    print('-',end='')
print()
print(S_slovo)
while i!='exit':
    i=input('Введите букву')
    a=0 #номер буквы в слове
    b=0 #кол-во букв в слове
    m=0 #кол-во букв осталось
    
    for q in Words[s]:
        if i==q:
            b=b+1
            S_slovo[a]=q
     
        a=a+1
    if b==0:
       print('нет такой буквы')
       mistakes=mistakes+1
    print(S_slovo)
    for z in S_slovo:
        if z=='-':
            m=m+1
   
        
    if mistakes==0:
        print('         ')
        print('         ')
        print('         ')
        print('         ')
        print('         ')
        print('         ')
        print(' =========')
    elif mistakes==1:
        print('        +')
        print('        |')
        print('        |')
        print('        |')
        print('        |')
        print('        |')
        print(' =========')
    elif mistakes==2:
        print('    +---+')
        print('        |')
        print('        |')
        print('        |')
        print('        |')
        print('        |')
        print(' =========')
    elif mistakes==3:
        print('    +---+')
        print('    |   |')
        print('    O   |')
        print('        |')
        print('        |')
        print('        |')
        print(' =========')
    elif mistakes==4:
        print('    +---+')
        print('    |   |')
        print('    O   |')
        print('    |   |')
        print('        |')
        print('        |')
        print(' =========')
    elif mistakes==5:
        print('    +---+')
        print('    |   |')
        print('    O   |')
        print('   /|   |')
        print('        |')
        print('        |')
        print(' =========')
    elif mistakes==6:
        print('    +---+')
        print('    |   |')
        print('    O   |')
        print('   /|\  |')
        print('        |')
        print('        |')
        print(' =========')
    elif mistakes==7:
        print('    +---+')
        print('    |   |')
        print('    O   |')
        print('   /|\  |')
        print('   /    |')
        print('        |')
        print(' =========')
    elif mistakes==8:
        print('    +---+')
        print('    |   |')
        print('    O   |')
        print('   /|\  |')
        print('   / \  |')
        print('        |')
        print(' =========')
    elif mistakes==9:
        print('вы проиграли')
        e=input('хотите сыграть ещё раз?')
    if m==0:
        print('вы выиграли')
        e=input('хотите сыграть ещё раз?')
        if e=='нет':
            i='exit'
        elif e=='да':
            s=random.randint(0,13)
            S_slovo=[]
            for q in Words[s]:
                S_slovo.append('-')
                print('-',end='')
            print()
            print(S_slovo)


















# print(Words[s][0])
# print(Words[s][1])
# print(len(Words[s]))



