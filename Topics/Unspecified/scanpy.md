[[Single cell analysis]]

Single cell analysis를 위한 파이썬 패키지
Scanpy is a powerful Python library for single-cell RNA sequencing (scRNA-seq) analysis.

# Introduction to Scanpy

**Scanpy** is an open-source, scalable toolkit for analyzing single-cell gene expression data in Python ([Scanpy – Single-Cell Analysis in Python — scanpy](https://scanpy.readthedocs.io/#:~:text=Scanpy%20is%20a%20scalable%20toolkit,more%20than%20one%20million%20cells)). It provides a comprehensive suite of methods for **preprocessing**, **visualization**, **clustering**, **trajectory inference**, and **differential expression** analysis of single-cell RNA sequencing (scRNA-seq) data ([Scanpy – Single-Cell Analysis in Python — scanpy](https://scanpy.readthedocs.io/#:~:text=Scanpy%20is%20a%20scalable%20toolkit,more%20than%20one%20million%20cells)). Built on the efficient **AnnData** data structure (for “annotated data”), Scanpy can handle datasets with over a million single cells, making it suitable for large-scale studies ([Scanpy – Single-Cell Analysis in Python — scanpy](https://scanpy.readthedocs.io/#:~:text=Scanpy%20is%20a%20scalable%20toolkit,more%20than%20one%20million%20cells)). Scanpy was introduced by Wolf _et al._ (2018) as a Python counterpart to popular R-based tools (like Seurat) for single-cell analysis ([(PDF) SCANPY: Large-scale single-cell gene expression data analysis](https://www.researchgate.net/publication/322973402_SCANPY_Large-scale_single-cell_gene_expression_data_analysis#:~:text=SCANPY%20is%20a%20scalable%20toolkit,com%2Ftheislab%2Fanndata)) ([Hands-on: Filter, plot and explore single-cell RNA-seq data with Scanpy (Python) / Filter, plot and explore single-cell RNA-seq data with Scanpy (Python) / Single Cell](https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scrna-case-jupyter_basic-pipeline/tutorial.html#:~:text=McCarthy%20et%20al,widely%20used%20single%20cell%20toolkit)). It has since become widely used due to its performance and ability to integrate with the scientific Python ecosystem. Key features of Scanpy include an intuitive high-level API (`sc.pp`, `sc.tl`, `sc.pl` submodules for preprocessing, tools, and plotting), support for sparse data, and an extensive ecosystem of related packages (the **scverse** framework) for specialized tasks (e.g. **scvelo** for RNA velocity, **scirpy** for immune repertoires, etc.). In summary, Scanpy offers researchers a powerful and flexible platform to perform end-to-end single-cell analysis in Python.

# Installation

Scanpy can be installed via Python’s package managers or using Conda.

```bash
pip install scanpy
```

```bash
conda install -c conda-forge scanpy python-igraph leidenalg
```

# Workflow Overview

A typical scRNA-seq analysis workflow in Scanpy consists of several main steps: **data loading**, **quality control**, **normalization**, **feature selection and scaling**, **dimensionality reduction** (PCA), **clustering** (community detection on a kNN graph), **visualization** (embedding the clusters with UMAP or t-SNE), and **differential expression** analysis to identify marker genes. Below, we outline each step and demonstrate how to perform them with Scanpy. Throughout, we assume you have loaded your data into an AnnData object (Scanpy’s primary data container for observations × variables). We will use a small example dataset (3k Peripheral Blood Mononuclear Cells) to illustrate the code for each step, but you can replace this with your own dataset.

## Data Loading

Single-cell count data can be loaded into Scanpy’s **AnnData** object from various formats. Commonly, scRNA-seq data comes from 10x Genomics, which Scanpy can read using functions like `sc.read_10x_mtx` or `sc.read_10x_h5` (for Matrix Market files or 10x HDF5 files) ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=adata%20%3D%20sc.read_10x_mtx%28%20,symbols%20for%20the%20variable%20names)). You can also load data from text/CSV, Excel, Loom files, or directly from a pandas DataFrame using `anndata.AnnData`. The AnnData object holds the gene expression matrix (`adata.X`) along with cell metadata (`adata.obs`) and gene metadata (`adata.var`) ([(PDF) SCANPY: Large-scale single-cell gene expression data analysis](https://www.researchgate.net/publication/322973402_SCANPY_Large-scale_single-cell_gene_expression_data_analysis#:~:text=SCANPY%20is%20a%20scalable%20toolkit,com%2Ftheislab%2Fanndata)). For example, to read a filtered 10x dataset one might do:

```python
import scanpy as sc
# Example: Load a 10x Genomics dataset from a directory (e.g., with matrix.mtx and barcodes)
adata = sc.read_10x_mtx("path/to/filtered_gene_bc_matrices/hg19/", var_names="gene_symbols", cache=True)
```

In this example, `var_names="gene_symbols"` tells Scanpy to use gene symbols as gene names instead of Ensembl IDs ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=adata%20%3D%20sc.read_10x_mtx%28%20,symbols%20for%20the%20variable%20names)). As a quick alternative for practice, Scanpy provides built-in example datasets. For instance, you can load a 3k PBMC dataset with:

```python
adata = sc.datasets.pbmc3k()  # loads a 3k PBMCs dataset as an AnnData object
print(adata.shape)
```

This will download and return an AnnData with 2700 cells (observations) × 33,000 genes (variables) ([4. Analysis frameworks and tools — Single-cell best practices](https://www.sc-best-practices.org/introduction/analysis_tools.html#:~:text=adata%20%3D%20sc)). After loading, it’s good to examine `adata.obs` (cell metadata) and `adata.var` (gene metadata) to confirm the contents (e.g., total counts per cell, gene IDs, etc.).

## Quality Control (Filtering)

Quality control is critical to remove low-quality cells and genes before analysis. Common QC steps include filtering out cells with very few detected genes (potential empty droplets) or extremely high gene counts (potential doublets), and removing genes that are not expressed in enough cells. You may also filter cells with a high percentage of mitochondrial gene counts, as these often indicate damaged cells. Scanpy can compute QC metrics and apply such filters:

```python
# Filter out cells with fewer than 200 genes expressed
sc.pp.filter_cells(adata, min_genes=200)
# Filter out genes expressed in fewer than 3 cells
sc.pp.filter_genes(adata, min_cells=3)
```

In our example dataset, this would remove cells that have less than 200 genes detected and drop genes seen in less than 3 cells ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). Next, we identify mitochondrial genes (which in many gene annotations start with "MT-") and calculate the percentage of mitochondrial counts per cell:

```python
# Annotate mitochondrial genes:
adata.var['mt'] = adata.var_names.str.startswith('MT-')
# Calculate QC metrics (adds metrics like pct_counts_mt to adata.obs)
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, inplace=True)
```

This adds, for each cell, metadata such as `n_genes_by_counts` (number of genes detected), `total_counts`, and `pct_counts_mt` (percentage of counts from mitochondrial genes) ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=,percent_top%3DNone%2C%20log1p%3DFalse%2C%20inplace%3DTrue)). We can then filter out cells that have too high mitochondrial fraction or an unusually high gene count:

```python
# Filter out cells with >2500 genes or >5% mitochondrial counts
adata = adata[adata.obs.n_genes_by_counts < 2500, :]
adata = adata[adata.obs.pct_counts_mt < 5, :]
```

These thresholds (e.g., drop cells with more than 2,500 genes or more than 5% of reads mitochondrial) are commonly used defaults ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=adata%20%3D%20adata%5Badata.obs.n_genes_by_counts%20,5%2C%20%3A%5D.copy)), but they should be adjusted based on your dataset’s characteristics. After filtering, the dataset (`adata`) contains only high-quality cells and genes. It’s often useful to save the filtered data or at least note the number of cells/genes retained.

## Normalization and Scaling

After QC, the raw UMI counts need to be normalized to make cells comparable. A typical approach is **library-size normalization**: scale each cell’s counts so that each cell has the same total count (e.g., 10,000) and then log-transform the data. In Scanpy, this is done as:

```python
sc.pp.normalize_total(adata, target_sum=1e4)  # normalize each cell to total counts of 1e4
sc.pp.log1p(adata)  # log-transform the data (log(1 + counts))
```

Library size normalization divides each cell’s counts by the total counts for that cell, multiplying by the `target_sum` (10,000) ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). The `sc.pp.log1p` applies natural log to each value (after adding 1) ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)), which stabilizes variance and makes the data more normally distributed for downstream analysis.

Next, it’s common to perform **feature selection** by identifying highly variable genes (HVGs). These are genes with high cell-to-cell variation, which are often informative for clustering. Scanpy provides `sc.pp.highly_variable_genes` to flag HVGs:

```python
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
```

This calculates the mean and dispersion for each gene and marks a subset as highly variable (stored as `adata.var['highly_variable']`) using the specified cutoffs ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). We can then subset the data to include only these HVGs for downstream analyses:

```python
adata = adata[:, adata.var.highly_variable]  # keep only highly variable genes
```

Optionally, Scanpy allows regression of unwanted sources of variation (for example, cell cycle scores, or the total counts and percentage mitochondrial content) using `sc.pp.regress_out`. For instance, one could regress out the `total_counts` and `pct_counts_mt` effects if needed ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=match%20at%20L248%20sc.pp.regress_out%28adata%2C%20%5B,pct_counts_mt)). After that, we **scale** the data (usually z-score each gene across cells):

```python
sc.pp.scale(adata, max_value=10)
```

Scaling ensures each gene has mean ~0 and variance ~1, which is important for PCA. The `max_value=10` argument caps gene expression values to avoid extreme outliers after scaling ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). It’s worth noting that Scanpy by default stores the **log-normalized** data in `adata.X`. If you want to preserve raw counts or the normalized-but-unscaled data for later (e.g., for differential expression), you can store a copy in `adata.raw` before scaling:

```python
adata.raw = adata.copy()
```

This way, the non-regressed, non-scaled expression values are saved for use in plotting and DE tests later ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=adata)).

## Principal Component Analysis (PCA)

The next step is **dimensionality reduction** to capture the most important variation in the data. Scanpy uses Principal Component Analysis (PCA) as a first step to reduce the high-dimensional gene expression matrix into a smaller set of principal components (PCs). PCA helps denoise the data and is the basis for constructing neighborhood graphs for clustering. To perform PCA on the filtered, normalized, and scaled data:

```python
sc.tl.pca(adata, n_comps=50, svd_solver='arpack')
```

This computes the top 50 principal components of the data ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc.tl.pca%28adata%2C%20svd_solver%3D)) and stores the result in `adata.obsm['X_pca']` (the PC scores for each cell) and `adata.varm['PCs']` (the loadings for each gene on those PCs). You can inspect `adata.obsm['X_pca']` to see the reduced coordinates. It’s also common to examine the variance explained by PCs (e.g., with `sc.pl.pca_variance_ratio`) to decide how many PCs to use in downstream steps. In practice, one might choose the top 10–50 PCs that capture most variance as input for clustering algorithms ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=function%20,number%20of%20PCs%20does%20fine)). (In our example, we used 50 components; often fewer are sufficient.)

## Clustering

**Clustering** aims to group cells into discrete clusters (putative cell types or states) based on their gene expression profiles. Scanpy uses graph-based clustering similar to methods in Seurat: first, build a k-nearest-neighbor (kNN) graph of cells in the PCA space, then apply a community detection algorithm (like Louvain or Leiden) on this graph. The typical steps are:

1. **Neighborhood graph computation** – This finds each cell’s nearest neighbors in the PCA space and constructs a graph. For example:
    
    ```python
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
    ```
    
    This computes the neighbor graph using the first 40 PCs and 10 nearest neighbors for each cell ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). The graph info is stored in `adata.obsp['distances']` and `'connectivities'` (distance and adjacency matrices).
    
2. **Community detection (clustering)** – With the graph, we can find communities of cells. Scanpy supports the **Louvain** algorithm (older default) and **Leiden** algorithm (recommended for more consistency). For example, using Leiden clustering:
    
    ```python
    sc.tl.leiden(adata, resolution=0.5)
    ```
    
    This will cluster the cells and add a categorical label `adata.obs['leiden']` with cluster assignments ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). The `resolution` parameter controls the granularity of clustering (higher resolution = more clusters) – you can adjust it to get an appropriate number of clusters for your data. Each cluster is essentially a group of cells that are more connected to each other in the kNN graph than to the rest of the cells. (If desired, you could use `sc.tl.louvain` similarly; Leiden is generally preferred as it’s an improved method.)
    

After this step, you should have cluster labels for each cell. You can check the sizes of clusters (e.g., `adata.obs['leiden'].value_counts()`) and proceed to interpret them. Often, one might iterate: compute neighbors and clustering with different parameters, or even run **graph-based pseudotime** (Scanpy’s `tl.paga`) before final clustering if doing trajectory analysis – but for a standard workflow, the above suffices to get cluster assignments.

## Visualization (UMAP and t-SNE)

Visualization of high-dimensional data is typically done by projecting cells into 2D. **UMAP** (Uniform Manifold Approximation and Projection) and **t-SNE** are two popular non-linear dimensionality reduction techniques for visualizing single-cell data. Scanpy can compute these embeddings after the neighbor graph is prepared:

- **UMAP**:
    
    ```python
    sc.tl.umap(adata)
    ```
    
    This computes a 2D UMAP embedding of the cells (stored in `adata.obsm['X_umap']`) based on the neighbor graph ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc)). UMAP tends to preserve both local and some global structure of the data and is widely used for scRNA-seq.
    
- **t-SNE**:
    
    ```python
    sc.tl.tsne(adata, n_pcs=40)
    ```
    
    This computes a t-SNE embedding (stored in `adata.obsm['X_tsne']`), using PCA components as input. t-SNE is older and emphasizes local neighbor relations; it can sometimes split clusters more exaggeratedly than UMAP.
    

After computing an embedding, we can plot the cells in 2D and color them by cluster or other metadata. Scanpy’s plotting module makes this easy:

```python
sc.pl.umap(adata, color='leiden')
```

This will produce a UMAP scatter plot of all cells, colored by their Leiden cluster labels ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc.pl.umap%28adata%2C%20color%3D%5B)). Each point is a cell, and clusters should appear as distinct groups of points. You can also color by gene expression or other annotations (for example, `sc.pl.umap(adata, color=['leiden', 'MS4A1'])` would show clusters and highlight the expression of **MS4A1**). Similarly, `sc.pl.tsne(adata, color='leiden')` would plot a t-SNE. These visualizations are crucial for interpreting the clustering results — for instance, seeing if known cell types separate into different clusters, or if there are gradients suggesting continuous transitions.

_(In a Jupyter notebook or interactive environment, these plots will display inline. In a script, you might need to save them to files via arguments like `save="fig.png"`.)_

## Differential Expression Analysis

Once clusters are identified, a common step is to find **marker genes** for each cluster – genes that are significantly higher in one group of cells compared to others. Scanpy provides `sc.tl.rank_genes_groups` for differential expression (DE) testing between groups. This function can perform tests (Wilcoxon rank-sum, t-tests, logistic regression, etc.) to rank genes for each cluster versus all other cells (or versus a specific cluster). For example:

```python
# Identify marker genes for each Leiden cluster using the Wilcoxon rank-sum test
sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon')
```

This will compute, for each cluster in the `'leiden'` category, a set of ranked genes that are most differentially expressed in that cluster compared to the rest ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc.tl.rank_genes_groups%28adata%2C%20,sharey%3DFalse)). The results are stored in `adata.uns['rank_genes_groups']` (with fields for scores, p-values, etc. for each cluster). You can inspect the top genes per cluster by, for instance:

```python
# Get the top 5 genes for each cluster
import pandas as pd
pd.DataFrame(adata.uns['rank_genes_groups']['names']).head(5)
```

Or use Scanpy’s plotting function to visualize the results:

```python
sc.pl.rank_genes_groups(adata, n_genes=5, sharey=False)
```

This will show a plot of the top 5 marker genes for each cluster and their scores ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc.tl.rank_genes_groups%28adata%2C%20%22leiden%22%2C%20method%3D%22t,sharey%3DFalse)). Marker gene identification helps in assigning biological identities to clusters (e.g., a cluster with high **MS4A1** and **CD79A** might be B cells). It’s important to note that by default `rank_genes_groups` uses the `.raw` attribute of AnnData if it’s set (which typically contains the normalized counts before scaling), so that the DE is calculated on meaningful expression values rather than scaled or PCA-reduced data. You can specify parameters like `reference` to do pairwise comparisons (e.g., one cluster vs another) if needed ([Preprocessing and clustering 3k PBMCs (legacy workflow) — scanpy-tutorials 0.1.dev50+g860745c documentation](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#:~:text=sc.tl.rank_genes_groups%28adata%2C%20,n_genes%3D20)).

With differential expression results, you would validate and annotate clusters according to known cell type markers or novel markers of interest. This often completes a first-pass analysis of an scRNA-seq dataset.

# Comparison with Other Tools

Scanpy is often compared to **Seurat** (an R-based single-cell analysis package) and other frameworks. In terms of core functionality, Scanpy and Seurat offer very similar workflows – both cover data filtering, normalization, HVG selection, PCA, clustering, UMAP/t-SNE, and marker detection, and both have methods for batch correction and data integration. The choice between them often comes down to the user’s preferred programming language (Python vs R) and specific features:

- **Performance and Scalability**: Scanpy is designed to efficiently handle large datasets (millions of cells) with optimized memory usage and speed (leveraging sparse matrices and numpy operations) ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=)). Many users report that Scanpy is faster on large data than Seurat, which can become memory-intensive in R ([Scanpy from python or seurat from R single cell Rna seq : r/bioinformatics](https://www.reddit.com/r/bioinformatics/comments/16dhi6y/scanpy_from_python_or_seurat_from_r_single_cell/#:~:text=%E2%80%A2)) ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=)). Seurat has improved over the years and can also handle large data, but Python’s performance (and options to use GPUs via libraries like rapids-singlecell) can give Scanpy an edge for very big datasets ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=)).
    
- **Usability and Ecosystem**: Seurat is known for its user-friendly interface and comprehensive documentation, which is great for R users ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=)). It integrates well with **ggplot2** for plotting, making it easy to produce publication-quality figures. Scanpy, being in Python, is favored by those who work in the Python scientific stack and want integration with libraries like pandas, NumPy/SciPy, scikit-learn, etc. Scanpy’s API is quite straightforward, but it may have a slightly steeper learning curve if you’re not familiar with Python (and Jupyter notebooks) ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=,Highly%20customizable%20analysis%20workflows)). The AnnData object in Scanpy is analogous to Seurat’s object (both store assay data and metadata), but some users find AnnData’s design (with `.obs`, `.var`, etc.) more transparent and “less weird” than Seurat’s S4 class structure ([Scanpy from python or seurat from R single cell Rna seq : r/bioinformatics](https://www.reddit.com/r/bioinformatics/comments/16dhi6y/scanpy_from_python_or_seurat_from_r_single_cell/#:~:text=%E2%80%A2)).
    
- **Functionality**: Both tools offer a rich set of methods. Seurat has pioneered methods like **SCTransform** normalization and advanced batch integration techniques (CCA, Harmony, etc.) and has a large ecosystem of extensions in R. Scanpy, on the other hand, is modular and part of the **scverse** ecosystem – it may rely on external packages for certain functionality (for example, **scanorama** or **BBKNN** for batch correction, **scvi-tools** for deep learning-based integration, **CellRank** for fate prediction, etc.), which can be used alongside Scanpy. In practice, anything you can do in Seurat can be done in Scanpy with the right combination of Python tools. Scanpy also includes novel approaches like **PAGA** for coarse-grained trajectory inference. When it comes to **trajectory analysis**, R packages like **Monocle** or **slingshot** are often used, but Scanpy can perform pseudotime analyses and connects to specialized tools (like scvelo for RNA velocity) in Python. Visualization capabilities are extensive in both (Scanpy uses Matplotlib/Seaborn; Seurat uses ggplot2) – Scanpy’s plots are highly customizable through Matplotlib if needed, while Seurat’s defaults are aesthetically pleasing and easy to tweak for those familiar with R plotting ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=,quality%20figures%20for%20publication)) ([Scanpy vs Seurat: Two Powerhouses for Single Cell RNA-seq Data Analysis - Data Science For Bio](https://datascienceforbio.com/scanpy-vs-seurat/#:~:text=)).
    

In summary, **Scanpy vs Seurat** is not about which is “better” overall – both are powerful. Scanpy might be preferable if you’re working in Python, need to scale to very large data, or want to leverage Python’s machine learning libraries. Seurat might be preferable if you are embedded in the R ecosystem or prefer its out-of-the-box methods for certain tasks. Many analyses have shown that results from Scanpy and Seurat are comparable, though default parameter choices can lead to some differences ([The impact of package selection and versioning on single-cell RNA ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC11014608/#:~:text=The%20impact%20of%20package%20selection,HVG%20selection%20analysis%20UpSet)). Other tools like **Scater/Scran** (R/Bioconductor) or **SingleCellToolkit** also exist, but Seurat and Scanpy remain the most widely used toolkits in their respective languages. Some researchers even use both: for example, using Scanpy for initial processing and then Seurat for specific visualization, or vice versa, since AnnData and Seurat objects can be converted via formats like Loom or h5ad. Ultimately, the choice may depend on familiarity and the specific features needed for a project.

# Resources and Further Learning

For those looking to learn more about Scanpy and single-cell analysis, here are some helpful resources:

- **Official Scanpy Documentation** – The Scanpy documentation site (ReadTheDocs) is the best place to start ([Scanpy – Single-Cell Analysis in Python — scanpy](https://scanpy.readthedocs.io/#:~:text=The%20tutorials%20walk%20you%20through,world%20applications%20of%20scanpy)). It contains an overview of Scanpy’s functionality, detailed API reference, and **tutorials**. Notably, the “Preprocessing and clustering 3k PBMCs” tutorial is a step-by-step notebook that reproduces a basic single-cell analysis workflow, which is great for beginners.
    
- **Tutorials and Workshops** – The scverse project provides a curated set of single-cell analysis tutorials (using Scanpy and related tools) at _scverse.org/learn_ ([Tutorials — scanpy](https://scanpy.readthedocs.io/en/stable/tutorials/index.html#:~:text=See%20also)). These include case studies and workflows on various topics (integration, trajectory inference, spatial data, etc.). Additionally, platforms like **Galaxy Training** materials ([Hands-on: Filter, plot and explore single-cell RNA-seq data with Scanpy (Python) / Filter, plot and explore single-cell RNA-seq data with Scanpy (Python) / Single Cell](https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scrna-case-jupyter_basic-pipeline/tutorial.html#:~:text=insights%21%20There%20are%20many%20packages,widely%20used%20single%20cell%20toolkit)) and online courses often feature Scanpy tutorials. For example, the Galaxy training “Filter, Plot and Explore single-cell RNA-seq data with Scanpy” is a hands-on tutorial covering the basics.
    
- **Scanpy Paper and References** – The original Scanpy publication by Wolf _et al._ 2018 in _Genome Biology_ is a useful reference for the methods and design philosophy ([(PDF) SCANPY: Large-scale single-cell gene expression data analysis](https://www.researchgate.net/publication/322973402_SCANPY_Large-scale_single-cell_gene_expression_data_analysis#:~:text=SCANPY%20is%20a%20scalable%20toolkit,com%2Ftheislab%2Fanndata)). It details the algorithmic steps and also introduces AnnData. Citing this paper is recommended if you use Scanpy in published research. Furthermore, the Scanpy documentation’s _References_ section lists relevant papers for the algorithms implemented (e.g., the Leiden algorithm paper, etc.).
    
- **Community and Support** – Scanpy is actively developed as part of the scverse community. You can ask questions or find answers on the **scverse discourse forum** (community forum) ([Scanpy – Single-Cell Analysis in Python — scanpy](https://scanpy.readthedocs.io/#:~:text=Discuss%20usage%20on%20the%20scverse,look%20at%20our%20%20298)), or on Q&A sites like Biostars/StackExchange. The Scanpy GitHub page is also active for reporting issues. Additionally, there are **tutorial videos** and blog posts by users that walk through Scanpy workflows (search for “Scanpy tutorial” on YouTube or blogs like _Data Science for Bio_). Engaging with the community will help you stay updated on best practices (for instance, new normalization methods or integration techniques as they emerge).
    
- **Seurat to Scanpy Guides** – If you come from a Seurat background, you might find guides comparing Seurat and Scanpy workflows useful. Some blog posts and notebooks outline how to translate common Seurat steps into Scanpy code, which can accelerate the learning process.
    

By utilizing these resources – documentation, tutorials, papers, and community forums – you can deepen your understanding of single-cell analysis with Scanpy and stay current with the evolving **scRNA-seq** analysis landscape. Scanpy, combined with the broader scverse ecosystem, continues to grow, so there’s always more to learn, from basic clustering to advanced topics like multi-omics integration and RNA velocity. Good luck with your single-cell analysis!