from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Character(models.Model):
    name = models.CharField("Имя", max_length=100)
    race = models.CharField("Раса", max_length=50)
    character_class = models.CharField("Класс", max_length=50)
    level = models.PositiveIntegerField("Уровень", default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])

    # Основные атрибуты
    strength = models.PositiveIntegerField("Сила (STR)", default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dexterity = models.PositiveIntegerField("Ловкость (DEX)", default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    constitution = models.PositiveIntegerField("Телосложение (CON)", default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    intelligence = models.PositiveIntegerField("Интеллект (INT)", default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    wisdom = models.PositiveIntegerField("Мудрость (WIS)", default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    charisma = models.PositiveIntegerField("Харизма (CHA)", default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])

    def __str__(self):
        return self.name
