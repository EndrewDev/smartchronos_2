# Generated by Django 5.1.4 on 2025-02-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_usergroup_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='option',
            field=models.CharField(choices=[('FUNCIONARIO', 'funcionário'), ('GERENTE', 'gerente'), ('CHEFE', 'Chefe')], default='FUNCIONARIO', max_length=20),
        ),
    ]
