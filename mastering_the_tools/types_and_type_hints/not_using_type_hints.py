def compute_stats(uses, plans, products):
    total_uses = sum(uses)
    total_plans = len(plans)
    total_products = len(products)

    return total_uses, total_plans, total_products
