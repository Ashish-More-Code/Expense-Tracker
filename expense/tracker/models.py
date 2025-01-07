from django.db import models
from django.contrib.auth.models import User
import uuid



class BaseModel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True

class  Transaction(BaseModel):
    description=models.CharField(max_length=100)
    amount=models.FloatField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering=('amount',)
        db_table ="transaction"

    def isNegative(self):
        return self.amount <0 

