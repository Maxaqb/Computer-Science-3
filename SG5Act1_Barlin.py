
# Defining the main class, attributes, and methods
class Hero:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack

  def take_damage(self, damage):
    self.health -= damage


# Defining the heros
arthur = Hero("Arthur", 100, 15)
morgana = Hero("Morgana", 100, 10)


# Simulating Arthur taking 10 damage 
for i in range(1):
  arthur.take_damage(morgana.attack)
  print(f"Arthur's health after taking 10 damage: {arthur.health}")

# Print both their HPs to see that Morgana is still at full health
print()
print("Hero's health left:")
print(f"Arthur's Health: {arthur.health}")
print(f"Morgana's Health: {morgana.health}")
print()

# Check if anyone is at full health
if arthur.health == 100:
  print("Arthur is at full health!")
if morgana.health == 100:
  print("Morgana is at full health!")
  
