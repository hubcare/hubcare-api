from django.test import TestCase

from hubcare_api import views

import os

class GetMetricsTestCase(TestCase):
    def setUp(self):
        self.owner = 'markinlimac'
        self.repo = 'dns_scan'
        self.token_auth = str(os.getenv('TOKEN_AUTH_GIT'))
        self.request_type = 'get'
        self.expected = {
                "issue_metric": {
                    "activity_rate": "0.00",
                    "activity_max_rate": "0.75",
                    "active_issues": 0,
                    "dead_issues": 3,
                    "total_issues": 3,
                    "help_wanted_issues": 0,
                    "help_wanted_rate": "0.00",
                    "help_wanted_max_rate": "0.40",
                    "good_first_issue": 0,
                    "good_first_issue_rate": "0.00",
                    "good_first_issue_max_rate": "0.40"
                },
                "community_metric": {
                    "code_of_conduct": False,
                    "contribution_guide": False,
                    "issue_template": False,
                    "license": False,
                    "pull_request_template": False,
                    "release_note": False,
                    "readme": True,
                    "description": True
                },
                "commit_metric": {
                    "total_commits": 0,
                    "commits_last_period": 0,
                    "commits_week": "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]",
                    "commits_high_score": 10,
                    "differents_authors": 0
                },
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
            
    def test_get_metrics(
        self
    ):
        ans = views.get_metric(self.owner,
                                        self.repo,
                                        self.token_auth,
                                        self.request_type)
        print(" ")
        print(ans)
        print(self.expected)
        print(" ")
        self.assertDictEqual(ans, self.expected)