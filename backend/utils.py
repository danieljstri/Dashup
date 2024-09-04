def convert_to_float(value):
    """
    Convert a string value to float by removing currency symbols and commas
    """
    return float(value.replace("R$", "").replace(".", "").replace(",", "."))