import stringdb
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

# grafo 200 genes
# Read the CSV file using pandas
df = pd.read_csv('../results/grafo_200_genes.csv', sep='\t')

# Create a graph from the CSV data
G = nx.from_pandas_edgelist(df, 'preferredName_A', 'preferredName_B')

# Ejecutar el algoritmo de greedy_modularity_communities
communities = nx.community.greedy_modularity_communities(G)

# Crear un grafo con colores por comunidades
colors = [0] * len(G.nodes)
for i, community in enumerate(communities):
    for node in community:
        colors[list(G.nodes()).index(node)] = i

pos = nx.spring_layout(G) 
nx.draw(G, pos, node_color=colors, node_size = 60)

# Guardar el grafo en un archivo
output_path = os.path.join('../results', 'graph_communities.png')
plt.savefig(output_path)

# ENRIQUECIMIENTO --------------------

# definimos las columnas que nos interesa presentar para el enriquecimiento
columnas_seleccionadas = ["category", "number_of_genes", "p_value", "fdr", "description"]



# Análisis funcional del grafo entero
enrichment_df = stringdb.get_enrichment(G.nodes(), species=9606)
enrichment_df = enrichment_df[columnas_seleccionadas]
filter_df = enrichment_df.sort_values('fdr', ascending=True)
filter_df.to_csv('../results/enriquecimiento_200_ordenado.csv', sep='\t', index=False)

# Análisis funcional de la comunidad1
enrichment_df= stringdb.get_enrichment(communities[0], species=9606)
enrichment_df = enrichment_df[columnas_seleccionadas]
filter_df=enrichment_df.sort_values('fdr', ascending=True)
filter_df.to_csv('../results/enriquecimiento_comunidad1_ordenado.csv', sep='\t', index=False)

# Análisis funcional de la comunidad2
enrichment_df= stringdb.get_enrichment(communities[1], species=9606)
enrichment_df = enrichment_df[columnas_seleccionadas]
filter_df=enrichment_df.sort_values('fdr', ascending=True)
filter_df.to_csv('../results/enriquecimiento_comunidad2_ordenado.csv', sep='\t', index=False)

# Análisis funcional de la comunidad3
enrichment_df= stringdb.get_enrichment(communities[2], species=9606)
enrichment_df = enrichment_df[columnas_seleccionadas]
filter_df=enrichment_df.sort_values('fdr', ascending=True)
filter_df.to_csv('../results/enriquecimiento_comunidad3_ordenado.csv', sep='\t', index=False)