from django.test import TestCase
from .models import Projects,Profile,Rates,Comments
# Create your tests here.

class TestProjects(TestCase):
    def setUp(self):

        self.new_project=Projects(name='The Law',image='kenya.jpg',description='lit',link='https:kenya',screen1='s',screen2='njcnjd')

    def test_instace(self):
        self.assertTrue(isinstance(self.new_project,Projects))

    def test_initialization(self):
        self.assertEqual(self.new_project.name,"The Law")
        self.assertEqual(self.new_project.image,"kenya.jpg")
        self.assertEqual(self.new_project.description,"lit")
        self.assertEqual(self.new_project.link,"https:kenya")
        self.assertEqual(self.new_project.screen1,"s")
        self.assertEqual(self.new_project.screen2,"njcnjd")

class TestProfile(TestCase):
    def setUp(self):
        self.new_profile=Profile(profile='collo',bio='am in love withoutu',phone="0715775170")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_initialization(self):
        self.assertEqual(self.new_profile.profile,'collo')
        self.assertEqual(self.new_profile.bio,'am in love withoutu')
        self.assertEqual(self.new_profile.phone,"0715775170")


class TestRating(TestCase):
    def setUp(self):
        self.new_rating=Rates(design=0,usability=0,content=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_rating,Rates))

    def test_initialization(self):
        self.assertEqual(self.new_rating.design,0)
        self.assertEqual(self.new_rating.usability,0)
        self.assertEqual(self.new_rating.content,0)
class TestComments(TestCase):
    def setUp(self):
        self.new_comment=Comments(comment="Kenya",pro_id=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comments))

    def test_initialization(self):
        self.assertEqual(self.new_comment.comment,"Kenya")
        self.assertEqual(self.new_comment.pro_id,0)
