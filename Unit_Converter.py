print("Unit converter by junior python developer AITMAD")

def weight_converter():
    while True:
        try:
            # Get the weight value first
            val = input("Enter the weight value: ").strip()
            weight = float(val)
            
            # Ask for the unit
            unit = input("Is this in (K)gs or (L)bs? ").strip().upper()

            if unit == "K":
                # Kilograms to Pounds: Multiply by 2.20462
                converted = weight * 2.20462
                print(f"{weight} kg is approximately {round(converted, 2)} lbs.")
                
            elif unit == "L":
                # Pounds to Kilograms: Divide by 2.20462
                converted = weight / 2.20462
                print(f"{weight} lbs is approximately {round(converted, 2)} kg.")
                
            else:
                print("Sorry, I didn't recognize that unit. Please use 'K' or 'L'.")

            print("Thank you for using the weight converter!")
            return # Exit after successful conversion
            
            

        except ValueError:
            print("That doesn't look like a number. Please try again with digits (e.g., 75.5).")
        

weight_converter()
