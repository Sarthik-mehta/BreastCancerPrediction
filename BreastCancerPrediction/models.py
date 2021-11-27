from django.db import models
from django.conf import settings


class userData(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    radiusMean = models.DecimalField(max_digits=10, decimal_places=2)
    textureMean = models.DecimalField(max_digits=10, decimal_places=2)
    perimeterMean = models.DecimalField(max_digits=10, decimal_places=2)
    areaMean = models.DecimalField(max_digits=10, decimal_places=2)
    smoothnessMean = models.DecimalField(max_digits=10, decimal_places=2)
    compactnessMean = models.DecimalField(max_digits=10, decimal_places=2)
    concavityMean = models.DecimalField(max_digits=10, decimal_places=2)
    concavePointMean = models.DecimalField(max_digits=10, decimal_places=2)
    symmetryMean = models.DecimalField(max_digits=10, decimal_places=2)
    fractalDimensionMean = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username
