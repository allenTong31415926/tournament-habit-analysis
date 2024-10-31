# tournament/views.py
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import logging
from django.shortcuts import render
from .models import Tournament


def tournament_chart(request):
    selected_sport = request.GET.get('sport', '')

    # If no sport is selected, return without generating the chart
    if not selected_sport:
        return render(request, 'tournament/tournament_chart.html', {
            'graphic': None,
            'selected_sport': selected_sport
        })

    # Define a base queryset with the selected sport filter
    tournaments_queryset = Tournament.objects.filter(sports=Tournament.get_sport_enum(selected_sport))

    # Get count of tournaments for each format within the selected sport
    round_robin_count = tournaments_queryset.filter(format=1).count()
    single_elimination_count = tournaments_queryset.filter(format=2).count()
    double_elimination_count = tournaments_queryset.filter(format=3).count()

    # Get count of tournaments for team/player within the selected sport
    team_count = tournaments_queryset.filter(team_player=1).count()
    player_count = tournaments_queryset.filter(team_player=2).count()

    # Initialize the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Chart 1: Formats Chart ---
    formats = ['Round Robin', 'Single Elimination', 'Double Elimination']
    colors_formats = ['blue', 'red', 'orange']
    formats_counts = [round_robin_count, single_elimination_count, double_elimination_count]

    # Create the bar chart for formats
    bars_formats = ax1.bar(formats, formats_counts, color=colors_formats)
    ax1.set_title(f'Number of {selected_sport.capitalize()} Tournaments by Format')
    ax1.set_xlabel('Format')
    ax1.set_ylabel('Number of Tournaments')
    ax1.set_ylim(0)  # Ensure y-axis starts at 0

    # Display count above each bar
    for bar, count in zip(bars_formats, formats_counts):
        ax1.text(bar.get_x() + bar.get_width() / 2, count, str(count), ha='center', va='bottom')

    # --- Chart 2: Team/Player Chart ---
    team_player_types = ['Team', 'Player']
    colors_team_player = ['blue', 'red']
    team_player_counts = [team_count, player_count]

    # Create the bar chart for team/player
    bars_team_player = ax2.bar(team_player_types, team_player_counts, color=colors_team_player)
    ax2.set_title(f'Number of {selected_sport.capitalize()} Tournaments by Team/Player')
    ax2.set_xlabel('Type')
    ax2.set_ylabel('Number of Tournaments')
    ax2.set_ylim(0)  # Ensure y-axis starts at 0

    # Display count above each bar
    for bar, count in zip(bars_team_player, team_player_counts):
        ax2.text(bar.get_x() + bar.get_width() / 2, count, str(count), ha='center', va='bottom')

    # Encode the chart as a PNG image
    buffer = BytesIO()
    plt.tight_layout()
    fig.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    graphic = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Pass the encoded image and selected sport to the template
    return render(request, 'tournament/tournament_chart.html', {'graphic': graphic, 'selected_sport': selected_sport})
