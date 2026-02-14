from main.scraper import NBAScraper
from main.storage import StorageManager
from main.analysis import NBAAnalysis

def main():
    url = "https://www.nba.com/stats/leaders"
    scraper = NBAScraper(url)
    jogadores = scraper.coletar_dados()
    scraper.fechar()

    storage = StorageManager()
    storage.salvar_json(jogadores)
    df = storage.carregar_dataframe(jogadores)

    if df.empty:
        print("Nenhum dado coletado. Verifique o scraper.")
        return

    analysis = NBAAnalysis(df)

    analysis.grafico_top10("pontos_por_jogo", "Top 10 jogadores - Pontos por jogo")

if __name__ == "__main__":
    main()