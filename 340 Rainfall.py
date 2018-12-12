#Anthony Foretich
#ISAT 340
#Rainfall program 

#Initialize Variables
months = 12

#Get Input
total_years = int(input(' How many years total in this calculation? '))

#Process
for years in range (total_years):
    total_rainfall = 0.0
    print('for this year', years+1)
    for months in range (months):
        rainfall = int(input('How much rain this month?'))
        total_rainfall += rainfall
                       
total_months = total_years*12
average_rainfall = total_rainfall/total_months

#Output                       
print (total_months, total_rainfall, average_rainfall)        

