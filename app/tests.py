from django.test import TestCase,Client
from .models import Item
import datetime as dt
from django.utils import timezone as tz
from django.urls import reverse,resolve
from .views import ItemFilterView,ItemDetailView,ItemCreateView,ItemUpdateView,ItemDeleteView
from .forms import ItemForm




class TestModels(TestCase):
    
    def testEmpty(self):
        saved_item=Item.objects.all()
        self.assertEqual(saved_item.count(),0)


    def testCreateUser(self):
        item=Item(name="みぽりん",age=17,sex=2,memo="大洗学園戦車道部",created_at=tz.now())
        item.save()
        saved_item=Item.objects.all()
        self.assertEqual(saved_item.count(),1)

    def testPushAndStack(self):
        item=Item()
        item.name="みぽりん"
        item.age=17
        item.sex=2
        item.memo="大洗学園戦車道部"
        created=tz.now()
        item.created_at=created

        item.save()
        saved_item=Item.objects.all()
        actual_item=saved_item[0]

        self.assertEqual(actual_item.name,"みぽりん")
        self.assertEqual(actual_item.age,17)
        self.assertEqual(actual_item.sex,2)
        self.assertEqual(actual_item.memo,"大洗学園戦車道部")
        self.assertEqual(actual_item.created_at,created)

class TestUrls(TestCase):
    def testFilterView(self):
        view=resolve('/')
        self.assertEqual(view.func.view_class,ItemFilterView)

    def testDetailView(self):
        view=resolve('/detail/1/')
        self.assertEqual(view.func.view_class,ItemDetailView)

    def testCreateView(self):
        view=resolve('/create/')
        self.assertEqual(view.func.view_class,ItemCreateView)

    def testDeleteView(self):
        view=resolve('/delete/1/')
        self.assertEqual(view.func.view_class,ItemDeleteView)

    def testUpdateView(self):
        view=resolve('/update/1/')
        self.assertEqual(view.func.view_class,ItemUpdateView)

class TestViews(TestCase):
    def setUp(self):
        item1=Item.objects.create(name="みぽりん",age=17,sex=2,memo="大洗学園戦車道部",created_at=tz.now())
        item2=Item.objects.create(name="まぽりん",age=18,sex=2,memo="黒森峰学園戦車道部",created_at=tz.now())


    def testGet(self):
        res=self.client.get(reverse('create'))
        self.assertEquals(res.status_code,302)

    def testLogin(self):
        client=Client()
        loginstatus=client.logout()
        self.assertFalse(loginstatus)

    # def testTemplateLogin(self):
    #     client=Client()
    #     loginuser=client.login()
    #     self.assertTrue(loginuser)

    def tearDown(self):
        item1=Item.objects.create(name="みぽりん",age=17,sex=2,memo="大洗学園戦車道部",created_at=tz.now())
        item2=Item.objects.create(name="まぽりん",age=18,sex=2,memo="黒森峰学園戦車道部",created_at=tz.now()) 

class TestForm(TestCase):

    def testItemForm(self):
        params=dict(name="みぽりん",age=17,sex=2,memo="大洗学園戦車道部",created_at=tz.now())
        item=Item()
        form=ItemForm(params,instance=item)
        self.assertTrue(form.is_valid())

    def testEmptyItemForm(self):
        params=dict()
        item=Item()
        form=ItemForm(params,instance=item)
        self.assertFalse(form.is_valid())      