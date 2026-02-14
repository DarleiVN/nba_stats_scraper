import pytest
from main.scraper import NBAScraper

@pytest.mark.skip(reason="Scraping depende de internet e Selenium")
def test_scraper_coleta_dados():
    url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1"
    scraper = NBAScraper(url)
    jogadores = scraper.coletar_dados()
    scraper.fechar()

    # Verifica se retornou uma lista
    assert isinstance(jogadores, list)
    # Verifica se pelo menos um jogador foi coletado
    assert len(jogadores) > 0
    # Verifica se contém chave 'nome'
    assert "nome" in jogadores[0]