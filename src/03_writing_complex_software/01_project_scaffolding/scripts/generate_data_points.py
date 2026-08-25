import random

# Generate a simple dataset
data = [(x, x**2) for x in range(10)]

# Basic data analysis
mean_x = sum([x for x, _y in data]) / len(data)
mean_y = sum([y for _x, y in data]) / len(data)
print(f"Mean of x: {mean_x}")
print(f"Mean of y: {mean_y}")


# Generate new data points based on a simple function
def generate_new_data(num_points: int):
    new_data: list[tuple[int | float, int | float]] = []
    for _ in range(num_points):
        x = random.uniform(0, 10)
        y = x**2 + random.uniform(-5, 5)  # Adding some noise
        new_data.append((x, y))
    return new_data


# Generate and display new data points
new_data = generate_new_data(5)
print("New generated data points (x, y):")
for x, y in new_data:
    print(f"{x:.2f}, {y:.2f}")
