from django.test import TestCase
from hubcare_api import views
import os


class CommitGraphTestCase(TestCase):
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
                    "10 weeks ago",
                    "9 weeks ago",
                    "8 weeks ago",
                    "7 weeks ago",
                    "6 weeks ago",
                    "5 weeks ago",
                    "4 weeks ago",
                    "3 weeks ago",
                    "2 weeks ago",
                    "this week"
                ],
                "y_axis": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            }

    def test_commit_graph(self):

        ans = views.get_commit_graph(self.metrics)
        self.assertDictEqual(ans, self.expected)

    def test_is_empty(self):

        ans = views.get_commit_graph(self.metrics)
        self.assertTrue(ans)
