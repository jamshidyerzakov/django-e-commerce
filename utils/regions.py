from django.db import models


class TashkentRegions(models.TextChoices):
    BEKTEMIR = 'Bektemir'
    CHILANZAR = 'Chilanzar'
    YASHNOBOD = 'Yashnobod'
    MIROBOD = 'Mirobod'
    MIRZO_ULUGBEK = 'Mirzo Ulugbek'
    SERGELI = 'Sergeli'
    SHAYKHONTOHUR = 'Shaykhontohur'
    OLMAZOR = 'Olmazor'
    UCHTEPA = 'Uchtepa'
    YAKKASAROY = 'Yakkasaroy'
    YUNUSABAD = 'Yunusabad'
