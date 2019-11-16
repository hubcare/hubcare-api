from django.test import TestCase

from hubcare_api.services import issue_metric

from parameterized import parameterized

import os

class IssueServiceTestCase(TestCase):
    def setUp(self):
        self.owner = 'pedro-prp'
        self.repo = 'Buzz-terminal'
        self.token_auth = str(os.getenv('TOKEN_AUTH_GIT'))
        self.request_type = 'get'
        self.expected = {
                "issue_metric": {
                    "activity_rate": "0.00",
                    "activity_max_rate": "0.75",
                    "active_issues": 0,
                    "dead_issues": 1,
                    "total_issues": 1,
                    "help_wanted_issues": 0,
                    "help_wanted_rate": "0.00",
                    "help_wanted_max_rate": "0.40",
                    "good_first_issue": 0,
                    "good_first_issue_rate": "0.00",
                    "good_first_issue_max_rate": "0.40"
                }
            }
    def test_get_metric(
        self
    ):
        ans = issue_metric.get_metric(self.owner,
                                        self.repo,
                                        self.token_auth,
                                        self.request_type)
        self.assertAlmostEqual(ans, self.expected)