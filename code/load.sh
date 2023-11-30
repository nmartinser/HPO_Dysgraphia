#!/bin/bash

# Descompresión del archivo 9606.protein.links.v12.0.txt.zip
unzip ./9606.protein.links.v12.0.zip

# Filtrado del archivo 9606.protein.links.v12.0.txt
awk -F" " '$3 > 800 {print $0}' 9606.protein.links.v12.0.txt > 9606.protein.links.v12.0.txt

# Execute Python script to get the 51 gene network and their ids for DIAMOnD
python get_51_gene_network.py

# From the obtained genes ids, run DIAMOnD to enlarge the network to 200 genes
python DIAMOnD.py 9606.protein.links.v12.0.txt grafo_51_genes.txt 200 propaged_genes.txt

# Get a network with the 200 genes
python get_200_gene_network.py

# Community detection 
