def total_quantity(lines):
    if any(row["quantity"] < 0 for row in lines):
        raise ValueError("negative quantity")
    return sum(row["quantity"] for row in lines)
