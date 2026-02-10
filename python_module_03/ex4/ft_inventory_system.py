#!/usr/bin/env python3
def print_info_inventory(inv: dict):
    """
    Print detailed inventory information and general statistics.

    :param inv: Dictionary containing inventory slots with item details.
    """
    cat_items = {}
    for slot in inv:
        obj: dict = inv[slot]
        qty = obj.get("qty", 0)
        gold = obj.get("gold", 0)
        cat = obj.get("cat", "unknow")
        rarity = obj.get("rarity", "unknow")
        cat_items.update({cat: qty})
        print(f"{slot} ({cat}, {rarity}): "
              f"{qty}x @ {gold} gold each",
              f"= {qty * gold} gold")

    print(f"\nInventory value: {inventory_value(inv)} gold")
    print(f"Item count: {inventory_amount(inv)} items")
    txt = ""
    for cat, qty in cat_items.items():
        txt += f"{cat}({qty}), "
    txt = txt[:-2]
    print(f"Catergory: {txt}")


def inventory_value(inv: dict) -> int:
    """
    Calculate the total gold value of the inventory.

     :param inv: Dictionary of items, where each value is a dict with 'qty'
      and 'gold'.
     :return: Total value calculated as the sum of (quantity * price)
      for all items.
    """
    inv_value = 0
    for obj in inv:
        item: dict = inv[obj]
        qty = item.get("qty", 0)
        gold = item.get("gold", 0)
        inv_value += qty * gold
    return inv_value


def inventory_amount(inv: dict) -> int:
    """
    Returns the total quantity of all items in the inventory.

    :param inv: Dictionary where values are dicts containing a 'qty' key.
    :return: Total sum of all quantities.
    """
    inv_qty = 0
    for obj in inv:
        inv_qty += obj_amount(inv, obj)
    return inv_qty


def obj_amount(inv: dict, obj: str) -> int:
    """
    Returns the amount of a object in a inventory

    :param inv Dictionary of a inventory
    :param obj The name of the object
    :return: Total amount of the object or 0 if isn't exist
    """
    if inv.get(obj):
        item = inv.get(obj, "unknown")
        return item.get("qty", 0)
    return 0


def transaction(inv_out: dict, inv_in: dict, obj: str, qty: int):
    """
    Execute a transaction of an item between two inventories.

    :param inv_out: Inventory dictionary to take the object from.
    :param inv_in: Inventory dictionary where the object will be placed.
    :param obj: The key of the object to trade.
    :param qty: The quantity of the object to transfer.
    """
    item: dict = inv_out.get(obj)
    if item and item.get("qty", 0) >= qty:
        if obj not in inv_in:
            inv_in[obj] = {k: v for k, v in item.items()}
            inv_in[obj]["qty"] = 0

        inv_out[obj]["qty"] -= qty
        inv_in[obj]["qty"] += qty
        print("Transaction succesful!")
    else:
        print("Transaction Failed")


def most_value_inv(invs: dict) -> str:
    """
    Identify the wealthiest player and format the result as a string.

    :param invs: Dictionary containing inventories as values.
    :return: A formatted string with the player name and
             their total gold value.
    """
    most_value = 0
    most_name = ""
    for name, inv in invs.items():
        value = inventory_value(inv)
        if value > most_value:
            most_value = value
            most_name = name

    return f"Most value player: {most_name} ({most_value})"


def most_items_inv(invs: dict) -> str:
    """
    Identify the player with the most items and format the result as a string.

    :param invs: Dictionary containing inventories as values.
    :return: A formatted string with the name of the player
             with the highest item count.
    """
    most_items = 0
    for name, inv in invs.items():
        items = inventory_amount(inv)
        if items > most_items:
            most_items = items
            most_name = name

    return f"Most value player: {most_name} ({most_items})"


def rarest_items_inv(invs: dict) -> str:
    """
    Identify the rarest items in the inventoris and format
    the result as a string.

    :param invs: Dictionary containing inventories as values.
    :return: A formatted string with the name of the rarest items.
    """
    txt = ""
    for inv in invs.values():
        for obj, stats in inv.items():
            if stats.get("rarity") == "rare":
                txt += f"{obj}, "
    return f"Rarest items: {txt[:-2]}"


def ft_inventory_system():
    print("=== Player Inventory System ===")

    alice = {"sword": {"qty": 1,
                       "gold": 500,
                       "cat": "weapon",
                       "rarity": "rare"},
             "potion": {"qty": 5,
                        "gold": 50,
                        "cat": "consumable",
                        "rarity": "common"},
             "shield": {"qty": 1,
                        "gold": 200,
                        "cat": "armor",
                        "rarity": "uncommon"}}
    bob = {"magic_ring": {"qty": 1,
                          "gold": 400,
                          "cat": "weapon",
                          "rarity": "rare"}}

    invs = {"Alice": alice, "Bob": bob}

    print("\n=== Alice's Inventory ===")
    print_info_inventory(invs.get("Alice"))

    print("\n=== Transaction: Alice gives Bob 2 potions")
    transaction(invs.get("Alice"), invs.get("Bob"), "potion", 2)

    print("\n=== Update Inventories ===")
    alice_pots = obj_amount(alice, "potion")
    print(f"Alice potions: {alice_pots}")
    bob_pots = obj_amount(bob, "potion")
    print(f"Bob potions: {bob_pots}")

    print("\n=== Inventory Analytics ===")
    print(most_value_inv(invs))
    print(most_items_inv(invs))
    print(rarest_items_inv(invs))


# if __name__ == "__main__":
#     ft_inventory_system()
