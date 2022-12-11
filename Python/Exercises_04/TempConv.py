#My list of kelvin temps
my_Temp_in_kelvin = [273.15, 283.15, 293.15, 294.15, 303.15,310.15,313.15,323.15,333.15,343.15]

#My conversion for Kelvin to celsius
my_Temp_in_celsius = [(Temp - 273.15) for Temp in my_Temp_in_kelvin]

#My conversion for kelvin to Fahrenheit
my_Temp_in_Fahrenheit = [(Temp * 1.8 - 459.67) for Temp in my_Temp_in_kelvin]

#My printed results
print(my_Temp_in_celsius)
print(my_Temp_in_Fahrenheit)