# Generated by Django 5.0.4 on 2024-04-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                default=2, upload_to="categories/", verbose_name="Изображение"
            ),
            preserve_default=False,
        ),
    ]