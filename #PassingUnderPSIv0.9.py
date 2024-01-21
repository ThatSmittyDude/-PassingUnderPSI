#PassingUnderPSIv0.9
#Author: Austin Smith
#Email: ThatSmittyDude@outlook.com
#github.com/ThatSmittyDude
#Unix Timestamp: 1705755553

#Desired Hot PSI
#Using some user input we can predict a cold Tire pressure to grow to a desired hot pressure
#The left and right side have different rates of expansion while heating, so we have to have 2 outputs

#List variables
des_hot_psi = float(input("Desired hot PSI: "))         #user desired hot pressure
hot_temp = float(input("hot Average IMO tire temp: "))  #Average tire temp across IMO, Use data from last run
hot_psi = float(input("Last Hot psi: "))
l_psi_per_deg = 0.038                                   #Left side psi/℉ constant
r_psi_per_deg = 0.060                                   #Right side psi/℉ constant, varies per side
cold_temp = float(input("Enter cold avg temp: "))       #average cold tire temp

#Math
delta_temp = hot_temp - cold_temp                       #Change in tempurature
l_delta_psi = delta_temp * l_psi_per_deg                #Calculate Left change in psi
r_delta_psi = delta_temp * r_psi_per_deg                #Calculate Right change in psi
l_rec_cold_psi = des_hot_psi - l_delta_psi              #recommended cold psi for left side
r_rec_cold_psi = des_hot_psi - r_delta_psi              #recommended cold psi fo right side

#Print results
print("Recommended cold psi left: ", l_rec_cold_psi, "     Recommended cold psi right: ", r_rec_cold_psi)