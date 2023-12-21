# class File:
#     className = 'File'
#     objectsCount = 0

#     def __init__(self, name, kbs, type):
#         self._name = name
#         self._kbs = kbs
#         self._type = type
#         File.objectsCount = File.objectsCount + 1

#     def get_name(self):
#         return self._name

#     def set_name(self, n):
#         self._name = n

#     def get_kbs(self):
#         return self._kbs

#     def set_kbs(self, kbs):
#         if kbs > 0:
#             self._kbs = kbs
#         else:
#             self._kbs = 0.1

#     def type(self):
#         return self._type

#     def info(self):
#         print(self._name)
#         print(f"Размер: {self._kbs} кб")
#         print(f'Формат: {self._type}')

#     def kbsToBytes(self):
#         print(f'Размер в байтах: {self._kbs * 1024}')


# class Image(File):
#     className = 'Image'

#     def __init__(self, name, kbs, type, height, width):
#         super().__init__(name, kbs, type)
#         self.height = height
#         self.width = width

#     def set_height(self, height):
#         if height > 0:
#             self.height = height
#         else:
#             self.height = 1

#     def set_width(self, width):
#         if width > 0:
#             self.width = width
#         else:
#             self.width = 1

#     def info(self):
#         super().info()
#         print(f'Тип: {Image.className}')
#         print(f"Высота (пкс): {self.height}")
#         print(f'Ширина (пкс): {self.width}')

#     def amount(self):
#         print(f'Площадь в пикселях: {self.height * self.width}')

#     def __eq__(self, other):
#         return self.height == other.height and self.width == other.width


# b = File("Объект класса " + File.className, 11, 'TXT')
# b.info()
# b.kbsToBytes()

# print('\n')

# im = Image('background.jpg', 44.1, 'JPG', 800, 600)
# im2 = Image('new_background.jpg', 42.8, 'JPG', 800, 600)

# im.amount()
# im.kbsToBytes()

# if (im == im2) is True:
#     print(f'{im.get_name()} и {im2.get_name()} равны.')
# else:
#     print(f'{im.get_name()} и {im2.get_name()} не равны.')

# print(f'Objects count: {File.objectsCount}')

class Firearms:
    def __init__(self, ammo_count, rate_of_fire, shooting_range):
        self.ammo_count = ammo_count
        self.rate_of_fire = rate_of_fire
        self.shooting_range = shooting_range

    def empty_magazine_time(self):
        if self.rate_of_fire <= 0:
            return "Cannot calculate time for a non-positive rate of fire."
        else:
            time_to_empty = self.ammo_count / self.rate_of_fire
            return f"Magazine will be empty in {time_to_empty:.2f} seconds."


class AssaultRifle(Firearms):
    def __init__(self, ammo_count, rate_of_fire, shooting_range, automatic_mode):
        super().__init__(ammo_count, rate_of_fire, shooting_range)
        self.automatic_mode = automatic_mode

    def fire_rate_to_range_ratio(self):
        if self.shooting_range <= 0:
            return "Cannot calculate ratio for non-positive shooting range."
        else:
            ratio = self.rate_of_fire / self.shooting_range
            return f"Ratio of fire rate to shooting range: {ratio:.5f}"


class SniperRifle(Firearms):
    def __init__(self, ammo_count, rate_of_fire, shooting_range, scope_magnification):
        super().__init__(ammo_count, rate_of_fire, shooting_range)
        self.scope_magnification = scope_magnification

    def fire_rate_to_range_ratio(self):
        if self.shooting_range <= 0:
            return "Cannot calculate ratio for non-positive shooting range."
        else:
            ratio = self.rate_of_fire / self.shooting_range
            return f"Ratio of fire rate to shooting range: {ratio:.2f}"


# Example usage
assault_rifle = AssaultRifle(ammo_count=30, rate_of_fire=600, shooting_range=300, automatic_mode=True)
print(assault_rifle.empty_magazine_time())
print(assault_rifle.fire_rate_to_range_ratio())

sniper_rifle = SniperRifle(ammo_count=5, rate_of_fire=60, shooting_range=1000, scope_magnification=10)
print(sniper_rifle.empty_magazine_time())
print(sniper_rifle.fire_rate_to_range_ratio())
