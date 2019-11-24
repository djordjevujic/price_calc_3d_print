# Fiksne stvari - const values
filament_cost = 15.2  # Eur / kg
printer_price = 900.0  # Euro
assumption_hours = 3000.0 # Hours
failure_rate = 1.1  # Print fail coefficient
electricity_price = 0.04  # E / kWh
printer_power = 0.15  # kW
printer_power_hour = electricity_price * printer_power
cleaning = 0.1
support_removal = 15.0  # E/hour
preparation = 10.0  # E/hour, Inspecting STL, setup for g-code
inspection_cost = 0.1  # E/hour

EUR_TO_DIN_COEFF = 120.0  # Constant for converting EUR to DIN values

# Stampa - Print details
weigh = 56.0  # g
print_hours = 5.0   # h
print_minutes = 47.0  # min
support_removing_hours = 0.05
preparation_hours = 0.05
profit_procent = 20.0  # Profit after calculating outgoings

weigh_kg = weigh / 1000.0
print_time = print_hours + print_minutes / 60.0

print("Amortizacija:" + str(printer_price / assumption_hours))

amort = (printer_price / assumption_hours) * print_time

first_price = amort + printer_power_hour * print_time + filament_cost * weigh_kg
print("Energija i filament: " + str(first_price))

second_price = first_price * failure_rate + cleaning
print(second_price)

thirt_price = second_price + support_removal * support_removing_hours
print("Faktor greske i skidanje suporta: "  + str(thirt_price))

fourth_price = thirt_price + preparation * preparation_hours
print(fourth_price)

fifth_price = fourth_price + print_time * inspection_cost
print(fifth_price)

profit = fifth_price * (profit_procent / 100.0)
print("Profit: " + str(profit))
print("Profit din: " + str(profit * EUR_TO_DIN_COEFF))

final_price = fifth_price + profit

print("Konacna cena (EUR): " + str(final_price))
print("Konacna cena (DIN): " + str(final_price * EUR_TO_DIN_COEFF))
print("\nCena slanja posiljke nije uracunata \ Shipping not included")