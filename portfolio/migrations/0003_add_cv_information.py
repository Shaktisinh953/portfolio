from django.db import migrations, models


def add_cv_information(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Education = apps.get_model('portfolio', 'Education')
    Experience = apps.get_model('portfolio', 'Experience')
    Project = apps.get_model('portfolio', 'Project')
    Skill = apps.get_model('portfolio', 'Skill')

    profile = Profile.objects.filter(email='hello@example.com').first() or Profile.objects.first()
    if profile:
        profile.name = 'Shaktisinh Parmar'
        profile.headline = 'Software Developer | Python Developer'
        profile.bio = 'Motivated and detail-oriented fresher with a foundation in programming, web development, databases and cybersecurity. I enjoy learning new technologies and turning ideas into useful software.'
        profile.objective = 'Seeking an entry-level software developer opportunity in a growth-oriented organization where I can apply my knowledge, learn new skills and contribute effectively to team goals.'
        profile.location = 'Ahmedabad, Gujarat'
        profile.education = 'B.E. Computer Science Engineering, Final Year'
        profile.availability = 'Open to entry-level opportunities'
        profile.email = 'parmarshakti336@gmail.com'
        profile.phone = '6355242808'
        profile.languages = 'Gujarati, Hindi, English'
        profile.interests = 'Reading, Sports, Learning new technologies'
        profile.save()

    Education.objects.update_or_create(
        qualification='B.E. Computer Science Engineering',
        defaults={'institution': 'SLTIET (GTU), Rajkot', 'period': 'Final year / 2027', 'description': 'Currently completing a Bachelor of Engineering in Computer Science Engineering.', 'sort_order': 1},
    )
    Education.objects.update_or_create(
        qualification='Diploma in Information Technology',
        defaults={'institution': 'Government Polytechnic College, Rajkot', 'period': 'Completed 2023', 'description': 'Diploma-level foundation in information technology and software development.', 'sort_order': 2},
    )

    Experience.objects.update_or_create(
        role='Web Developer Intern', organization='NSIC Technical Services Centre',
        defaults={'period': 'Aug - Sep 2022', 'description': 'Internship experience in web development. Add specific responsibilities and technologies through Admin when ready.', 'sort_order': 1},
    )
    Experience.objects.update_or_create(
        role='Cybersecurity Intern', organization='NSIC Technical Services Centre',
        defaults={'period': 'May - Jun 2023', 'description': 'Internship experience in cybersecurity. Add specific responsibilities and technologies through Admin when ready.', 'sort_order': 2},
    )

    Project.objects.update_or_create(
        slug='etrafficeye',
        defaults={
            'title': 'eTrafficEye',
            'summary': 'A team-built progressive web app concept for traffic monitoring.',
            'description': 'A team-built progressive web app concept designed around traffic monitoring and a clearer view of road activity.',
            'problem': 'Traffic monitoring needs timely, accessible information for people and teams making decisions on the move.',
            'solution': 'A responsive progressive web app concept that presents traffic information through a focused, mobile-friendly experience.',
            'features': 'Progressive web app concept\nTraffic monitoring\nResponsive interface\nTeam-built academic project',
            'technologies': 'Progressive Web App, JavaScript, HTML, CSS',
            'learnings': 'Team collaboration, responsive web design and turning a real-world problem into a practical product concept.',
            'is_featured': True,
            'sort_order': 0,
        },
    )

    for name, category, level in [
        ('Programming fundamentals', 'Programming', 70), ('Object-Oriented Programming', 'Programming', 64), ('Data Structures and Algorithms', 'Programming', 58),
        ('SQL and databases', 'Database', 64), ('Git / GitHub', 'Tools', 70), ('Debugging and problem solving', 'Tools', 74),
    ]:
        Skill.objects.update_or_create(name=name, category=category, defaults={'level': level})


def remove_cv_information(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Education = apps.get_model('portfolio', 'Education')
    Experience = apps.get_model('portfolio', 'Experience')
    Project = apps.get_model('portfolio', 'Project')
    Education.objects.filter(institution__in=['SLTIET (GTU), Rajkot', 'Government Polytechnic College, Rajkot']).delete()
    Experience.objects.filter(organization='NSIC Technical Services Centre').delete()
    Project.objects.filter(slug='etrafficeye').delete()
    profile = Profile.objects.filter(email='parmarshakti336@gmail.com').first()
    if profile:
        profile.delete()


class Migration(migrations.Migration):
    dependencies = [('portfolio', '0002_seed_portfolio_content')]
    operations = [
        migrations.AddField(model_name='profile', name='phone', field=models.CharField(blank=True, max_length=30)),
        migrations.AddField(model_name='profile', name='languages', field=models.CharField(blank=True, help_text='Comma-separated languages.', max_length=180)),
        migrations.AddField(model_name='profile', name='interests', field=models.CharField(blank=True, help_text='Comma-separated hobbies or interests.', max_length=240)),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=160)),
                ('organization', models.CharField(max_length=180)),
                ('period', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={'ordering': ['sort_order', '-period']},
        ),
        migrations.RunPython(add_cv_information, remove_cv_information),
    ]
