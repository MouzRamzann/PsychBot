# Generated by Django 4.1.7 on 2023-03-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot_app", "0009_alter_doc_timing_timing"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_appointment",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user_appointment",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
