# tournament/signals.py

import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tournament
from elasticsearch import Elasticsearch

# Set up Elasticsearch client
es = Elasticsearch(os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"))


@receiver(post_save, sender=Tournament)
def index_tournament_in_elasticsearch(sender, instance, **kwargs):
    # Prepare the document for Elasticsearch
    doc = {
        "sports": instance.sports,
        "format": instance.format,
        "team_player": instance.team_player
    }
    # Index the document in Elasticsearch
    es.index(index="tournaments", id=instance.id, document=doc)
