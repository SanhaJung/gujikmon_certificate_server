from djongo import models
from django import forms
# Create your models here.
class Favorate(models.Model):
    busiNo =models.CharField(max_length=250) #db에 저장된 기업 번호
    coNm = models.CharField(max_length=250) #기업이름
    class Meta:
        abstract=True

class FavorateFrom(forms.ModelForm):
    class Meta:
        model=Favorate
        fields=(
            'busiNo','coNm'
        )

class User(models.Model):
    social_login_id=models.CharField(max_length=250)
    email=models.EmailField()
    platform = models.CharField(max_length=250,default=0)
    cofavorate = models.ArrayField(model_container=Favorate,model_form_class=FavorateFrom)
    class Meta:
        db_table = u'User'