import pytest
import pandas as pd
from main.analysis import NBAAnalysis

def test_grafico_top5_pontos():
    dados = [
        {"PLAYER": "Jogador A", "TEAM": "Time X", "GP": 10, "PTS": 20},
        {"PLAYER": "Jogador B", "TEAM": "Time Y", "GP": 12, "PTS": 25},
        {"PLAYER": "Jogador C", "TEAM": "Time Z", "GP": 8, "PTS": 15},
        {"PLAYER": "Jogador D", "TEAM": "Time W", "GP": 14, "PTS": 30},
        {"PLAYER": "Jogador E", "TEAM": "Time V", "GP": 9, "PTS": 18},
    ]
    df = pd.DataFrame(dados)
    analysis = NBAAnalysis(df)

    # Agora usa a coluna real "PTS"
    analysis.grafico_top10("PTS", "Top 10 jogadores - Pontos por jogo")