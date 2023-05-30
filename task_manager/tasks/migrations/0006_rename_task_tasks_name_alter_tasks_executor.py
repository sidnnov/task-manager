# Generated by Django 4.2.1 on 2023-05-30 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0005_rename_label_labelfortask_labels_remove_tasks_label_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tasks",
            old_name="task",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="tasks",
            name="executor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executor",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Executor",
            ),
        ),
    ]
