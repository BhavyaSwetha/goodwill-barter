# Generated by Django 3.1.7 on 2021-04-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product category (e.g. Electronics)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Random Product Name', max_length=100),
            preserve_default=False,
        ),
    ]