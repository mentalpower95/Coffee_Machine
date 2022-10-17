class CoffeeMachine:

    def __init__(self):
        self.amounts = [400, 540, 120, 9, 550]

    def coffee_machine(self):
        self.make_action(self.amounts)

    def make_action(self, all_amount):
        while True:
            print("")
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy_stuff(all_amount)
            elif action == "fill":
                self.fill_stuff(all_amount)
            elif action == "take":
                self.take_money(all_amount)
            elif action == "remaining":
                self.print_info(all_amount)
            elif action == "exit":
                break

    def print_info(self, levels):
        print(f"The coffee machine has: ")
        print(f"{levels[0]} ml of water")
        print(f"{levels[1]} ml of milk")
        print(f"{levels[2]} g of coffee beans")
        print(f"{levels[3]} disposable cups")
        print(f"${levels[4]} of money")

    def buy_stuff(self, all_amount):
        chosen_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if chosen_coffee == "back":
            return
        else:
            chosen_coffee = int(chosen_coffee) - 1
        cost = self.coffee_kinds(chosen_coffee)
        if self.checking_levels(cost, all_amount):
            for x in range(len(all_amount) - 1):
                all_amount[x] -= cost[x]
            all_amount[-1] += cost[-1]
        return all_amount

    def coffee_kinds(self, number):
        water = [250, 350, 200]
        milk = [0, 75, 100]
        beans = [16, 20, 12]
        money = [4, 7, 6]
        return [water[number], milk[number], beans[number], 1, money[number]]

    def checking_levels(self, cost, all_amount):
        ingredient = ["water", "milk", "beans", "cups"]
        for x in range(len(cost) - 1):
            if all_amount[x] < cost[x]:
                print(f"Sorry, not enough {ingredient[x]}!")
                return False
        print("I have enough resources, making you a coffee!")
        return True

    def fill_stuff(self, all_amount):
        water = int(input("Write how many ml of water you want to add: "))
        milk = int(input("Write how many ml of milk you want to add: "))
        beans = int(input("Write how many grams of coffee beans you want to add: "))
        cups = int(input("Write how many disposable cups you want to add:"))
        added = [water, milk, beans, cups, 0]
        for x in range(len(all_amount)):
            all_amount[x] += added[x]
        return all_amount

    def take_money(self, all_amounts):
        print(f"I gave you ${all_amounts[4]}")
        all_amounts[4] = 0
        return all_amounts


if __name__ == "__main__":
    CoffeeMachine().coffee_machine()
