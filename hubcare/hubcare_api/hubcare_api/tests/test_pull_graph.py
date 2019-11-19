from django.test import TestCase
from hubcare_api import views
import os


class PullGraphTestCase(TestCase):
    def setUp(self):
        self.owner = 'markinlimac'
        self.repo = 'dns_scan'
        self.token_auth = str(os.getenv('GIT_AUTH_TOKEN'))
        self.request_type = 'post'
        self.metrics = views.get_metric(self.owner,
                                        self.repo,
                                        self.token_auth,
                                        self.request_type)
        self.expected = {
                "x_axis": [
                    "merged_yes",
                    "merged_no",
                    "open_yes_new",
                    "closed_yes",
                    "open_yes_old",
                    "closed_no",
                    "open_no_old"
                ],
                "y_axis": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            }

    def test_pull_graph(self):

        ans = views.get_pull_request_graph(self.metrics)
        self.assertDictEqual(ans, self.expected)
