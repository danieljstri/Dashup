# formula: ((k * aliquota) - valor_a_reduzir) / k

def get_aliquota_reducao(k, is_medup):
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
    k = float(receita_bruta)
    
    # Compute for is_medup = True
    aliquota_medup, reducao_medup = get_aliquota_reducao(k, True)
    resultado_medup = ((k * aliquota_medup) - reducao_medup) / k
    
    # Compute for is_medup = False
    aliquota_non_medup, reducao_non_medup = get_aliquota_reducao(k, False)
    resultado_non_medup = ((k * aliquota_non_medup) - reducao_non_medup) / k
    
    # Calculate the difference
    diferenca = resultado_non_medup - resultado_medup
    
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
    Calculate the proportion of the fixed expenses, and the variables expenses of a product, based on the total revenue and the product revenue, to calculate the MARKUP profit of the product.

    :total_revenue: the total revenue of the company
    :product_revenue: the revenue of the product
    :fixed_expenses: the fixed expenses of the company
    :variable_expenses: the variable expenses of the company
    :variable_expenses_product: the variable expenses of the product 

    :return: the proportion of the fixed expenses, and the variables expenses of a product
    """
    proportion = product_revenue / total_revenue
    fixed_expenses_product = fixed_expenses * proportion
    variable_expenses_product = (variable_expenses * proportion) + expenses_product

    return fixed_expenses_product, variable_expenses_product
    