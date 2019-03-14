from driver import driver_function

x = 0;
i = 50;

while x < 300:
    if(i == 400):
        i = 500
    elif(i == 1500):
        i = 2000
    elif(i == 4000):
        i = 5000
    output_name = "E:\\CS300\\CS350_project\\output\\n_"+str(i)
    print("n = ", str(i))
    x = driver_function(output_name, i, 5)
    i *= 2
