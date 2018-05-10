from django.core.management.base import BaseCommand, CommandError
from polls.models import Question
from django.utils import timezone

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        q = Question.objects.get(pk=1)
        c = q.choice_set.get(choice_text='Not much')
        c.votes += 1
        c.save()
        self.stdout.write(self.style.SUCCESS(' Votes for "%s" successfully' % q))
