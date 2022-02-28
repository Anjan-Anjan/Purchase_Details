#TM06: purchase

try:
    dic=dict()
    li=list()
    x=input('Enter the file name: ')
    f=open(x+'.txt')

    pitem=0
    fitem=0
    pay=0
    li=f.read().replace('\n',' ').split(' ')
    dic = {li[i]:li[i+1] for i in range(0, len(li), 2)}         
    for i in dic:
        if dic[i]=='free':
            fitem+=1
        else:
            price=dic[i]
            pay+=int(price)
            pitem+=1
        if i=='discount':
            pay=pay-int(dic['discount'])
            pitem-=1
        
    print('No of items purchased:',pitem)
    print('No of free items:',fitem)
    print('Amount to pay;',pay)
    print('Discount given:',dic['discount'])
    print('Final amount paid:',(pay-int(dic['discount'])))
    f.close()
except FileNotFoundError:
    print('File does not exist!')
