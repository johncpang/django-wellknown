from django.test import TestCase
from wellknown import models


VALID_PATH = 'acme-challenge/challenge-request'
MISSING_PATH = 'missing'


class WellKnownIntegrationTest(TestCase):

    def testFetchValidPath(self):
        DATA = 'challenge-response'
        models.Resource(
            path=VALID_PATH,
            content=DATA).save()
        response = self.client.get(
            '/.well-known/%s' % VALID_PATH)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, DATA)

    def testFetchMissingResource(self):
        response = self.client.get(
            '/.well-known/%s' % MISSING_PATH)
        self.assertEqual(response.status_code, 404)

    def testFailToPost(self):
        response = self.client.post(
            '/.well-known/%s' % VALID_PATH, {'path': 'foo'})
        self.assertEqual(response.status_code, 403)
