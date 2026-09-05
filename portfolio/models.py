from django.db import models
from django.urls import reverse


class Profile(models.Model):
    name = models.CharField(max_length=120, default='Your Name')
    headline = models.CharField(max_length=180, default='Software Developer')
    bio = models.TextField(default='I build clean, scalable and user-focused web applications with Python and Django.')
    objective = models.TextField(default='Seeking an opportunity to contribute as a software developer while growing through meaningful product work.')
    location = models.CharField(max_length=120, default='Open to remote and onsite opportunities')
    education = models.CharField(max_length=180, default='Add your degree and institution')
    availability = models.CharField(max_length=120, default='Open to opportunities')
    email = models.EmailField(default='hello@example.com')
    phone = models.CharField(max_length=30, blank=True)
    languages = models.CharField(max_length=180, blank=True, help_text='Comma-separated languages.')
    interests = models.CharField(max_length=240, blank=True, help_text='Comma-separated hobbies or interests.')
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [('Programming', 'Programming'), ('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Database', 'Database'), ('Tools', 'Tools')]
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    level = models.PositiveSmallIntegerField(default=70, help_text='Use an honest estimate from 1 to 100.')
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['category', 'sort_order', 'name']

    def __str__(self):
        return f'{self.name} ({self.category})'


class Project(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=220)
    description = models.TextField()
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    features = models.TextField(help_text='One feature per line.')
    technologies = models.CharField(max_length=250, help_text='Comma-separated technologies.')
    challenges = models.TextField(blank=True)
    learnings = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    sort_order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    @property
    def feature_list(self):
        return [item.strip() for item in self.features.splitlines() if item.strip()]

    @property
    def tech_list(self):
        return [item.strip() for item in self.technologies.split(',') if item.strip()]


class Certification(models.Model):
    name = models.CharField(max_length=180)
    organization = models.CharField(max_length=120)
    issued_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=120, blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['-issued_date', 'name']

    def __str__(self):
        return self.name


class Education(models.Model):
    qualification = models.CharField(max_length=180)
    institution = models.CharField(max_length=180)
    period = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', '-period']

    def __str__(self):
        return f'{self.qualification} - {self.institution}'


class Experience(models.Model):
    role = models.CharField(max_length=160)
    organization = models.CharField(max_length=180)
    period = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', '-period']

    def __str__(self):
        return f'{self.role} - {self.organization}'


class Achievement(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date', 'title']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} from {self.name}'