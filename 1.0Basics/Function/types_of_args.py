def data(name,age=25):
    print(f"{name} is {age} years old")

data('Sunanda',24);                 #Positional Args
data(age=24,name="sunanda")         #Keyword Args
data("Sunanda")                     #default Args

#Variable length Args
#arbitary positional args
def add(a,*args):
    print(f"{a}\t{sum(args)}")

add(10,1,2,3,4,5)

#arbitary keyword args
def bio_data(**kwargs):
    for key,pair in kwargs.items():
        print(f"{key}\t{pair}")

bio_data(name="Sunanda", title="sadhu",age=24)
bio_data(name="Priyanka", title="sadhu",age=18)

#normal args + arbitary positional args + arbitary keyword args
print('\nargs + arbitary positional args + arbitary keyword args\n')
def combined_args(name,*marks,**result):
    sum=0
    for mark in marks:
        sum+=mark
    for key,val in result.items():
        avg=sum/5;
        if(avg<=12):
            r='Fail' 
        elif(avg<=25):
            r='Pass'
        elif(avg<=40):
            r='Good'
        else:
            r='Excellent'
        print(f"{name} scored=> \t {sum}\t{key} \t{avg.__ceil__()}\t{r}")

combined_args('Apple',10,20,30,40,50,Average='')
combined_args('Ball',10,10,10,10,10,Average='')
combined_args('Cat',50,50,40,40,50,Average='')
combined_args('Dog',13,20,13,15,16,Average='')
