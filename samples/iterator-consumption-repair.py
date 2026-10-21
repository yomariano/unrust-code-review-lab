def total_quantity(lines):
    total = 0
    for row in lines:
        quantity = row["quantity"]
        if quantity < 0:
            raise ValueError("negative quantity")
        total += quantity
    return total
