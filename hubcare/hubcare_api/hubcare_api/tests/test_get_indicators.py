from django.test import TestCase
from hubcare_api import views
import os


class GetIndicatorsTestCase(TestCase):
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
                "indicators": {
                    "active_indicator": 0.0,
                    "welcoming_indicator": 14.29,
                    "support_indicator": 25.0
                }
            }

    def test_get_indicators(self):

        ans = views.get_hubcare_indicators(self.owner,
                                        self.repo,
                                        self.token_auth,
                                        self.metrics)
        self.assertDictEqual(ans, self.expected)
