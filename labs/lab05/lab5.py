class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.ownership = None  

    def pick_up(self, character: str) -> str:
        self.ownership = character
        return f'{self.name} is now owned by {character}'
    
    def throw_away(self) -> str:
        self.ownership = None
        return f'{self.name} is thrown away'
    
    def use(self) -> str:
        if self.ownership:
            return f'{self.name} is used'
        else:
            return f'{self.name} has no owner and cannot be used'
        
    def __str__(self):
        return f'{self.name} ({self.rarity})'


class Weapon(Item):
    def __init__(self, name, description='', rarity='common', damage=0, type=''):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.type = type
        self.attack_modifier = 1.0 if rarity in ['common', 'uncommon', 'epic'] else 1.15
    
    def equip(self):
        return f'{self.name} is equipped by {self.ownership}'

    def use(self):
        if self.ownership:
            attack_move_message = self.attack_move()
            attack_power = self.damage * self.attack_modifier
            return f'{attack_move_message}\n{self.name} is used, dealing {attack_power} damage'
        else:
            return f'{self.name} has no owner and cannot be used'
    
    def attack_move(self):
        if self.type == 'single-handed':
            return self._slash()
        elif self.type == 'double-handed':
            return self._spin()
        elif self.type == 'pike':
            return self._thrust()
        elif self.type == 'ranged':
            return self._shoot()
        else:
            return 'No unique attack animation available'

    def _slash(self):
        return f'{self.name} performs a quick slash with precision!'

    def _spin(self):
        return f'{self.name} spins wildly, striking in all directions!'

    def _thrust(self):
        return f'{self.name} thrusts forward with incredible force!'

    def _shoot(self):
        return f'{self.name} shoots a powerful projectile from afar!'

    def __str__(self):
        if self.rarity == 'legendary':
            return f'~~~ {self.name} ~~~\nThe Legendary Weapon!\nDamage: {self.damage}\nA weapon of unimaginable power!\nRarity: {self.rarity}'
        else:
            return f'{self.name} ({self.rarity})'


class Shield(Item):
    def __init__(self, name, description='', rarity='common', defense=0, broken=False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.0 if rarity in ['common', 'uncommon', 'epic'] else 1.10
        self.broken_modifier = 0.5 if self.broken else 1.0

    def equip(self):
        return f'{self.name} is equipped by {self.ownership}'
    
    def use(self):
        if self.ownership:
            defense_power = self.defense * self.defense_modifier * self.broken_modifier
            return f'{self.name} is used, blocking {defense_power} damage'
        else:
            return f'{self.name} has no owner and cannot be used'
    
    def __str__(self):
        if self.rarity == 'legendary':
            return f'*** {self.name} ***\nThe Legendary Shield!\nDefense: {self.defense}\nImpenetrable defense!\nRarity: {self.rarity}'
        else:
            return f'{self.name} ({self.rarity})'


class Potion(Item):
    def __init__(self, name, description='', rarity='common', value=0, effective_time='', owner=''):
        super().__init__(name, description, rarity)
        self.value = value
        self.effective_time = effective_time
        self.owner = owner
        self.is_used = False
    
    def use(self):
        if self.ownership:
            if not self.is_used:
                self.is_used = True
                return f'{self.owner} used {self.name}, and {self.description} for {self.effective_time}s'
            else:
                return f'{self.name} has already been used and destroyed'
        else:
            return f'{self.name} has no owner and cannot be used'
        
    @classmethod
    def from_ability(cls, name, owner, type):
        if type == 'attack':
            potion = cls(name=name, description='Attack power increased', value=50, effective_time=30, owner=owner)
            potion.ownership = owner
            return potion
        elif type == 'defense':
            potion = cls(name=name, description='Defense power increased', value=50, effective_time=30, owner=owner)
            potion.ownership = owner
            return potion
        elif type == 'hp':
            potion = cls(name=name, description='Health restored', value=50, effective_time=0, owner=owner)
            potion.ownership = owner
            return potion
        else:
            raise ValueError('Invalid potion type')
        
    def __str__(self):
        if self.rarity == 'legendary':
            return f'@@@ {self.name} @@@\nThe Legendary Potion!\nEffect: {self.description}\nRestores {self.value} points\nRarity: {self.rarity}'
        else:
            return f'{self.name} ({self.rarity}) - {self.description}'


class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item):
        if item.ownership is None:
            item.pick_up(self.owner)
        self.items.append(item)

    def remove_item(self, item: Item):
        if item in self.items:
            item.throw_away()
            self.items.remove(item)

    def view_item(self, item: Item):
        if item in self.items:
            return str(item)
        return 'Item not found in inventory.'

    def view_all(self):
        return [str(item) for item in self.items]

    def view_by_type(self, item_type: str):
        return [str(item) for item in self.items if isinstance(item, globals()[item_type])]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items


# Example usage
belthronding = Weapon(name='Belthronding', rarity='legendary', damage=5000, type='ranged')
print(belthronding.pick_up('Beleg'))  # Belthronding is now owned by Beleg
print(belthronding.equip())  # Belthronding is equipped by Beleg
print(belthronding.use())  # Belthronding shoots a powerful projectile from afar!, dealing 5750 damage
print(belthronding)  # Prints legendary weapon details

print()

long_bow = Weapon(name='Longbow', rarity='common', damage=200, type='ranged')
print(long_bow.pick_up('Beleg'))  # Longbow is now owned by Beleg
print(long_bow.equip())  # Longbow is equipped by Beleg
print(long_bow.use())  # Longbow shoots a powerful projectile from afar!, dealing 200 damage
print(long_bow)  # Prints common weapon details

print()

sword = Weapon(name='Sword', rarity='common', damage=150, type='single-handed')
print(sword.pick_up('Beleg'))  # Sword is now owned by Beleg
print(sword.equip())  # Sword is equipped by Beleg
print(sword.use())  # Sword performs a quick slash with precision!, dealing 150 damage
print(sword)  # Prints common weapon details

print()

two_handed_sword = Weapon(name='Great Sword', rarity='epic', damage=400, type='double-handed')
print(two_handed_sword.pick_up('Beleg'))  # Great Sword is now owned by Beleg
print(two_handed_sword.equip())  # Great Sword is equipped by Beleg
print(two_handed_sword.use())  # Great Sword spins wildly, striking in all directions!, dealing 460 damage
print(two_handed_sword)  # Prints epic weapon details

print()

pike = Weapon(name='Pike', rarity='uncommon', damage=300, type='pike')
print(pike.pick_up('Beleg'))  # Pike is now owned by Beleg
print(pike.equip())  # Pike is equipped by Beleg
print(pike.use())  # Pike thrusts forward with incredible force!, dealing 345 damage
print(pike)  # Prints uncommon weapon details

print()

# Type checking
print(isinstance(long_bow, Item))  # True
print(isinstance(sword, Weapon))  # True
print(isinstance(pike, Weapon))  # True

# Inventory testing
inventory = Inventory(owner="Beleg")

# Creating a shield object
shield = Shield(name="Wooden Shield", rarity="common", defense=50)
potion = Potion.from_ability(name="Health Potion", owner="Beleg", type="hp")

# Adding items to the inventory
inventory.add_item(sword)
inventory.add_item(long_bow)
inventory.add_item(pike)
inventory.add_item(shield)
inventory.add_item(potion)

# Viewing inventory
print(inventory.view_item(sword))  # Sword (common) with details
print(inventory.view_all())  # List of all items in the inventory
print(inventory.view_by_type("Weapon"))  # List of all weapon items in the inventory

# Checking membership
print(sword in inventory)  # True
print(potion in inventory)  # True

# Removing an item
inventory.remove_item(sword)
print(sword in inventory)  # False

