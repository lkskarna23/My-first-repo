#6. **Simple Discount:** Prompt for an original price and a discount percentage, then display the final discounted price

o_price=int(input("enter original price : "))
d_percent=int(input("enter discount percentage : "))

d_price=o_price*d_percent/100


print(f"discouted price : {d_price} ")

print(f"Final price is :{o_price-d_price}")
