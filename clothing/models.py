from django.db import models

# Create your models here.
class ClothingItemCategory(models.Model):
    description=models.CharField(max_length=64)
    parent=models.IntegerField(blank=True, null=True)

class ClothingItem(models.Model):
    name=models.CharField(max_length=64)
    remaining_tolerance=models.IntegerField(default=0)
    tolerance=models.IntegerField()
    category=models.ForeignKey(ClothingItemCategory, on_delete=models.CASCADE, default=0)

    def json(self):
        return dict(
            name=self.name,
            remaining_tolerance = self.remaining_tolerance,
            tolerance=self.tolerance,
            category=self.category.description
        )
