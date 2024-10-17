class itemz:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)  # Ensuring price is a float
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def getTotal(self):
        return self.price * self.qty

    def getTMostPrices(self):
        return self.price * self.qty * 0.6


class shoppinCart:
    def __init__(self):
        self.items = []
        self.taxRate = 0.08
        self.memberDiscount = 0.05
        self.bigSpenderDiscount = 10
        self.couponDiscount = 0.15
        self.currency = "USD"

    def addItem(self, item):
        self.items.append(item)

    def calculateSubtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.getTotal()
        return subtotal

    def applyDiscounts(self, subtotal, isMember, hasCoupon):
        if isMember:
            subtotal -= subtotal * self.memberDiscount

        if subtotal > 100:
            subtotal -= self.bigSpenderDiscount

        return subtotal

    def calculateTotal(self, isMember, hasCoupon):
        subtotal = self.calculateSubtotal()
        subtotal = self.applyDiscounts(subtotal, isMember, hasCoupon)

        total = subtotal + (subtotal * self.taxRate)

        if hasCoupon:
            total -= total * self.couponDiscount

        return total


def main():
    cart = shoppinCart()

    item1 = itemz("Apple", 1.5, 10)
    item2 = itemz("Banana", 0.5, 5)
    item3 = itemz("Laptop", 1000, 1)  # Fixed price as a number

    item3.category = "electronics"

    cart.addItem(item1)
    cart.addItem(item2)
    cart.addItem(item3)

    isMember = True
    hasCoupon = True  # Changed to boolean

    total = cart.calculateTotal(isMember, hasCoupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print(f"The total price is: ${total:.2f}")


if __name__ == "__main__":
    main()
