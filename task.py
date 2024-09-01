from typing import Dict
import asyncio

# 1. Product Class
class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"

# 2. Inventory Class
class Inventory:
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def remove_product(self, name: str, quantity: int) -> None:
        if name in self.products:
            if self.products[name].quantity <= quantity:
                del self.products[name]
            else:
                self.products[name].quantity -= quantity

    def get_inventory(self) -> Dict[str, Product]:
        return self.products

# 3. Main Function for Inventory Management
def main_inventory() -> None:
    inventory = Inventory()

    # Adding products
    inventory.add_product(Product("Apple", 10))
    inventory.add_product(Product("Banana", 5))
    inventory.add_product(Product("Apple", 5))  # Updates quantity of Apple
    
    # Display inventory after adding
    print("Inventory after adding products:")
    for product in inventory.get_inventory().values():
        print(product)

    # Removing products
    inventory.remove_product("Apple", 8)
    
    # Display inventory after removing
    print("\nInventory after removing products:")
    for product in inventory.get_inventory().values():
        print(product)

# 4. Asynchronous Function for Simulating Downloads with Time Remaining
async def task(name: str, duration: int):
    print(f"Starting {name} which will take {duration} seconds...")
    for remaining in range(duration, 0, -1):
        print(f"{name} is running. Time remaining: {remaining} seconds.")
        await asyncio.sleep(1)
    print(f"{name} completed!\n")

# 5. Main Function for Async Download Simulation
async def main_async() -> None:
    await asyncio.gather(
        task("Task A", 6),
        task("Task B", 4),
        task("Task C", 8)
    )

# 6. Entry Point
if __name__ == "__main__":
    # Run inventory management demonstration
    main_inventory()
    
    # Run asynchronous download simulation
    asyncio.run(main_async())
