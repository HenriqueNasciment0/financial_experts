from django.db import models
from profiles.models import CompanyProfile, ExpertProfile


class QuoteRequest(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    expert = models.ForeignKey(ExpertProfile, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=50, default="Pendente")
    created_at = models.DateTimeField(auto_now_add=True)
