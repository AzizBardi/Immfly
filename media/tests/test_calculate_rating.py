from media.models import Channel, Content
from media.utils.channel import calculate_rating
import pytest

@pytest.mark.django_db
def test_calculate_rating():
    channel = Channel.objects.create(title='test channel',slug='slug1')

    expected_rating = (4.5 + 3.0) / 2

    assert calculate_rating(channel) == expected_rating

@pytest.mark.django_db
def test_calculate_rating_with_subchannels():
    channel = Channel.objects.create(title='Test Channel', slug='test-channel')


    subchannel = Channel.objects.create(title='Subchannel 1', slug='subchannel-1')
    channel.subchannels.add(subchannel)


    expected_rating = (((4.5 + 3.0) / 2) + ((2.5 + 4.0) / 2)) / 2

    rating = calculate_rating(channel)

    assert rating == expected_rating

@pytest.mark.django_db
def test_calculate_rating_no_content_or_subchannels():

    channel = Channel.objects.create(title='Test Channel', slug='test-channel')

    expected_rating = 0

    rating = calculate_rating(channel)

    assert rating == expected_rating
