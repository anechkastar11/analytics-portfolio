import pandas as pd
data = {
    "food": [
        "Pizza",
        "Burger",
        "Pasta",
        "Sushi",
        "Salad",
        "Tacos",
        "Soup",
        "Steak",
        "Ramen",
        "Sandwich"
    ],
    "orders": [42, 35, 28, 51, 19, 24, 16, 21, 33, 26]
}
df = pd.DataFrame(data)
print(df)
