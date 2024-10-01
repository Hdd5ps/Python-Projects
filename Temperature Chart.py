# Step 1: Initialize variable F
F = 0.0

# Step 2: Set up the header
print("Fahrenheit       Celsius")

print("------------------------")

# Step 3: Use a while loop to calculate and display the results
while F <= 212:
    
    C = (F - 32) * 5 / 9  # Conversion formula
    
    print(format(F, '10.1f'), format(C, '10.1f'))
    
    F = F + 2  # Increment by 5 degrees
