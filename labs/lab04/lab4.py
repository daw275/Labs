class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.ownership = ''

    def pick_up(self, character: str) -> str:
        self.ownership = character
        return f'{self.name} is now owned by {character}'
    
    def throw_away(self) -> str:
        self.ownership = ''
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
            attack_power = self.damage * self.attack_modifier
            return f'{self.name} is used, dealing {attack_power} damage'
        else:
            return f'{self.name} has no owner and cannot be used'
        
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
        return f'{self.name} ({self.rarity}) - {self.description}'
    
# Example usage
belthronding = Weapon(name='Belthronding', rarity='legendary', damage=5000, type='bow')
print(belthronding.pick_up('Beleg'))  # Belthronding is now owned by Beleg
print(belthronding.equip())  # Belthronding is equipped by Beleg
print(belthronding.use())  # Belthronding is used, dealing 5750 damage

print() 

long_bow = Weapon(name='Longbow', rarity='common', damage=200, type='bow')
print(long_bow.pick_up('Beleg'))  # Longbow is now owned by Beleg
print(long_bow.equip())  # Longbow is equipped by Beleg
print(long_bow.use())  # Longbow is used, dealing 200 damage

print()  

broken_pot_lid = Shield(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense=5, broken=True)
print(broken_pot_lid.pick_up('Beleg'))  # wooden lid is now owned by Beleg
print(broken_pot_lid.equip())  # wooden lid is equipped by Beleg
print(broken_pot_lid.use())  # wooden lid is used, blocking 2.5 damage
print(broken_pot_lid.throw_away())  # wooden lid is thrown away
print(broken_pot_lid.use())  # NO OUTPUT

print()  # Blank line between outputs

# Correctly using the class method from_ability
attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', type='attack')
print(attack_potion.use())  # Beleg used atk potion temp, and attack increase 50 for 30s
print(attack_potion.use())  # NO OUTPUT

print()  # Blank line between outputs

# Type checking
print(isinstance(long_bow, Item))  # True
print(isinstance(broken_pot_lid, Shield))  # True
print(isinstance(attack_potion, Weapon))  # False