# Generated by Django 4.2.4 on 2024-08-07 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
