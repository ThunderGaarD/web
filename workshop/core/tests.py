from django.test import TestCase


class HomeTest(TestCase):


    def setUp(self):
        self.response = self.client.get('/')


    def test_get(self):
        self.assertEqual(200, self.response.status_code)


    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/index.html')


    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/subscription/"')


    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')


    def test_speakers_link(self):
        self.assertContains(self.response, 'href="/speakers/"')


    def test_events_link(self):
        self.assertContains(self.response, 'href="/events/"')


    def test_contact_link(self):
        self.assertContains(self.response, 'href="/contact/"')


class AboutTest(TestCase):


    def setUp(self):
        self.response = self.client.get('/about/')


    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/about.html')



