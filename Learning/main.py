#Goal is to create a script that lists the available minute bundles, asks the user to choose a bundle and currency and calculates and displays the total price and price per minute for that selection.
#The pricing data
pricing_data = {
    "500":{"USD":175, "EUR":175, "GBP":130, "AUD":265},
    "1000":{"USD":350, "EUR":350, "GBP":260, "AUD":530},
    "2500":{"USD":725, "EUR":725, "GBP":550, "AUD":1100},
    "5000":{"USD":1450, "EUR":1450, "GBP":1100, "AUD":2200},
    "10000":{"USD":2500, "EUR":2500, "GBP":1900, "AUD":3800}
}
#for loop to display available bundles
# 1. Display the available options
print("---Aircall AI Voice Agent Pricing---")
print ("Available Minute Bundles:")
for bundle in pricing_data:
    print(f"- {bundle} minutes")
# 2. Get user choices
#We use .upper() so 'usd' or 'USD' both work
selected_bundle = input("\nEnter the bundle size (eg., 500): ")
selected_currency = input("Enter currency (USD, GBP, EUR, AUD): ").upper()
# 3. Retrive and calculate
#This looks into the dictionary using the two inputs as keys
try:
    # 1. Ask for the actual minutes used
    actual_minutes = int(input("How many minutes were actually used?"))

    # 2. Get the base data
    bundle_size = int(selected_bundle)
    base_price = pricing_data[selected_bundle][selected_currency]
    rate_per_min = base_price / bundle_size

    # 3. Calculate Overage Logic
    if actual_minutes > bundle_size:
        extra_minutes = actual_minutes - bundle_size
        overage_cost = extra_minutes * rate_per_min
        total_cost = base_price +overage_cost
    else:
        #if they stay under, they just pay the flat bundle price
        extra_minutes = 0
        total_cost = base_price

    # 4. Show the detailed result
    print(f"\n--- Detailed Quote Summary ---")
    print(f"Bundle: {selected_bundle} minutes ({base_price} {selected_currency})")

    if extra_minutes > 0:
        print(f"Overage: {extra_minutes} extra mins x {rate_per_min:.2f} = {overage_cost:.2f} {selected_currency}")

    print(f"Final Total: {total_cost: .2f} {selected_currency}")
except KeyError:
    print("\nError: Invalid bundle or currency.")
except ValueError:
    print("\nError: Please enter numbers only for minutes.")