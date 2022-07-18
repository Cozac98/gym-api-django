# Generated by Django 4.0.6 on 2022-07-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0001_initial'),
        ('routine_day', '0002_routineday_exercises'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routineday',
            name='exercises',
        ),
        migrations.AlterField(
            model_name='routineday',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routine_days', to='routines.routine'),
        ),
    ]
