# CTI-110

   # P3HW2 - Salary

   # Andrew Johnson

   # 3/19/2023










#employee name
name = input("Enter employee's name: ")
#number of hours
hours = float(input("Enter number of hours worked: "))
#pay rate
payrate = float(input("Enter employee's pay rate: "))
#overtime_pay
overtime_pay = 0
#overtime_hours
overtime_hours = 0
#regular pay
reg_pay = 0
#Overtime Total
overtime_total = 0

if hours > 40:
        overtime_hours = (( hours - 40))
        overtime_pay = payrate + (payrate / 2)
        overtime_total =  overtime_pay * overtime_hours
        hours -= overtime_hours
 # Regular Pay Updated   
reg_pay = hours * payrate
#Gross Pay
gross = reg_pay + overtime_total





print("---------------------------------------")

print(f"Employee Name: {name} ")
print(f"Hours Worked: {hours}")
print(f"Pay Rate:$ {payrate}")
print(f"Overtime: {overtime_hours}")
print(f"Overtime Pay:$ {overtime_total}")
print(f"Regular Pay:$ {reg_pay}")
print(f"Gross Pay:$ {gross}")
