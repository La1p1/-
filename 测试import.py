def make_pizza(size , *toppings):
        """显示pizza的配料和大小"""
        print("\nMaking a " + str(size) + 
                "-inch pizza with the following toppings: ")
        for topping in toppings:
                print("- " + topping)