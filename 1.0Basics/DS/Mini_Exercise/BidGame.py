import os
def findWinner(dict1):
    winner=''
    maximum=0   
    for name,val in dict1.items():
        if(maximum<val):
            winner=name
            maximum=val
    return (winner,maximum)
    
        
bid_detail_dic={}
flag=True
while(flag):
    name=input("What is your name?\t")
    bid_amt=int(input("What is your bid?\t"))
    bid_detail_dic[name]=bid_amt
    check_next=input("Are there any other bidders? Type 'yes' or 'no'\t")
    if(check_next=='yes' or check_next=='y'):
        flag=True
        os.system('cls')
    elif(check_next=='no' or check_next=='n'):
        flag=False
        winner=findWinner(bid_detail_dic)
        print(bid_detail_dic)
        print(f"Winner is {winner[0]} with {winner[1]} bid !!!!!!!!!")
    else:
        flag=False
