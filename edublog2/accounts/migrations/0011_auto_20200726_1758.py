# Generated by Django 3.0.3 on 2020-07-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200726_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, default='accounts/img/default_profile.png', upload_to='images/'),
        ),
    ]