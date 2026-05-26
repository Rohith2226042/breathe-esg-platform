from django.db import models


class Organization(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    scope = models.CharField(
        max_length=50,
        default='SCOPE_1'
    )

    activity_type = models.CharField(
        max_length=255
    )

    quantity = models.FloatField()

    unit = models.CharField(
        max_length=50,
        default='Liters'
    )

    normalized_quantity = models.FloatField(
        default=0
    )

    normalized_unit = models.CharField(
        max_length=50,
        default='Liters'
    )

    record_date = models.DateField(
        null=True,
        blank=True
    )

    is_suspicious = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    analyst_notes = models.TextField(
        blank=True,
        null=True
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.activity_type