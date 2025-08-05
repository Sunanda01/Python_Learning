def no_of_cans(ht,wid,coverage):
    area=ht*wid;
    paint_can=area/coverage;
    print(f"Area is {area} m^2\nNumber of Cans required is {paint_can.__ceil__()}")

coverage=7
h=int(input("Enter the height of wall=> "))
w=int(input("Enter the width of wall=> "))
no_of_cans(h,w,coverage);