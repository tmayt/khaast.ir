# Generated by Django 5.2.3 on 2025-06-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('a', 'عمومی'), ('b', 'اضطراری'), ('c', 'اخبار'), ('d', 'نقدی'), ('e', 'سکونت')], default='a', max_length=1),
        ),
    ]
