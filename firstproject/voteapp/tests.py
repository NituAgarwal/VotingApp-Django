from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from voteapp.models import Question
from django.utils import timezone



class QuestionMethodTests(TestCase):

	def test_check_wrong_url(self):
	    """
	    test_check_wrong_url() should return 404 for url which is wrong.
	    """
	    client = Client()
	    response = client.get('/')
	    self.assertNotEqual(response.status_code, 200)

	def test_check_url(self):
	    """
	    test_check_url() should return 200 for url which is correct.
	    """
	    client = Client()
	    response = client.get(reverse('index'))
	    self.assertEqual(response.status_code, 200)

	def test_question(self):
	 	client = Client()
	 	question_text="Who is your favorite Cricketer?"
	 	q = Question(question_text=question_text,pub_date=timezone.now())
	 	q.save()
	 	response = client.get('/voteapp/')
	 	val = response.context['latest_question_list']
	 	self.assertEqual(val[0].question_text, question_text)
