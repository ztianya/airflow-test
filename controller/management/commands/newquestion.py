from django.core.management.base import BaseCommand, CommandError
from polls.models import Question
from django.utils import timezone

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        q = Question(question_text="What's new?", pub_date=timezone.now())
        q.save()
        q.choice_set.create(choice_text='Not much', votes=0)
        self.stdout.write(self.style.SUCCESS('Successfully create question "%s"' % q))
