from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    file_name = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    SCOPE_CHOICES = [
        ('SCOPE_1', 'Scope 1'),
        ('SCOPE_2', 'Scope 2'),
        ('SCOPE_3', 'Scope 3'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    activity_type = models.CharField(max_length=255)

    quantity = models.FloatField()

    unit = models.CharField(max_length=50)

    normalized_quantity = models.FloatField(
        null=True,
        blank=True
    )

    normalized_unit = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    record_date = models.DateField()

    is_suspicious = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    analyst_notes = models.TextField(
    blank=True,
    null=True
)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type