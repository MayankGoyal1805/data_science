import math
import statistics
import numpy as np
import pandas as pd

import pandas as pd

try:
    # Create a simple DataFrame
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)

    # Perform a basic operation
    sum_col1 = df['col1'].sum()

    # Print a success message and the result
    print("Pandas installation successful!")
    print("Sum of 'col1':", sum_col1)

except ImportError:
    print("Pandas is not installed. Please install it using 'pip install pandas'.")
except Exception as e:
    print(f"An error occurred during the Pandas test: {e}")

