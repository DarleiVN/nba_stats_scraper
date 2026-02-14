import matplotlib.pyplot as plt
import seaborn as sns

class NBAAnalysis:
    def __init__(self, dataframe):
        self.df = dataframe

    def grafico_top10(self, coluna: str, titulo: str = None):
        """Gera um gráfico de barras horizontais com os 10 melhores jogadores em uma estatística."""
        top10 = self.df.sort_values(coluna, ascending=False).head(10)

        # qual coluna usar para o eixo X
        eixo_x = "PLAYER" if "PLAYER" in self.df.columns else "nome"

        
        colors = sns.color_palette("Blues", n_colors=10)

        # Gráfico
        ax = top10.plot(
            x=eixo_x, y=coluna, kind="barh", figsize=(10, 6),
            color=colors, legend=False
        )

        plt.title(titulo or f"Top 10 jogadores - {coluna}", fontsize=16, fontweight="bold")
        plt.xlabel(coluna, fontsize=12)
        plt.ylabel("Jogadores", fontsize=12)
        plt.tight_layout()

        
        for p in ax.patches:
            ax.annotate(
                f"{p.get_width():.1f}",
                (p.get_width(), p.get_y() + p.get_height()/2),
                ha="left", va="center", fontsize=10, fontweight="bold", color="black"
            )

        plt.show()