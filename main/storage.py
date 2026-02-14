import pandas as pd
import json

class StorageManager:
    def __init__(self, arquivo="nba_stats.json"):
        self.arquivo = arquivo

    def salvar_json(self, dados):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def carregar_dataframe(self, dados):
        df = pd.DataFrame(dados)

        
        df = df.rename(columns={
            "PLAYER": "nome",
            "TEAM": "time",
            "AGE": "idade",
            "GP": "jogos",
            "W": "vitorias",
            "L": "derrotas",
            "MIN": "minutos",
            "PTS": "pontos_por_jogo",
            "REB": "rebotes",
            "AST": "assistencias",
            "FG%": "fg_percentual",
            "3P%": "tres_pontos_percentual",
            "FT%": "lances_livres_percentual"
        })

        
        colunas_numericas = [
            "idade", "jogos", "vitorias", "derrotas", "minutos",
            "pontos_por_jogo", "rebotes", "assistencias",
            "fg_percentual", "tres_pontos_percentual", "lances_livres_percentual"
        ]
        for col in colunas_numericas:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        return df