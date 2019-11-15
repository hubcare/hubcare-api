from django.test import TestCase

from hubcare_api.indicators import support_indicator

from parameterized import parameterized


class SupportIndicatorTestCase(TestCase):

    @parameterized.expand([
        (int(True), int(True), int(True), int(True), int(True), int(True), float(0.00), float(0.8125)),
        (int(False), int(False), int(True), int(True), int(False), int(False), float(0.00), float(0.25)),
        (int(False), int(False), int(False), int(False), int(False), int(False), float(0.00), float(0.0)),
    ])
    def test_calculate_support_metric(
        self,
        readme_int,
        issue_temp_int,
        license_int,
        description_int,
        code_cond_int,
        release_note_int,
        issue_act_float,
        expected
    ):
        ans = support_indicator.calculate_support_metric(readme_int,
                                                         issue_temp_int,
                                                         license_int,
                                                         description_int,
                                                         code_cond_int,
                                                         release_note_int,
                                                         issue_act_float)
        self.assertEqual(ans, expected)
