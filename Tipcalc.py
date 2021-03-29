print("Reed's really cool tip calculator")
full_amount = input("Pleae input the bill total here!\n£")

people = input("How many people are splitting the bill?\n")

tip_percent = input("Enter percentile tip as a 0.# number (e.g 0.15 for 15%)\n")
15

tip_for_calc = float(tip_percent)

tip = int(full_amount) * tip_for_calc

final_calc = round((int(full_amount) + tip) / int(people),2)

print(f"Ok so each person needs to pay\n£{final_calc}")

input("anything else?") #This is here beacuse i dont know how get the IDE to display the final output without instantly closing without it.
