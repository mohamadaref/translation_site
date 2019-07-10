# Generated by Django 2.2.3 on 2019-07-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190710_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='First_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Last_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Password',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='User_name',
            field=models.CharField(default='', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='Card_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='First_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='Last_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='Password',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='translator',
            name='User_name',
            field=models.CharField(default='', max_length=30, null=True, unique=True),
        ),
    ]