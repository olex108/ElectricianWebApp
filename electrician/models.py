# from django.db import models
#
#
# class Projects(models.Model):
#
#     APARTMENT = "apartment"
#     HOUSE = "house"
#     ROOM = "room"
#     KITCHEN = "kitchen"
#     COMMERCE = "commerce"
#
#     PROJECT_TYPE_CHOICES = [
#         (APARTMENT, "квартира"),
#         (HOUSE, "дом"),
#         (ROOM, "комната"),
#         (KITCHEN, "кухня"),
#         (COMMERCE, "коммерческое"),
#     ]
#
#     name = models.CharField(max_length=150, verbose_name="Project name")
#     address = models.CharField(
#         max_length=250, verbose_name="Address", help_text="Введите точный адрес и/или станцию метро"
#     )
#     square = models.FloatField(verbose_name="Square", help_text="Внесите площадь по проведению работ")
#     type = models.CharField(
#         max_length=15, choices=PROJECT_TYPE_CHOICES, default=APARTMENT, verbose_name="Project type"
#     )
#     created_at = models.DateField(auto_now_add=True)
#     update_at = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.name} - {self.type} - {self.square}"
#
#     class Meta:
#         verbose_name = "Проект"
#         verbose_name_plural = "Проекты"
#         ordering = ["last_name"]
#
#
# class ProjectParams(models.Model):
#
#     project = models.OneToOneField(Projects, on_delete=models.CASCADE, related_name="Params")
#     room_quantity = models.IntegerField(
#         verbose_name="Количество комнат", help_text="Указать с учетом кухни и учетом ванных комнат"
#     )
#
#     WALLS_MATERIAL_CHOICES = [("BRUTAL", "Бетон"), ("SOFT BLOCKS", "Газоблок"), ("DRYWALL", "Гипсокартон")]
#
#     walls_material = models.CharField(
#         max_length=12,
#         choices=WALLS_MATERIAL_CHOICES,
#         default="BRUTAL",
#         help_text="Укажите основной материал несущих стен",
#     )
#
#     PARTITIONS_MATERIAL_CHOICES = [("BRUTAL", "Бетон"), ("SOFT BLOCKS", "Газоблок"), ("DRYWALL", "Гипсокартон")]
#
#     partitions_material = models.CharField(
#         max_length=12,
#         choices=PARTITIONS_MATERIAL_CHOICES,
#         default="BRUTAL",
#         help_text="Укажите основной материал перегородок помещений",
#     )
#
#     is_suspended_ceiling = models.BooleanField(
#         default=True, verbose_name="Подвесные потолки", help_text="Укажите да если подвесные потолки"
#     )
#     sockets = models.IntegerField(verbose_name="Подрозетники", help_text="Указать розетки по количеству отверстий")
#     switches = models.IntegerField(verbose_name="Выключатели", help_text="Указать количество отдельных клавиш")
#     communication_sockets = models.IntegerField(
#         verbose_name="Слаботочные розетки", help_text="Укажите количество интернет и ТВ розеток"
#     )
#     light = models.IntegerField(
#         verbose_name="Осветительные приборы", help_text="Светильники, группа точечных светильников, бра, подсветки"
#     )
#     is_built_in_shield = models.BooleanField(default=False, verbose_name="Щит", help_text="Щит встроенный / навесной ")
#     is_power_cable = models.BooleanField(
#         default=False, verbose_name="Вводной кабель", help_text="Нужна замена вводного кабеля Да/нет"
#     )
#     is_dishwasher = models.BooleanField(default=False, verbose_name="Посудомойка", help_text="Посудомойка Да/нет")
#     is_boiler = models.BooleanField(default=False, verbose_name="Бойлер", help_text="Бойлер Да/нет")
#     is_washing_machine = models.BooleanField(
#         default=False, verbose_name="Стиральная машина", help_text="Стиральная машина Да/нет"
#     )
#     is_el_plate = models.BooleanField(default=False, verbose_name="Электроплита", help_text="Электроплита Да/нет")
#     is_water_heater = models.BooleanField(
#         default=False, verbose_name="Водонагреватель", help_text="Проточный водонагреватель Да/нет"
#     )
#     is_oven = models.BooleanField(default=False, verbose_name="Духовой шкаф", help_text="Духовой шкаф Да/нет")
#     other_electric_appliance = models.BooleanField(
#         default=0, verbose_name="Электроприборы", help_text="Укажите количество не перечисленных электроприборов"
#     )
