from django.db import models


# Create your models here.
class FamilyMember(models.Model):
    ADULT = "ADULT"
    CHILD = "CHILD"
    MEMBER_TYPE_CHOICES = [
        (ADULT, "Adult"),
        (CHILD, "Child"),
    ]
    member_type = models.CharField(
        max_length=5, choices=MEMBER_TYPE_CHOICES, default=CHILD
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(
        default=f"{first_name} {last_name}", unique=True, max_length=100
    )
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Chore(models.Model):
    FREQUENCY_CHOICES = [
        ("DAILY", "Daily"),
        ("EVERY_OTHER_DAY", "Every Other Day"),
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
        ("ANNUALLY", "Annually"),
        ("CUSTOM", "Custom"),
    ]

    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    ]

    title = models.CharField(max_length=150)
    frequency = models.CharField(
        max_length=100, choices=FREQUENCY_CHOICES, default="WEEKLY"
    )
    assignee = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(
        max_length=100, choices=PRIORITY_CHOICES, default="MEDIUM"
    )
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    estimated_time = models.IntegerField(
        help_text="Estimated time in minutes", blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
