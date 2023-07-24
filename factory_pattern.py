#  Factory pattern realization


class Weapon:
    def shoot(self):
        pass


class Shotgun(Weapon):
    def shoot(self):
        return "Shotgun is shooting"


class Artillery(Weapon):
    def shoot(self):
        return "Artillery is shooting"


class WeaponFactory:
    def create_weapon(self, weapon_type):
        if weapon_type == "shotgun":
            return Shotgun()
        elif weapon_type == "artillery":
            return Artillery()
        else:
            raise ValueError("Invalid weapon type.")


#  Client code
factory = WeaponFactory()

shotgun = factory.create_weapon("shotgun")
print(shotgun.shoot())

artillery = factory.create_weapon("artillery")
print(artillery.shoot())
