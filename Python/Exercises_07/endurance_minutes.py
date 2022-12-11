def validate_integer():
 # Loop forever
    while True:
        try:
            user_input = int(input("Enter Fuel In Litres: "))
            fuel_consumption = input("fuel consumption in litres per minute:")
            fuel_consumption = float(fuel_consumption)
            time = user_input / fuel_consumption

            # Time format
            mins = int(time)
        except:
            # Bad value,
            print("Error")
            continue
        else:
            print("time")
            # Good value, exit the loop
            break
        finally:
            # Only runs after the except, continue
            print("Try again - enter Fuel In Litres!")

    validate_integer()
