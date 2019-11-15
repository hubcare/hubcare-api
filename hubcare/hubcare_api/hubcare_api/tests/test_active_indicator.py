from django.test import TestCase

from hubcare_api.indicators import active_indicator

from parameterized import parameterized


class ActiveIndicatorTestCase(TestCase):
    # def setUp(self):
    #         self.release_note_int = int(False)
    #         self.contributors_int = int(439)
    #         self.pr_qua_float = float(0.44)
    #         self.commit_week_int = int(3819)
    #         self.activity_rate = float(0.00)

    @parameterized.expand([
        (int(False), int(439), int(3819), float(0.44), float(0.00),
            float(0.488)),
        (int(False), int(0), int(0), float(0.00), float(0.00), float(0.0)),
        (int(True), int(74), int(444), float(0.68), float(0.00), float(0.636)),
    ])
    def test_calculate_active_metric(
        self,
        release_note_int,
        contributors_int,
        commit_week_int,
        pr_qua_float,
        activity_rate,
        expected
    ):
        ans = active_indicator.calculate_active_metric(release_note_int,
                                                       contributors_int,
                                                       commit_week_int,
                                                       pr_qua_float,
                                                       activity_rate)

        # assertAlmostEqual has an additional parameter place which takes the
        # no of decimal places upto which the number will be rounded of too.
        self.assertAlmostEqual(ans, expected, places=4)
