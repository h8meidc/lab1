step=0
vitrati=80
for i in range(1,11,1):
    step+=50
    step-=vitrati
    vitrati *= 1.02
print("Борг студента за 10 місяців скадає: ", -step)  
