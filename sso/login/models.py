from djongo import models
from django import forms
# Create your models here.

class Info( models.Model):
    objects = models.DjongoManager()
    title = models.CharField(max_length=250)
    wantedAuthNo = models.CharField(max_length=250)
    wantedInfoUrl = models.CharField(max_length=250)
    wantedMobileInfoUrl = models.CharField(max_length=250)
    class Meta:
        abstract = True

class InfoForm(forms.ModelForm):
    class Meta:
        model= Info
        fields = (
            'title','wantedInfoUrl','wantedMobileInfoUrl','wantedAuthNo'
        )

class Certified(models.Model):
    objects=models.DjongoManager()
    ceNm=models.CharField(max_length=250)
    class Meta:
        abstract = True

class CertifiedForm(forms.ModelForm):
    class Meta:
        model = Certified
        fields = (
            'ceNm',
        )


class Companies(models.Model):
    objects=models.DjongoManager()
    busiNo = models.CharField(max_length=250)
    coNm = models.CharField(max_length=250)
    coAddr = models.CharField(max_length=250)
    superRegionCd = models.IntegerField()  # 지역코드 상
    superRegionNm = models.CharField(max_length=250)
    regionCd =models.IntegerField() # 지역코드 중
    regionNm = models.CharField(max_length=250)
    x = models.CharField(max_length=250)
    y = models.CharField(max_length=250)
    superIndTpCd = models.CharField(max_length=250) # 업종코드 상
    superIndTpNm = models.CharField(max_length=250)
    indTpCd = models.CharField(max_length=250)# 업종코드 중
    indTpNm = models.CharField(max_length=250)
    coMainProd = models.CharField(max_length=250)
    coHomePage = models.CharField(max_length=250)
    alwaysWorkerCnt = models.CharField(max_length=250)
    sgBrandNm = models.ArrayField(model_container=Certified,model_form_class=CertifiedForm)
    recruitment = models.BooleanField(default=False)
    info = models.ArrayField(model_container=Info,model_form_class=InfoForm)
    class Meta:
        db_table = u'Companies' 






class Favorate(models.Model):
    coId =models.IntegerField() #db에 저장된 기업 번호
    class Meta:
        abstract=True

class FavorateFrom(forms.ModelForm):
    class Meta:
        model=Favorate
        fields=(
            'coId',
        )

class User(models.Model):
    social_login_id=models.CharField(max_length=250)
    email=models.EmailField()
    platform = models.CharField(max_length=250,default=0)
    cofavorate = models.ArrayField(model_container=Favorate,model_form_class=FavorateFrom)
    class Meta:
        db_table = u'User'