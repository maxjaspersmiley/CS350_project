from driver import driver_function

for i in range(100, 10000, 100):
    output_name = "E:\\CS300\\CS350_project\\output\\n_"+str(i)
    x = driver_function(output_name, i, 50)
    if(x > 2):
        break
