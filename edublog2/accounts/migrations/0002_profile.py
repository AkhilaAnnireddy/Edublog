# Generated by Django 3.0.3 on 2020-07-25 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_facebook', models.URLField(blank=True, null=True)),
                ('contact_linkedin', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='accounts/img/default_profile.png', upload_to='../accounts/img')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Faculty')),
            ],
        ),
    ]