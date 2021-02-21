from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название категории")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Родительская категория")

    def __str__(self):
        return self.name if not self.parent else "{} -> {}".format(self.parent.name, self.name)


class Region(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название региона")

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return "{}".format(self.name)


class ItemImage(models.Model):
    image = models.ImageField(upload_to='media/images/%Y/%m/%d', verbose_name="Изображение")
    item = models.ForeignKey("item.Item", on_delete=models.CASCADE, verbose_name="Связанный товар")

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'


class Item(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Наименование")
    comment = models.TextField(null=True, blank=True,verbose_name="Комментарий")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    material = models.TextField(null=True, blank=True, verbose_name="Материал")
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Регион")
    price_buy = models.DecimalField(null=True, blank=True, max_digits=10000000, decimal_places=2, verbose_name="Цена закупочная")
    price_sell = models.DecimalField(null=True, blank=True, max_digits=10000000, decimal_places=2, verbose_name="Цена продажи")
    count = models.IntegerField(default=1, verbose_name="Количество")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def articul(self):
        return str(self.created.strftime('%d%m%Y')) + "05{0:06d}".format(self.id)
