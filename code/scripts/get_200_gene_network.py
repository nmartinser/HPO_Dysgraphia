import pandas as pd
import stringdb

# Lectura de archivo de fenotipos y genes de disgrafía
df = pd.read_csv("../results/propaged_genes.txt", sep="\t")

genes = set(df['DIAMOnD_node'])
enrichment_df = stringdb.get_network(genes, required_score=700 ,species=9606)
enrichment_df.drop_duplicates().to_csv("../results/grafo_200_genes.csv", sep='\t', index=False)