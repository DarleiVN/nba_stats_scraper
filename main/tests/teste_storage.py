import os
from storage import StorageManager

def test_salvar_e_carregar_json(tmp_path):
    dados = [{"nome": "LeBron James", "time": "Lakers", "jogos": "82", "pontos_por_jogo": "27.5"}]
    arquivo = tmp_path / "nba_test.json"

    storage = StorageManager(str(arquivo))
    storage.salvar_json(dados)
    df = storage.carregar_dataframe(dados)

    # Verifica se o arquivo foi criado
    assert arquivo.exists()
    # Verifica se dataframe tem coluna 'nome'
    assert "nome" in df.columns
    # Verifica se pontos foram convertidos para float
    assert df["pontos_por_jogo"].dtype == "float64"