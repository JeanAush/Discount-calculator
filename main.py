def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent/100) * price
        print (price - discount_amount)
    else:
        print(price)  

def main():
    price = float(input("Enter original price before discount: "))
    discount_percent = float(input("Enter the discount percent: "))

    calculate_discount(price, discount_percent)

if __name__ == "__main__":
    main()
    


