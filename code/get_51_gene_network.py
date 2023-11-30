import pandas as pd
import stringdb

# Lectura de archivo de fenotipos y genes de disgrafía
df = pd.read_csv("id_51_genes.csv", sep="\t")

genes = set(df['GENE_SYMBOL'])
enrichment_df = stringdb.get_string_ids(genes, species=9606)
enrichment_df['stringId'].to_csv("../results/grafo_51_genes.txt", sep='\t', index=False)
