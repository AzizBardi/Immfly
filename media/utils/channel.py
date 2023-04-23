from django.db.models import Sum, Count


def calculate_rating(channel):
    subchannel_ratings = []
    if channel.contents.exists():
        content_rating_sum = channel.contents.aggregate(Sum('rating'))['rating__sum'] or 0
        content_rating_count = channel.contents.aggregate(Count('rating'))['rating__count'] or 1
        subchannel_ratings.append(content_rating_sum)
        return (sum(subchannel_ratings) / content_rating_count)
    elif channel.subchannels.exists():
        for subchannel in channel.subchannels.all():
            return calculate_rating(subchannel)
    else:
        return 0