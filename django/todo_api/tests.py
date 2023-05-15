from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task
from SDG23.solve import getMaxSum, uniqueChars

class TaskTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Finish the project', 'description': 'Complete the remaining tasks'}
        self.response = self.client.post(reverse('task_list'), self.task_data, format='json')

    def test_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task_list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        task = Task.objects.get()
        response = self.client.get(reverse('task_detail', kwargs={'task_id': task.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        task = Task.objects.get()
        updated_task = {'title': 'Finish the project', 'description': 'Complete all the remaining tasks'}
        response = self.client.put(reverse('task_detail', kwargs={'task_id': task.id}), updated_task, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.get()
        response = self.client.delete(reverse('task_detail', kwargs={'task_id': task.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_mark_task_as_complete(self):
        task = Task.objects.get()
        response = self.client.put(reverse('task_complete', kwargs={'task_id': task.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
####################### Unit test for algorithms Questions in solve.py #######################
class UniqueCharsTestCase(TestCase):
    def test_empty_string(self):
        self.assertEqual(uniqueChars(''), '')

    def test_whitespace_string(self):
        self.assertEqual(uniqueChars('  \t   '), '')

    def test_all_unique_chars(self):
        self.assertEqual(uniqueChars('abcdefg'), 'abcdefg')

    def test_only_unique_chars(self):
        self.assertEqual(uniqueChars('hello world'), 'helo wrd')
        self.assertEqual(uniqueChars('foo bar baz'), 'fo barz')
        self.assertEqual(uniqueChars('python django'), 'python djag')

    def test_preserve_order_of_unique_chars(self):
        self.assertEqual(uniqueChars('abca'), 'abc')
        self.assertEqual(uniqueChars('abbac'), 'abc')
        self.assertEqual(uniqueChars('abcabc'), 'abc')
        

class GetMaxSumTestCase(TestCase):
    def test_maximum_sum(self):
        self.assertEqual(getMaxSum([1, -2, 3, 4, -5, 8]), 10)
        self.assertEqual(getMaxSum([-1, 2, 3, -4, 5, 10]), 16)
        self.assertEqual(getMaxSum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(getMaxSum([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(getMaxSum([5]), 5)

    def test_empty_or_negative_array(self):
        self.assertEqual(getMaxSum([]), 0)
        self.assertEqual(getMaxSum([-1, -2, -3]), 0)
