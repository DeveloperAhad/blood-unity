from django.db import models

# Create your models here.
class Post(models.Model):
    POST_TYPE = (
        ('blood_request', 'Blood Request'),
        ('blood_donation', 'Blood Donation'),
        ('news', 'News'),
    )

    class BloodGroup(models.TextChoices):
        A_POSITIVE = 'A+', 'A+'
        A_NEGATIVE = 'A-', 'A-'
        B_POSITIVE = 'B+', 'B+'
        B_NEGATIVE = 'B-', 'B-'
        O_POSITIVE = 'O+', 'O+'
        O_NEGATIVE = 'O-', 'O-'
        AB_POSITIVE = 'AB+', 'AB+'
        AB_NEGATIVE = 'AB-', 'AB-'

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('authentication.Account', on_delete=models.CASCADE)

    blood_group = models.CharField(max_length=3, choices=BloodGroup.choices, null=True, blank=True)

    division = models.ForeignKey('locations.Division', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey('locations.District', on_delete=models.SET_NULL, null=True, blank=True)
    upazila = models.ForeignKey('locations.Upazila', on_delete=models.SET_NULL, null=True, blank=True)
    union = models.ForeignKey('locations.Union', on_delete=models.SET_NULL, null=True, blank=True)

    post_type = models.CharField(max_length=20, choices=POST_TYPE, default='blood_request')

    def __str__(self):
        return self.title
