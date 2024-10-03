"""
Economia Module

This module provides functions to calculate economic metrics such as tax rates
and markups based on a company's gross revenue. It includes functions to determine
the appropriate tax rates and reductions based on predefined revenue brackets
and whether the company is part of MEDUP. Additionally, it offers a function
to calculate the markup for a specific product by allocating fixed and variable
expenses proportionally based on revenue contributions.
"""

def get_aliquota_reducao(k, is_medup):
    """
    Determines the tax rate (aliquota) and reduction (reducao) based on the
    company's gross revenue (k) and its MEDUP status.

    The formula used is: ((k * aliquota) - reducao) / k

    Args:
        k (float): The gross revenue of the company.
        is_medup (bool): Indicates whether the company is part of MEDUP.

    Returns:
        tuple:
            float or None: The applicable tax rate (aliquota). Returns None if `k` is outside defined ranges.
            float or None: The applicable reduction (reducao). Returns None if `k` is outside defined ranges.

    Raises:
        ValueError: If `k` is not a positive number.
    """
    if k <= 0:
        raise ValueError("Gross revenue 'k' must be a positive number.")

    match k:
        case _ if k <= 180000:
            if is_medup:
                aliquota = 0.06  # 6%
                reducao = 0
            else:
                aliquota = 0.155  # 15.5%
                reducao = 0
        case _ if 180001 <= k <= 360000:
            if is_medup:
                aliquota = 0.112  # 11.2%
                reducao = 9360
            else:
                aliquota = 0.18  # 18%
                reducao = 4500
        case _ if 360001 <= k <= 720000:
            if is_medup:
                aliquota = 0.135  # 13.5%
                reducao = 17640
            else:
                aliquota = 0.195  # 19.5%
                reducao = 9900
        case _ if 720001 <= k <= 1800000:
            if is_medup:
                aliquota = 0.16  # 16%
                reducao = 35640
            else:
                aliquota = 0.205  # 20.5%
                reducao = 17100
        case _ if 1800001 <= k <= 3600000:
            if is_medup:
                aliquota = 0.21  # 21%
                reducao = 125640
            else:
                aliquota = 0.23  # 23%
                reducao = 62100
        case _ if 3600001 <= k <= 4800000:
            if is_medup:
                aliquota = 0.33  # 33%
                reducao = 648000
            else:
                aliquota = 0.305  # 30.5%
                reducao = 540000
        case _:
            # Handle values of k outside the defined ranges
            aliquota = None
            reducao = None
    return aliquota, reducao


def economia(receita_bruta):
    """
    Calculates the economic metrics based on the company's gross revenue.

    This function computes the tax results for both MEDUP and non-MEDUP companies
    and determines the difference between them.

    The formula used is: ((k * aliquota) - reducao) / k

    Args:
        receita_bruta (str or float): The gross revenue of the company.

    Returns:
        dict: A dictionary containing the following keys:
            - 'medup': A dictionary with 'aliquota', 'reducao', and 'resultado' for MEDUP.
            - 'non_medup': A dictionary with 'aliquota', 'reducao', and 'resultado' for non-MEDUP.
            - 'diferenca': The difference between the non-MEDUP and MEDUP results.

    Raises:
        ValueError: If `receita_bruta` cannot be converted to a positive float.
    """
    try:
        k = float(receita_bruta)
    except (TypeError, ValueError):
        raise ValueError("Receita bruta must be a number.")

    if k <= 0:
        raise ValueError("Receita bruta must be a positive number.")

    # Compute for is_medup = True
    aliquota_medup, reducao_medup = get_aliquota_reducao(k, True)
    if aliquota_medup is None or reducao_medup is None:
        resultado_medup = None
    else:
        resultado_medup = ((k * aliquota_medup) - reducao_medup) / k

    # Compute for is_medup = False
    aliquota_non_medup, reducao_non_medup = get_aliquota_reducao(k, False)
    if aliquota_non_medup is None or reducao_non_medup is None:
        resultado_non_medup = None
    else:
        resultado_non_medup = ((k * aliquota_non_medup) - reducao_non_medup) / k

    # Calculate the difference
    if resultado_non_medup is not None and resultado_medup is not None:
        diferenca = resultado_non_medup - resultado_medup
    else:
        diferenca = None

    return {
        'medup': {
            'aliquota': aliquota_medup,
            'reducao': reducao_medup,
            'resultado': resultado_medup
        },
        'non_medup': {
            'aliquota': aliquota_non_medup,
            'reducao': reducao_non_medup,
            'resultado': resultado_non_medup
        },
        'diferenca': diferenca
    }


def expenses_product_calculation(total_revenue, product_revenue, fixed_expenses, variable_expenses, expenses_product):
    """
    Calculates the proportion of fixed and variable expenses allocated to a specific product
    based on its revenue contribution to the total revenue. This is used to determine
    the markup profit of the product.

    The calculation follows the formula:
    - Proportion = product_revenue / total_revenue
    - Fixed Expenses for Product = fixed_expenses * proportion
    - Variable Expenses for Product = (variable_expenses * proportion) + expenses_product

    Args:
        total_revenue (float): The total revenue of the company.
        product_revenue (float): The revenue generated by the specific product.
        fixed_expenses (float): The total fixed expenses of the company.
        variable_expenses (float): The total variable expenses of the company.
        expenses_product (float): The variable expenses specific to the product.

    Returns:
        tuple:
            float: The allocated fixed expenses for the product.
            float: The allocated variable expenses for the product.

    Raises:
        ValueError: If `total_revenue` is zero or negative.
    """
    if total_revenue <= 0:
        raise ValueError("Total revenue must be a positive number.")

    proportion = product_revenue / total_revenue
    fixed_expenses_product = fixed_expenses * proportion
    variable_expenses_product = (variable_expenses * proportion) + expenses_product

    return fixed_expenses_product, variable_expenses_product
