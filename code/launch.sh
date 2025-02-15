#!/bin/bash

####################
## Comentamos esto por que el archivo 9606.protein.links.v12.0.txt.zip es demasiado grande para github
# Descompresión del archivo 9606.protein.links.v12.0.txt.zip
# unzip ./9606.protein.links.v12.0.zip

# Filtrado del archivo 9606.protein.links.v12.0.txt
#awk -F" " '$3 > 800 {print $0}' 9606.protein.links.v12.0.txt > proteinas_filtrado.txt

#################### 

# Partimos de proteinas_filtrado.txt:

# Execute Python script to get the 51 gene network and their ids for DIAMOnD
python scripts/get_51_gene_network.py

# From the obtained genes ids, run DIAMOnD to enlarge the network to 200 genes
python scripts/DIAMOnD.py proteinas_filtrado.txt ../results/grafo_51_genes.txt 200 ../results/propaged_genes.txt

# Get a network with the 200 genes
python scripts/get_200_gene_network.py

# Community detection 
python scripts/community_detection.py

# Get greatest relation with others hpos
echo "Esto puede tardar unos minutos..."
python scripts/mas_relacionados.py
