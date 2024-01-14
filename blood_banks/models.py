from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.gis.db import models as geoModels

user = get_user_model()


# Create your models here.
class BloodBank(models.Model):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    division = models.ForeignKey('locations.Division', on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey('locations.District', on_delete=models.SET_NULL, null=True)
    upazila = models.ForeignKey('locations.Upazila', on_delete=models.SET_NULL, null=True)
    union = models.ForeignKey('locations.Union', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    blood_group_a_positive = models.IntegerField(default=0)
    blood_group_a_negative = models.IntegerField(default=0)
    blood_group_b_positive = models.IntegerField(default=0)
    blood_group_b_negative = models.IntegerField(default=0)
    blood_group_o_positive = models.IntegerField(default=0)
    blood_group_o_negative = models.IntegerField(default=0)
    blood_group_ab_positive = models.IntegerField(default=0)
    blood_group_ab_negative = models.IntegerField(default=0)
    location_point = geoModels.PointField(null=True, blank=True)

    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    @property
    def get_address(self):
        return f"{self.union}, {self.upazila}, {self.district}, {self.division}"
