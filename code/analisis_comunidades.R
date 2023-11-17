# Librerias
suppressMessages(library(igraph))
suppressMessages(library(this.path))

# Establecer Working directory
setwd(dirname(sys.frame(1)$ofile))

## Borrar variables de R
rm(list=ls())

# Creación de grafo
graph <- graph.data.frame(read.csv("grafo_17_genes.csv", sep="\t"), directed = TRUE)

pdf(file="../results/Red_de_genes_Original.pdf")
plot(graph, edge.arrow.size=0.2, edge.curved=0.1, vertex.size=15, vertex.color="white", vertex.frame.color="black", vertex.label.color="black",vertex.label.cex=0.4)

V(graph)
