from mjb.primitives.dates import convert_to_24_hour_format


class TestDateTime:

    def test_convert_to_24_hour_format_valid_data(self):
        """
        Test conversion of valid 12-hour format time strings to 24-hour format.
        """
        assert convert_to_24_hour_format('07:05:45PM') == '19:05:45'
        assert convert_to_24_hour_format('12:40:22AM') == '00:40:22'
        assert convert_to_24_hour_format('12:40:22PM') == '12:40:22'
        assert convert_to_24_hour_format('01:05:45AM') == '01:05:45'

        # edge cases.
        assert convert_to_24_hour_format('12:00:00PM') == '12:00:00'
        assert convert_to_24_hour_format('12:00:00AM') == '00:00:00'

    def test_convert_to_24_hour_format_invalid_data(self):
        """
        Test handling of invalid 12-hour format time strings.
        """
        assert convert_to_24_hour_format('') is False
        assert convert_to_24_hour_format('01:05:45AMPM') is False
        assert convert_to_24_hour_format('24:01:01AM') is False
        assert convert_to_24_hour_format('11:60:60PM') is False
