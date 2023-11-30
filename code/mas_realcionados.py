import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from networkx.algorithms import bipartite
import networkx as nx
import matplotlib.pyplot as plt
import os
import networkx as nx
import matplotlib.pyplot as plt
%pip install python-louvain
# Especifica la ruta de tu archivo TSV
ruta_archivo = 'red_fenotipos_genes_dysgraphia.txt'

# Lee el archivo TSV y crea un grafo bipartito
    
df = pd.read_csv(ruta_archivo, sep='\t')

# Crea un grafo bipartito
G = nx.Graph()

# Agregar nodos y aristas al grafo bipartito
for _, row in df.iterrows():
    gene_symbol = row['gene_symbol']
    hpo_id = row['hpo_id']
    G.add_node(gene_symbol, bipartite=0)  # genes en la primera partición
    G.add_node(hpo_id, bipartite=1)       # HPO IDs en la segunda partición
    G.add_edge(gene_symbol, hpo_id)
#centra el grafo
target_hpo = 'HP:0010526'

# Calcular las longitudes de los caminos más cortos desde el nodo de interés
shortest_paths = nx.single_source_shortest_path_length(G, target_hpo)

# Filtrar nodos a 2 pasos o menos
filtered_nodes2 = [node for node, distance in shortest_paths.items() if distance <= 2]

# Crear un subgrafo con los nodos filtrados
subgraph2 = G.subgraph(filtered_nodes2)

## tomamos de la red todos los nodos de tipo hpo del grafo
hpo_ids  = bipartite.sets(subgraph2)[0]

hpo_projection = nx.bipartite.projected_graph(subgraph2, hpo_ids )

genes= bipartite.sets(subgraph2)[1]
gene_projection = nx.bipartite.projected_graph(subgraph2, genes )

#usamos la lista de nodos (que son los nodos a un paso del hpo , sacada de la pryeccion de hpos)
lista_de_nodos = list(hpo_projection.nodes())
df_un_paso=df[df['hpo_id'].isin(lista_de_nodos)]
## filtramos tambien con la lista de genes relacionados con la d
df_un_paso=df_un_paso[df['gene_symbol'].isin(gene_projection.nodes())]
df_un_paso=df_un_paso[["ncbi_gene_id","gene_symbol","hpo_id","hpo_name"]].drop_duplicates()

df_un_paso['relaciones_con_dysgraphia']=1

resultado=df_un_paso.groupby('hpo_id').agg({'hpo_name': 'first', 'relaciones_con_dysgraphia': 'sum'}).reset_index().sort_values(by="relaciones_con_dysgraphia", ascending = False)

ruta_relativa =  os.path.join(os.path.dirname(os.getcwd()), 'results')+"/"
resultado.to_csv(ruta_relativa+'Hpos_rank_relacionados.csv', index=False)

top25=resultado[resultado["relaciones_con_dysgraphia"]>=45]
lista25=top25["hpo_id"].tolist()
genesList = df_un_paso[df_un_paso["hpo_id"]== 'HP:0010526'].sort_values(by= "gene_symbol")["gene_symbol"].drop_duplicates().tolist()

listaTotal=lista25+genesList
grafoMasRelacion = G.subgraph(listaTotal)


def visualizar_grafo_bipartito_circular(grafo, dpi=300):
  

    # Asegurarse de que la carpeta de resultados exista en el mismo nivel que la carpeta de código
    carpeta_guardado = os.path.join(os.path.dirname(os.getcwd()), 'results')
    if not os.path.exists(carpeta_guardado):
        os.makedirs(carpeta_guardado)

    # Dividir nodos por partición
    nodos_genes = [nodo for nodo, particion in nx.get_node_attributes(grafo, 'bipartite').items() if particion == 0]
    nodos_hpos = [nodo for nodo, particion in nx.get_node_attributes(grafo, 'bipartite').items() if particion == 1]

    # Crear un layout circular
    pos = nx.circular_layout(grafo)

    # Dibujar nodos y aristas
    nx.draw_networkx_nodes(grafo, pos, nodelist=nodos_genes, node_color='blue', label='Genes', node_size=50)
    nx.draw_networkx_nodes(grafo, pos, nodelist=nodos_hpos, node_color='red', label='HPOs', node_size=50)
    nx.draw_networkx_edges(grafo, pos, edge_color='gray')

    # Etiquetas
    labels = {nodo: nodo for nodo in grafo.nodes}
    nx.draw_networkx_labels(grafo, pos, labels, font_size=8)

    # Mostrar leyenda
    plt.legend()

    # Guardar el gráfico en la carpeta especificada con nombre de archivo y resolución
    nombre_archivo = 'grafo_Hpos_alta_relacion.png'
    ruta_guardado = os.path.join(carpeta_guardado, nombre_archivo)
    plt.savefig(ruta_guardado, dpi=dpi)
 visualizar_grafo_bipartito_circular(grafoMasRelacion)
