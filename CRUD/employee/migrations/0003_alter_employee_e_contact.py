# Generated by Django 4.0.4 on 2022-06-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_e_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_contact',
            field=models.CharField(max_length=10),
        ),
    ]