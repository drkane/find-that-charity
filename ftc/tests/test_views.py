from django.urls import reverse

from ftc.tests import TestCase


class OrganisationViewTests(TestCase):

    def test_organisation(self):

        response = self.client.get(reverse('orgid_html', kwargs={'org_id': 'XX-XXX-1234'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Find that Charity", html=True)
        self.assertContains(response, "Source publisher", html=True)
        self.assertContains(response, "Registered Charity", html=True)
        self.assertContains(response, "Test organisation", html=True)
        self.assertContains(response, "Test description", html=True)
