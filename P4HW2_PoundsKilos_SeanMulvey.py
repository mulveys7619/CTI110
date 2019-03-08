# Converts pounds to kilograms
# 03/04/2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Sean Mulvey
###################################################


print("pounds\tKilograms")
print("------------------")

for pound in range(100,300,10):
    kilo = pound / 2.2046

    print (pound,"\t",format (kilo,".2f"))
