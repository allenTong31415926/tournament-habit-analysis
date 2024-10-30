# tournament/management/commands/bulk_insert_tournaments.py

from django.core.management.base import BaseCommand
from tournament.models import Tournament

class Command(BaseCommand):
    help = 'Bulk insert tournaments into the database'

    def handle(self, *args, **kwargs):
        # Clear all existing tournament records
        Tournament.objects.all().delete()

        tournaments_data = []

        # 50 tournaments with round_robin format, baseball sport, and team player setup.
        for i in range(50):
            tournaments_data.append(Tournament(
                name=f"Round Robin Baseball Tournament {i + 1}",
                format=1,
                sports=1,
                team_player=1
            ))

        # 150 tournaments with single_elimination format, basketball sport, and team player setup.
        for i in range(150):
            tournaments_data.append(Tournament(
                name=f"Single Elimination Basketball Tournament {i + 1}",
                format=2,
                sports=2,
                team_player=1
            ))

        # 30 tournaments with single_elimination format, tennis sport, and player setup.
        for i in range(30):
            tournaments_data.append(Tournament(
                name=f"Single Elimination Tennis Tournament {i + 1}",
                format=2,
                sports=3,
                team_player=2
            ))

        # 5 tournaments with single_elimination format, tennis sport, and team setup.
        for i in range(5):
            tournaments_data.append(Tournament(
                name=f"Single Elimination Tennis Team Tournament {i + 1}",
                format=2,
                sports=3,
                team_player=1
            ))

        # Bulk insert all tournament records into the database.
        Tournament.objects.bulk_create(tournaments_data)

        self.stdout.write(self.style.SUCCESS(f"Inserted {len(tournaments_data)} tournament records into the database."))

