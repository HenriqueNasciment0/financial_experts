from django.db import models
from profiles.models import CompanyProfile, ExpertProfile


class Review(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    expert = models.ForeignKey(ExpertProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
