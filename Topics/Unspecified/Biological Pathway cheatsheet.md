
## Quick Reference for Pathway Visualization Types

|Pathway Type|Best Visualization|Common Tools|Key Features|
|---|---|---|---|
|Metabolic|Flowcharts, Node-Edge|KEGG, MetaCyc, BioCyc|Enzyme reactions, metabolites, cofactors|
|Signaling|Node-Edge, Process Diagrams|Reactome, KEGG, GenMAPP|Protein interactions, activation/inhibition|
|Gene Regulatory|Directed Networks|BioTapestry, GRNsight|Transcription factors, promoters, binding sites|
|Protein-Protein Interaction|Force-directed Networks|Cytoscape, STRING|Protein complexes, physical interactions|

## Common Notation Systems

### SBGN (Systems Biology Graphical Notation)

- **Process Description (PD)**: Detailed biochemical/molecular events
- **Entity Relationship (ER)**: Influences between entities without mechanisms
- **Activity Flow (AF)**: Simplified activation/inhibition relationships

### Standard Symbols

- **Rectangles**: Genes, proteins, or macromolecules
- **Circles/Ovals**: Small molecules, metabolites
- **Arrows**: Reactions, conversions, transport
- **T-bars**: Inhibition
- **Diamonds**: Branch points or decisions

## Top Visualization Tools & Resources

### Web-Based Tools

- **KEGG Pathway**: Comprehensive metabolic and signaling pathways
- **Reactome**: Curated peer-reviewed pathway diagrams
- **WikiPathways**: Community-curated pathway collection
- **PathVisio**: Pathway drawing and analysis
- **STRING**: Protein-protein interaction networks
- **iPath**: Interactive pathway explorer

### Desktop Software

- **Cytoscape**: Network analysis and visualization
    - Key plugins: BiNGO, clusterMaker, enhancedGraphics
- **Gephi**: Large-scale network visualization
- **CellDesigner**: Process diagram editor (SBGN compliant)
- **VANTED**: Metabolic network analysis

### R Packages

- **pathview**: KEGG pathway visualizer
- **RCy3**: Cytoscape automation in R
- **igraph**: Network analysis and visualization
- **ggraph**: Grammar of graphics for networks
- **visNetwork**: Interactive network visualization

### Python Libraries

- **NetworkX**: Network creation and analysis
- **py2cytoscape**: Python to Cytoscape bridge
- **libSBGN**: SBGN manipulation library
- **BioPython**: General bioinformatics toolkit
- **RDkit**: Cheminformatics and visualization

## Practical Guidelines

### Color Schemes

- **Metabolites**: Blue/purple
- **Enzymes/Proteins**: Green
- **Genes**: Yellow/orange
- **Reactions**: Red/pink
- **Up-regulation**: Red gradient
- **Down-regulation**: Blue gradient

## Common File Formats

- **SBML**: Systems Biology Markup Language
- **BioPAX**: Biological Pathway Exchange
- **SBGN-ML**: SBGN Markup Language
- **GraphML**: General graph markup
- **XGMML**: eXtensible Graph Markup and Modeling Language
- **SIF**: Simple Interaction Format
- **KGML**: KEGG Markup Language

## Recently Emerging Standards (2023-2024)

- **Neo4j Biological Graph Database**: Standardizing graph database schemas for biological pathways
- **ReactomeGSA**: Integrated pathway analysis for multi-omics data
- **CellMaps**: Interactive visualization of cellular pathways in spatial context
- **BioRender Pathway Builder**: Standardized biological diagrams with scientific accuracy

## Example Commands

### Cytoscape Network Import

```
File → Import → Network → From File...
```

### R Pathview Example

```r
library(pathview)
data <- read.csv("expression_data.csv", row.names=1)
pathview(gene.data=data, pathway.id="hsa04010", species="hsa")
```

### Python NetworkX Example

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([("Gene A", "Protein B"), ("Protein B", "Metabolite C")])
nx.draw(G, with_labels=True, node_color="lightblue", arrows=True)
plt.savefig("pathway.png", dpi=300)
```