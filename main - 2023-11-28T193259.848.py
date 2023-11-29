# Calorie values for each ingredient
calories_per_potato = 200
calories_per_tablespoon_olive_oil = 120
calories_per_can_sardines = 190
calories_arugula = 5
calories_per_cup_yogurt = 125  # Assuming an average value
calories_per_apple = 95
calories_per_onion = 45

# Quantity of each ingredient
quantity_potatoes = 2
quantity_tablespoons_olive_oil = 8
quantity_cans_sardines = 1
quantity_arugula = 1  # Assuming one handful
quantity_cup_yogurt = 1
quantity_apple = 1
quantity_onion = 1

# Calculate total calories
total_calories = (
    quantity_potatoes * calories_per_potato +
    quantity_tablespoons_olive_oil * calories_per_tablespoon_olive_oil +
    quantity_cans_sardines * calories_per_can_sardines +
    quantity_arugula * calories_arugula +
    quantity_cup_yogurt * calories_per_cup_yogurt +
    quantity_apple * calories_per_apple +
    quantity_onion * calories_per_onion
)

# Display the result
print(f'Total Calories: {total_calories} calories')
