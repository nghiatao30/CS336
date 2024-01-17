import re

def remove_trailing_zeros(input_string):
    parts = input_string.rsplit('_', 1)
    
    if len(parts) == 2:
        prefix, number_part = parts
        modified_number = re.sub(r'^0+', '', number_part)
        modified_string = f'{prefix}_{modified_number}'
        return modified_string
    
    return input_string

# Example usage
original_string = 'abc_000000010000'
modified_string = remove_trailing_zeros(original_string)
print(modified_string)
