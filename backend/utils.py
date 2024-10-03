"""
Utils Module

This module provides utility functions for data processing, including
conversions and formatting. It includes functions to convert string
representations of monetary values into floating-point numbers, handling
currency symbols, thousand separators, decimal commas, and negative values.
"""

def convert_to_float(value):
    """
    Converts a string value to a float by removing currency symbols and commas,
    and handling negative numbers.

    Args:
        value (str): The string representation of the monetary value to convert.
                     It should contain currency symbols like "R$", thousand separators
                     (.), decimal commas (,), and may include a negative sign (-).

    Returns:
        float: The converted floating-point number. Returns a negative float if the
               original string had a negative sign.

    Raises:
        ValueError: If the cleaned string cannot be converted to a float.
        AttributeError: If the input value does not have the replace method (i.e., is not a string).
    """
    if not isinstance(value, str):
        raise AttributeError("Input value must be a string.")
    
    # Remove currency symbols and spaces
    cleaned_value = value.replace("R$", "").strip()
    
    # Preserve the negative sign if it exists
    is_negative = cleaned_value.startswith('-')
    
    # Remove negative sign for now to clean the rest of the number
    cleaned_value = cleaned_value.replace("-", "")
    
    # Remove thousands separator and replace decimal comma with dot
    cleaned_value = cleaned_value.replace(".", "").replace(",", ".")
    
    try:
        # Convert to float
        result = float(cleaned_value)
    except ValueError as e:
        raise ValueError(f"Cannot convert cleaned value '{cleaned_value}' to float.") from e
    
    # Return negative value if it was originally negative
    return -result if is_negative else result
