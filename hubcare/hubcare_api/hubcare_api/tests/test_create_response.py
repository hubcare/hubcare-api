from django.test import TestCase
from hubcare_api import views
import os
import json

class CreateResponseTestCase(TestCase):
    def setUp(self):
        self.owner = 'markinlimac'
        self.repo = 'dns_scan'
        self.token_auth = str(os.getenv('GIT_AUTH_TOKEN'))
        self.request_type = 'post'
        self.metrics = views.get_metric(self.owner,
                                        self.repo,
                                        self.token_auth,
                                        self.request_type)
        
        self.indicators = views.get_hubcare_indicators(self.owner,
                                                       self.repo,
                                                       self.token_auth,
                                                       self.metrics)

        self.commit_graph = views.get_commit_graph(self.metrics)
        self.pull_request_graph = views.get_pull_request_graph(self.metrics)
        
        self.graphs = {
            'commit_graph': self.commit_graph,
            'pull_request_graph': self.pull_request_graph
        }
        
        self.expected = dict(self.metrics)
        self.expected.update(self.indicators)
        self.expected.update(self.graphs)

    def test_create_response(self):

        ans = views.create_response(self.metrics, self.indicators ,self.commit_graph, self.pull_request_graph)

        self.assertEqual(ans, self.expected)
