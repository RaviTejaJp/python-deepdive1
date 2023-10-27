import ctypes

def print_value_at_address(address):
    try:
        print("Going here")
        value = ctypes.cast(address, ctypes.py_object).value
        print(value)
    except Exception as e:
        print(f"Error accessing memory address: {e}")

# Example usage
a = 10
address = 140706871046024
print_value_at_address(address)
