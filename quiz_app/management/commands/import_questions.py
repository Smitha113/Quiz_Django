# In quiz_app/management/commands/import_questions.py

import csv
from django.core.management.base import BaseCommand
from quiz_app.models import Topic, Quiz, Question, Answer

class Command(BaseCommand):
    help = 'Import questions and answers from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        parser.add_argument('topic_name', type=str, help='Name of the topic to associate the questions with')
        parser.add_argument('quiz_title', type=str, help='Title of the quiz to add questions to')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        topic_name = options['topic_name']
        quiz_title = options['quiz_title']
        
        # Find or create the topic
        topic, created = Topic.objects.get_or_create(name=topic_name)
        
        # Find the quiz
        quiz = Quiz.objects.get(title=quiz_title, topic=topic)
        
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                question = Question.objects.create(
                    quiz=quiz,
                    text=row['Question']
                )
                for option in ['Option A', 'Option B', 'Option C', 'Option D']:
                    Answer.objects.create(
                        question=question,
                        text=row[option],
                        is_correct=row['Correct Answer'] == option
                    )
        self.stdout.write(self.style.SUCCESS('Questions and answers imported successfully'))
