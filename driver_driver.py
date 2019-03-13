from driver import driver_function

x = 0;
i = 100;

while x < 60:
    output_name = "E:\\CS300\\CS350_project\\output\\n_"+str(i)
    print("n = ", str(i))
    x = driver_function(output_name, i, 20)
    if i == 100:
        i = 500
    elif i == 500:
        i = 1000
    elif i == 1000:
        i = 2000
    elif i == 2000:
        i = 5000
    elif i == 5000:
        i = 10000
