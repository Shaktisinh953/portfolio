from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage, Project


class PortfolioViewsTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title='Task Desk', slug='task-desk', summary='A focused task app.', description='A project detail description.', features='Create tasks\nTrack progress', technologies='Python, Django')

    def test_homepage_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python.')

    def test_project_listing_and_detail_load(self):
        self.assertEqual(self.client.get(reverse('projects')).status_code, 200)
        response = self.client.get(self.project.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task Desk')

    def test_contact_form_validates_and_stores_message(self):
        response = self.client.post(reverse('contact'), {'name': 'Alex', 'email': 'alex@example.com', 'subject': 'Opportunity', 'message': 'I would like to discuss a software opportunity with you.'})
        self.assertRedirects(response, reverse('contact') + '#contact-form')
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_form_rejects_short_message(self):
        response = self.client.post(reverse('contact'), {'name': 'Alex', 'email': 'alex@example.com', 'subject': 'Hi', 'message': 'Too short'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please share a little more detail')
