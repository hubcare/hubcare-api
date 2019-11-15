from django.test import TestCase

from hubcare_api.indicators import welcoming_indicator

from parameterized import parameterized


class WelcomingIndicatorTestCase(TestCase):

    @parameterized.expand([
        (int(439), int(False), float(0.00), float(0.00), int(False),
         int(True), int(False), int(False), int(False), int(True),
         float(0.00), float(0.44), float(0.19)),
        (int(1), int(False), float(0.00), float(0.00), int(False),
         int(False), int(False), int(False), int(False), int(False),
         float(0.00), float(0.00), float(0.0179)),
        (int(74), int(True), float(0.04), float(0.01), int(True),
         int(True), int(True), int(True), int(True), int(True),
         float(0.00), float(0.68), float(0.6854)),
    ])
    def test_calculate_welcoming_metric(
        self,
        contributors_int,
        cont_guide_int,
        help_float,
        good_float,
        prt_int,
        description_int,
        code_cond_int,
        readme_int,
        issue_temp_int,
        license_int,
        act_rate_float,
        pr_qua_float,
        expected
    ):
        ans = welcoming_indicator.calculate_welcoming_metric(contributors_int,
                                                             cont_guide_int,
                                                             help_float,
                                                             good_float,
                                                             prt_int,
                                                             description_int,
                                                             code_cond_int,
                                                             readme_int,
                                                             issue_temp_int,
                                                             license_int,
                                                             act_rate_float,
                                                             pr_qua_float)
        # assertAlmostEqual has an additional parameter place which takes the
        # no of decimal places upto which the number will be rounded of too.
        self.assertAlmostEqual(ans, expected, places=4)
