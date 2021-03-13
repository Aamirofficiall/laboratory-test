from django.test import TestCase

import unittest

from unittest import TestCase
from faker import Factory
from .models import UserProfile,Report

from .factories import UserFactory,ReportFactory,UserProfileFactory

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase



faker = Factory.create()

class ShowLostReportTests(APITestCase):
    url = reverse("show_my_lost-list")

    def setUp(self):
    	self.admin = UserFactory(is_superuser=True)
    	self.user = UserFactory()
    	self.report = ReportFactory(reporter_user_id=self.user)

    
    #check if all 5  lost reports made by a single user
    def test_one_user_lost_report(self):
        reports = ReportFactory.create_batch(5, reporter_user_id=self.user)
        #print(reports)
        #print(self.user)
        self.client.force_login(self.user, backend=None)
        response = self.client.get(self.url)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for report in reports:
        	self.assertContains(response, report.reporter_user_id.id)
        	self.assertEqual(response.data[0]['reporter_user_id'], report.reporter_user_id.id)

    #check if lost report shown is for the user logged in and not for the other user
    def test_many_user_lost_report(self):
    	another_user = UserFactory()
    	user1_report = ReportFactory(reporter_user_id=self.user)
    	user2_report = ReportFactory(reporter_user_id=another_user)
    	self.client.force_login(self.user, backend=None)
    	response = self.client.get(self.url)
    	#print(response.data[0]['reporter_user_id'])
    	#json_string = json.dumps(response.data)
    	#print(json_string)
    	self.assertEqual(200, response.status_code)
    	self.assertEqual(response.data[0]['reporter_user_id'], user1_report.reporter_user_id.id)
    	self.assertNotEqual(response.data[0]['reporter_user_id'], user2_report.reporter_user_id.id)



class ShowFoundReportTests(APITestCase):
    url = reverse("show_my_found-list")

    def setUp(self):
    	self.admin = UserFactory(is_superuser=True)
    	self.user = UserFactory()
    	self.report = ReportFactory(reporter_user_id=self.user)

    
    #check if all 5  found reports made by a single user
    def test_one_user_lost_report(self):
        reports = ReportFactory.create_batch(5, reporter_user_id=self.user)
        #print(reports)
        #print(self.user)
        self.client.force_login(self.user, backend=None)
        response = self.client.get(self.url)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for report in reports:
        	self.assertContains(response, report.reporter_user_id.id)
        	self.assertEqual(response.data[0]['reporter_user_id'], report.reporter_user_id.id)

    #check if lost found shown is for the user logged in and not for the other user
    def test_many_user_lost_report(self):
    	another_user = UserFactory()
    	user1_report = ReportFactory(reporter_user_id=self.user)
    	user2_report = ReportFactory(reporter_user_id=another_user)
    	self.client.force_login(self.user, backend=None)
    	response = self.client.get(self.url)
    	#print(response.data[0]['reporter_user_id'])
    	#json_string = json.dumps(response.data)
    	#print(json_string)
    	self.assertEqual(200, response.status_code)
    	self.assertEqual(response.data[0]['reporter_user_id'], user1_report.reporter_user_id.id)
    	self.assertNotEqual(response.data[0]['reporter_user_id'], user2_report.reporter_user_id.id)


class RegistrationTestCase(APITestCase):
	url = reverse("signup-list")
	
	def setUp(self):
		self.user = UserFactory()
	
	def test_registration(self):
		user_profile=UserProfileFactory(user=self.user)
		response = self.client.post('/signup/',{"name":user_profile.user.name, "email": "neww@gmail.com","password":user_profile.user.password,"profile":{"bio":user_profile.bio,"gender":user_profile.gender}},format='json')
		
		#print(response.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
