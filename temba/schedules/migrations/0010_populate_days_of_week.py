# Generated by Django 2.2.4 on 2019-08-22 18:32

from django.db import migrations


def noop(apps, schema_editor):
    pass


def populate_days_of_week(apps, schema_editor):  # pragma: no cover
    Schedule = apps.get_model("schedules", "Schedule")
    WEEKDAYS = "MTWRFSU"
    updated = 0

    for s in Schedule.objects.filter(repeat_period="W"):
        if s.repeat_days:
            repeat_days_of_week = ""

            bitmask_number = bin(s.repeat_days)
            for idx in range(7):
                power = bin(pow(2, idx + 1))
                if bin(int(bitmask_number, 2) & int(power, 2)) == power:
                    repeat_days_of_week += WEEKDAYS[idx]

            s.repeat_days_of_week = repeat_days_of_week
            s.save(update_fields=["repeat_days_of_week"])

            updated += 1

    if updated > 0:
        print(f"updated {updated} weekly schedules")


class Migration(migrations.Migration):

    dependencies = [("schedules", "0009_auto_20190822_1823")]

    operations = [migrations.RunPython(populate_days_of_week, noop)]
