from django.db import migrations


def seed_content(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    profile = Profile.objects.create(
        name='Your Name',
        headline='Fresher Software Developer',
        bio='I build clean, scalable and user-focused web applications using Python, Django and modern web technologies.',
        objective='Seeking an opportunity to contribute as a software developer while growing through meaningful product work.',
        location='Open to remote and onsite opportunities',
        education='Add your degree and institution',
        availability='Open to opportunities',
        email='hello@example.com',
    )
    skills = [
        ('Python', 'Programming', 78), ('JavaScript', 'Programming', 62),
        ('Django', 'Backend', 76), ('Flask', 'Backend', 60), ('REST API', 'Backend', 68),
        ('HTML5', 'Frontend', 82), ('CSS3', 'Frontend', 76), ('Bootstrap / Tailwind', 'Frontend', 64),
        ('MySQL', 'Database', 65), ('SQLite', 'Database', 76),
        ('Git', 'Tools', 72), ('GitHub', 'Tools', 74), ('VS Code', 'Tools', 86), ('Postman', 'Tools', 65),
    ]
    Skill.objects.bulk_create([Skill(name=name, category=category, level=level, sort_order=index) for index, (name, category, level) in enumerate(skills)])
    projects = [
        ('Python / Django ERP System', 'A planned operations platform for managing people, customers and reports.', 'An editable project placeholder. Replace this with the problem your project actually solves.', 'Python, Django, MySQL', 'Authentication\nDashboard\nEmployee and customer CRUD\nReports'),
        ('Real Estate CRM', 'A planned CRM concept for keeping leads, properties and follow-ups organized.', 'An editable project placeholder for a customer relationship workflow.', 'Python, Django, REST API', 'Lead management\nProperty management\nFollow-up tracking\nDashboard'),
        ('Task Management System', 'A focused workspace for turning priorities into visible progress.', 'An editable project placeholder for a task tracking application.', 'Django, SQLite, JavaScript', 'Authentication\nTask status and priority\nCreate, update and delete tasks\nDashboard'),
    ]
    Project.objects.bulk_create([Project(title=title, slug=title.lower().replace(' / ', '-').replace(' ', '-'), summary=summary, description=description, technologies=technologies, features=features, sort_order=index + 1) for index, (title, summary, description, technologies, features) in enumerate(projects)])


def remove_content(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Profile.objects.filter(name='Your Name').delete()
    Skill.objects.all().delete()
    Project.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [('portfolio', '0001_initial')]
    operations = [migrations.RunPython(seed_content, remove_content)]
