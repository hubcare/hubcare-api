from hubcare_api.services import commit_metric
from parameterized import parameterized
from django.test import TestCase
import os


class CommitServiceTestCase(TestCase):
    def setUp(self):
        self.owner = 'romulosouza'
        self.repo = 'tutorialgit'
        self.token_auth = str(os.getenv('GIT_AUTH_TOKEN'))
        self.request_type = 'post'
        self.expected = {
                "commit_metric": {
                    "total_commits": 0,
                    "commits_last_period": 0,
                    "commits_week": "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]",
                    "commits_high_score": 10,
                    "differents_authors": 0
                }
            }

    def test_get_metric(self):

        ans = commit_metric.get_metric(self.owner,
                                       self.repo,
                                       self.token_auth,
                                       self.request_type)
        self.assertAlmostEqual(ans, self.expected)
