import json

class Item:
    """
    Base class for all inventory items.
    
    Attributes:
    name (str): The name of the item.
    description (str): A short description of the item.
    rarity (str): The rarity level of the item (common, uncommon, epic, legendary).
    ownership (str, optional): The owner of the item.
    """
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.ownership = None  

    def pick_up(self, character: str) -> str:
        """Assigns ownership of the item to a character."""
        self.ownership = character
        return f'{self.name} is now owned by {character}'
    
    def throw_away(self) -> str:
        """Removes ownership of the item."""
        self.ownership = None
        return f'{self.name} is thrown away'
    
    def use(self) -> str:
        """Uses the item if it has an owner."""
        if self.ownership:
            return f'{self.name} is used'
        else:
            return f'{self.name} has no owner and cannot be used'
        
    def to_json(self):
        """Serializes the item object into a JSON-compatible dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "rarity": self.rarity,
            "ownership": self.ownership
        }
    
    @classmethod
    def from_json(cls, data):
        """Creates an item instance from a JSON dictionary."""
        item = cls(data["name"], data["description"], data["rarity"])
        item.ownership = data.get("ownership")
        return item
    
    def __str__(self):
        return f'{self.name} ({self.rarity})'

class Weapon(Item):
    """
    Represents a weapon in the inventory.
    
    Attributes:
    damage (int): The attack power of the weapon.
    type (str): The type of the weapon (e.g., single-handed, double-handed, pike, ranged).
    """
    def __init__(self, name, description='', rarity='common', damage=0, type=''):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.type = type
        self.attack_modifier = 1.0 if rarity in ['common', 'uncommon', 'epic'] else 1.15
    
    def to_json(self):
        """Serializes the weapon object into a JSON-compatible dictionary."""
        data = super().to_json()
        data.update({
            "damage": self.damage,
            "type": self.type
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        """Creates a Weapon instance from a JSON dictionary."""
        return cls(data["name"], data["description"], data["rarity"], data["damage"], data["type"])

class Shield(Item):
    """
    Represents a shield in the inventory.
    
    Attributes:
    defense (int): The defensive power of the shield.
    broken (bool): Indicates if the shield is broken.
    """
    def __init__(self, name, description='', rarity='common', defense=0, broken=False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
    
    def to_json(self):
        """Serializes the shield object into a JSON-compatible dictionary."""
        data = super().to_json()
        data.update({
            "defense": self.defense,
            "broken": self.broken
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        """Creates a Shield instance from a JSON dictionary."""
        return cls(data["name"], data["description"], data["rarity"], data["defense"], data["broken"])

class Potion(Item):
    """
    Represents a potion in the inventory.
    
    Attributes:
    value (int): The effect value of the potion.
    effective_time (str): The duration of the potion's effect.
    """
    def __init__(self, name, description='', rarity='common', value=0, effective_time=''):
        super().__init__(name, description, rarity)
        self.value = value
        self.effective_time = effective_time
    
    def to_json(self):
        """Serializes the potion object into a JSON-compatible dictionary."""
        data = super().to_json()
        data.update({
            "value": self.value,
            "effective_time": self.effective_time
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        """Creates a Potion instance from a JSON dictionary."""
        return cls(data["name"], data["description"], data["rarity"], data["value"], data["effective_time"])

class Inventory:
    """
    Represents an inventory containing multiple items.
    
    Attributes:
    owner (str): The owner of the inventory.
    items (list): A list of Item objects stored in the inventory.
    """
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item):
        """Adds an item to the inventory."""
        if item.ownership is None:
            item.pick_up(self.owner)
        self.items.append(item)

    def to_json(self):
        """Serializes the inventory into a JSON-compatible dictionary."""
        return {
            "owner": self.owner,
            "items": [item.to_json() for item in self.items]
        }
    
    @classmethod
    def from_json(cls, data):
        """Creates an Inventory instance from a JSON dictionary."""
        inventory = cls(data["owner"])
        for item_data in data["items"]:
            item_type = item_data.get("type", "Item")
            if item_type == "Weapon":
                inventory.add_item(Weapon.from_json(item_data))
            elif item_type == "Shield":
                inventory.add_item(Shield.from_json(item_data))
            elif item_type == "Potion":
                inventory.add_item(Potion.from_json(item_data))
            else:
                inventory.add_item(Item.from_json(item_data))
        return inventory

class InventoryEncoder(json.JSONEncoder):
    """
    Custom JSON encoder for Inventory and Item objects.
    """
    def default(self, obj):
        if isinstance(obj, Inventory) or isinstance(obj, Item):
            return obj.to_json()
        return super().default(obj)

# Usage
def test_inventory_serialization():
    """
    Tests the serialization and deserialization of an Inventory object which:
    - Creates an inventory with multiple item types.
    - Serializes the inventory to JSON format.
    - Deserializes the JSON back into an Inventory object.
    - Prints it.

    Expected Output:
    - JSON string representation of the inventory.
    - List of deserialized items showing their names and rarity.
    """
    inventory = Inventory(owner="Beleg")
    inventory.add_item(Weapon(name='Longbow', rarity='common', damage=200, type='ranged'))
    inventory.add_item(Shield(name='Wooden Shield', rarity='common', defense=50))
    inventory.add_item(Potion(name='Health Potion', description='Restores 50 HP', rarity='common', value=50))

    # Serialize
    json_data = json.dumps(inventory, cls=InventoryEncoder, indent=4)
    print("Serialized JSON:")
    print(json_data)

    # Deserialize
    loaded_inventory = Inventory.from_json(json.loads(json_data))
    print("\nDeserialized Inventory:")
    for item in loaded_inventory.items:
        print(f"{item.name} ({item.rarity})")

# Runs it
test_inventory_serialization()
