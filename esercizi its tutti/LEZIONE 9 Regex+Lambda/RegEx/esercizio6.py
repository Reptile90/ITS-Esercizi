import re

def check_product_code(code):
    return bool(re.match(r"^PROD-\d{4}-[A-Z]{2}$", code))


print(check_product_code("PROD-9876-ZX"))  # True
print(check_product_code("PROD-99-ZX"))    # False
print(check_product_code("PROD-12345-AB")) # False