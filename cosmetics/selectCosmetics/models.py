from django.db import models


class Ages(models.Model):
    limits = models.CharField(max_length=200)

    def __str__(self):
        return self.limits

class Brands(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Prices(models.Model):
    limits = models.CharField(max_length=200)

    def __str__(self):
        return self.limits

class Types(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cosmetics(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    price = models.ForeignKey(Prices, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description + "/" + str(self.brand) + "/" + str(self.type) + "/" + str(self.price)

class Preferences(models.Model):
    age = models.ForeignKey(Ages, on_delete=models.CASCADE)
    cosmetics = models.ForeignKey(Cosmetics, on_delete=models.CASCADE)

    def __str__(self):
        return 'Boys at ' + str(self.age) + ' prefer ' + str(self.cosmetics)