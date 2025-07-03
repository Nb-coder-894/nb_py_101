import numpy as np
sales_data = np.array([
    [45, 52, 33, 66, 71, 48, 55],  # Product A
    [28, 35, 40, 32, 29, 31, 27],  # Product B
    [60, 65, 58, 72, 80, 63, 59],  # Product C
    [15, 20, 18, 22, 17, 19, 21],  # Product D
    [50, 55, 48, 60, 62, 53, 57]   # Product E
])
total_sales = (np.sum(sales_data, axis=1))
