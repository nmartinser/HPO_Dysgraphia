import pandas as pd
import stringdb

# Lectura de archivo de fenotipos y genes de disgrafía
df = pd.read_csv("id_51_genes.csv", sep="\t")

genes = set(df['GENE_SYMBOL'])
enrichment_df = stringdb.get_network(genes, required_score=500, species=9606)
enrichment_df.to_csv("grafo_51_genes.csv", sep='\t', index=False)
