from hubcare_api.services import pull_request_metric
from parameterized import parameterized
from django.test import TestCase
import os


class PullRequestServiceTestCase(TestCase):
    def setUp(self):
        self.owner = 'pedro-prp'
        self.repo = 'Buzz-terminal'
        self.token_auth = str(os.getenv('TOKEN_AUTH_GIT'))
        self.request_type = 'post'
        self.expected = {
                "pull_request_metric": {
                    "acceptance_quality": "0.00",
                    "categories": {
                        "merged_yes": 0,
                        "merged_no": 0,
                        "open_yes_new": 0,
                        "closed_yes": 0,
                        "open_yes_old": 0,
                        "closed_no": 0,
                        "open_no_old": 0
                    }
                }
            }

    def test_get_metric(
        self
    ):
        ans = pull_request_metric.get_metric(self.owner,
                                             self.repo,
                                             self.token_auth,
                                             self.request_type)
        self.assertAlmostEqual(ans, self.expected)
