from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Contacts



# Create your tests here.
class ContactTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testemail@example.com',
            password = 'secret'
        )
        self.contacts = Contacts.objects.create(
            first_name='John',
            last_name = 'Doe',
            phone_number='01212121',
            email='johndoe@email.com',
            author = self.user
        )
    def test_string_representation(self):
        contact = Contacts(first_name='John')
        self.assertEqual(str(contact),contact.first_name)

    def test_contact_content(self):
        self.assertEqual(f'{self.contacts.first_name}','John')
        self.assertEqual(f'{self.contacts.last_name}','Doe')
        self.assertEqual(f'{self.contacts.phone_number}','01212121')
        self.assertEqual(f'{self.contacts.email}','johndoe@email.com')
    def test_contacts_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.user)
        self.assertContains(response,'John')
        self.assertContains(response,'01212121')
        self.assertTemplateUsed(response,'home.html')
    def test_contact_details_view(self):
        response = self.client.get('/contacts/1/')
        no_response = self.client.get('/contacts/100000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'John')
        self.assertContains(response, 'Doe')
        self.assertContains(response, '01212121')
        self.assertContains(response,'johndoe@email.com')