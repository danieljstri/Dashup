def convert_to_float(value):
    """
    Convert a string value to float by removing currency symbols and commas,
    and handling negative numbers.
    """
    # Remove currency symbols and spaces
    cleaned_value = value.replace("R$", "").strip()
    
    # Preserve the negative sign if it exists
    is_negative = cleaned_value.startswith('-')
    
    # Remove negative sign for now to clean the rest of the number
    cleaned_value = cleaned_value.replace("-", "")
    
    # Remove thousands separator and replace decimal comma with dot
    cleaned_value = cleaned_value.replace(".", "").replace(",", ".")
    
    # Convert to float
    result = float(cleaned_value)
    
    # Return negative value if it was originally negative
    return -result if is_negative else result
