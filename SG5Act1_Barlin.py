class Hero:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack

  def take_damage(self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0

  def attack(self, damage):
    return self.attack

arthur = Hero("Arthur", 100, 15)
morgana = Hero("Morgana", 100, 10)


#Simulating Arthur taking 10 damage 
for i in range(1):
  arthur.take_damage(morgana.attack)
  print(f"Arthur's health after taking 10 damage: {arthur.health}")

# Showing both their HPs to see that Morgana is still at full health

print()

print("Hero's hp left:")
print(f"Arthur: {arthur.health}")
print(f"Morgana: {morgana.health}")





























