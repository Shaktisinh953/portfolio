from django.db import migrations


def update_role(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Profile.objects.filter(name='Shaktisinh Parmar').update(headline='Software Developer | Python Developer')


def restore_role(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Profile.objects.filter(name='Shaktisinh Parmar').update(headline='Fresher Software Developer | Python Developer')


class Migration(migrations.Migration):
    dependencies = [('portfolio', '0003_add_cv_information')]
    operations = [migrations.RunPython(update_role, restore_role)]
