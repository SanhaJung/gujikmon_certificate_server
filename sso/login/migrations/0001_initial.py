# Generated by Django 3.0.5 on 2021-04-14 07:40

from django.db import migrations, models
import djongo.models.fields
import login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_login_id', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('platform', models.CharField(default=0, max_length=250)),
                ('cofavorate', djongo.models.fields.ArrayField(model_container=login.models.Favorate, model_form_class=login.models.FavorateFrom)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
