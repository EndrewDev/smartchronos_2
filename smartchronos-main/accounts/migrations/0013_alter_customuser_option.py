# Generated by Django 5.1.4 on 2025-02-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_group_customuser_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='option',
            field=models.CharField(choices=[('FUNCIONARIO', 'Funcionário'), ('GERENTE', 'Gerente'), ('CHEFE', 'Chefe')], max_length=20),
        ),
    ]
