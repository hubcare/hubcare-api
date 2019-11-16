from django.test import TestCase

from hubcare_api.services import commit_metric

from parameterized import parameterized

import os

class CommitServiceTestCase(TestCase):
    def setUp(self):
        self.owner = 'pedro-prp'
        self.repo = 'Buzz-terminal'
        self.token_auth = str(os.getenv('TOKEN_AUTH_GIT'))
        self.request_type = 'get'
        self.expected = {
                "commit_metric": {
                        "total_commits": 2,
                        "commits_last_period": 2,
                        "commits_week": "[0, 0, 0, 0, 0, 0, 2, 0, 0, 0]",
                        "commits_high_score": 10,
                        "differents_authors": 1
                }
            }
    def test_get_metric(
        self
    ):
        ans = commit_metric.get_metric(self.owner,
                                        self.repo,
                                        self.token_auth,
                                        self.request_type)
        self.assertAlmostEqual(ans, self.expected)