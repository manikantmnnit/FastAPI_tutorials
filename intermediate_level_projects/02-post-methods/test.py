
import json
import os



# File names
customer_file = 'customer.json'
order_file = 'order.json'

# Ensure JSON files exist
for file in [customer_file, order_file]:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({}, f,indent=4)