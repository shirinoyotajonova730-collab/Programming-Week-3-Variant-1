print("=== Coffee Shop Order System ===")
print("Enter drink sizes: small, medium, or large")
print("Type 'done' when finished ordering\n")

total = 0.0

while True:
    size = input("Enter drink size: ").lower()
    
    if size == "done":
        break
    elif size == "small":
        price = 3.50
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    elif size == "medium":
        price = 4.50
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    elif size == "large":
        price = 5.50
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    else:
        print("Invalid size! Please enter small, medium, large, or done.\n")

print("\n=== Order Summary ===")
print(f"Subtotal: ${total:.2f}")

# Chegirma sharti ($20.00 yoki undan ko'p bo'lsa $3.00 chegirma)
if total >= 20.00:
    discount = 3.00
    final_total = total - discount
    print(f"Loyalty Discount: -${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")
else:
    print(f"Final Total: ${total:.2f}")

print("Thank you for your order!")