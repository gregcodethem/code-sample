from django.test import TestCase
from betfair.sports_operations import list_market_info
from unittest.mock import patch
from betfair.mock_api_results import MockMarketBookResult

class SportsOperationsTest(TestCase):

    @patch('betfair.sports_operations.list_market_info')
    def test_list_market_info(self, mock_list_market_info):

        # Assign mock market book result
        mock_list_market_info.return_value = MockMarketBookResult()

        market_info = mock_list_market_info('1.149383146')

        self.assertEqual(mock_list_market_info.called,
                         True)
        mock_list_market_info.assert_called_with(
            '1.149383146')

        expected_selection_ids = ['48756', '48224', '58805']
        for i in range(len(market_info.runners)):
            runner = market_info.runners[i]
            called_selection_id = runner.selection_id
            expected_selection_id = expected_selection_ids[i]
            self.assertEqual(
                called_selection_id,
                expected_selection_id)

