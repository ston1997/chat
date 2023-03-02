from django.db.models import Count

from settings.chat.models import Thread


class ThreadValidator:
    def __call__(self, data):
        user_ids = set(data['participants'])
        threads = Thread.objects.filter(
            participants__id__in=user_ids
        ).annotate(count=Count('id')).filter(count=len(user_ids))

        if threads.exists():
            return threads.first()

        # create new thread if it doesn't exist
        thread = Thread.objects.create(
            participants=user_ids
        )

        return thread
