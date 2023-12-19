import pandas as pd
import stringdb
import requests

# Lectura de archivo de fenotipos y genes de disgrafía
df = pd.read_csv("id_51_genes.csv", sep="\t")

genes = set(df['GENE_SYMBOL'])
enrichment_df = stringdb.get_enrichment(genes)
filter_df = enrichment_df[(enrichment_df['p_value']<=5e-10) & (enrichment_df['fdr']<=5e-8)]

filter_df = filter_df.sort_values('fdr', ascending=True)
filter_df = filter_df[["category", "preferredNames", "p_value", "fdr", "description"]]
cate = ['DISEASES', 'Function','HPO', 'WikiPathways']
filter_df = filter_df[filter_df["category"].isin(cate)]
print(filter_df)
filter_df.to_excel('enrique.xlsx')

