#!/bin/bash

# Realizar un script para descargar el archivo 9606.protein.links.v12.0.txt desde stringdb
# ----aquí o incluir el código en get_51_gene_network.py

# Execute Python script to get the 51 gene network and their ids for DIAMOnD
python get_51_gene_network.py

# From the obtained genes ids, run DIAMOnD to enlarge the network to 200 genes
python DIAMOnD.py 9606.protein.links.v12.0.txt grafo_51_genes.csv 200 propaged_genes.txt

# Get a network with the 200 genes
python get_200_gene_network.py

# Community detection 
