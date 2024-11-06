# tournament/utils.py
from elasticsearch import Elasticsearch
import os

es = Elasticsearch(os.getenv("ELASTICSEARCH_URL", "http://elasticsearch:9200"))


def get_tournament_trends(sport):
    """
    Query Elasticsearch for trends in `format` and `team_player`
    based on the selected sport.
    """
    query = {
        "query": {
            "term": {
                "sports": sport
            }
        },
        "size": 0,
        "aggs": {
            "popular_formats": {
                "terms": {
                    "field": "format"
                }
            },
            "team_player_distribution": {
                "terms": {
                    "field": "team_player"
                }
            }
        }
    }

    response = es.search(index="tournaments", body=query)

    # Extract data for format and team/player trends
    format_trends = [bucket['key'] for bucket in response['aggregations']['popular_formats']['buckets']]
    team_player_trends = [bucket['key'] for bucket in response['aggregations']['team_player_distribution']['buckets']]

    return {
        "formats": format_trends,
        "team_player": team_player_trends
    }
