def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height) / 100
        
        if not (10 <= weight <= 500):
            raise ValueError("Please enter a weight between 10 kg and 500 kg")
        if not (30 <= height * 100 <= 300):
            raise ValueError("Please enter a height between 30 cm and 300 cm")
        
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        return bmi, category
    except ValueError:
        raise ValueError("Please enter valid numbers for weight and height")
