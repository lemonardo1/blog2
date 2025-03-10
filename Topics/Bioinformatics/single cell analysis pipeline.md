## scRNA-seq 분석 핵심 워크플로우

Single-cell RNA sequencing(**scRNA-seq**) 데이터 분석에서는 raw 데이터로부터 유의미한 생물학적 insight를 얻기까지 여러 단계의 **표준 워크플로우**가 존재합니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=covering%20essential%20steps%20like%20quality,ensuring%20reliable%20results%20across%20experiments)). 여기서는 최신 연구 동향을 반영하여, scRNA-seq 분석의 핵심 단계들을 순차적으로 설명하고 각 단계별로 Python(예: **Scanpy** 라이브러리) 코드 예제를 제시합니다.

([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746)) _Figure: 전형적인 scRNA-seq 분석 워크플로우. 시퀀싱 후 얻은 count matrix에 대해 좌측의 **전처리**(QC, 정규화, feature selection 등) 단계를 거쳐, 우측의 **다운스트림 분석**(차원축소 및 클러스터링, marker 기반 Annotation, 시각화 등)을 수행한다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Figure%201,typical%20single%E2%80%90cell%20RNA%E2%80%90seq%20analysis%20workflow)) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Raw%20data%20generated%20by%20sequencing,genome%20alignment%2C%20and))._

## 1. 데이터 전처리 (Data Preprocessing)

**Data Preprocessing** 단계에서는 원시 count 데이터를 정제하여 분석에 적합한 형태로 만들어줍니다. 주로 **Quality Control (QC)**, **Filtering**, **Normalization** 등의 순서로 진행됩니다.

- **Quality Control (QC)**: 개별 세포들의 품질 지표를 계산하여 저품질 셀을 찾아냅니다. 일반적으로 세포별 **총 UMI counts**, **검출된 gene 수**, **미토콘드리아 유전자 비율** 등의 QC 지표를 사용하며, 분포 상 **극단적인 outlier**에 해당하는 셀들을 걸러냅니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Before%20analysing%20the%20single%E2%80%90cell%20gene,fraction%20of%20mitochondrial%20counts%20are)). 예를 들어 **counts**와 **gene 수**가 지나치게 낮고 **mito 비율**이 높은 셀은 파손된 세포로 간주하여 제거하고, 반대로 **counts**와 **gene 수**가 비정상적으로 높은 셀은 이중 포획된 세포(**doublet**)로 의심합니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=count%20depth%2C%20few%20detected%20genes%2C,Doublet%20Finder%3A%20McGinnis%20et%C2%A0al%2C%202018)). 최신 워크플로우에서는 **Scrublet**, **DoubletFinder** 등의 **이중세포 탐지** 도구를 활용하여 doublet을 보다 정교하게 제거하기도 합니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=membrane%2C%20and%20thus%2C%20only%20mRNA,Doublet%20Finder%3A%20McGinnis%20et%C2%A0al%2C%202018)).
    
- **Filtering**: QC 결과에 따라 결정한 임계값(threshold)에 기반해 **셀 및 유전자 필터링**을 수행합니다. 예를 들어, 일정 기준 이하의 gene을 가진 셀이나 mito 비율이 높은 셀을 제거하고, 극히 소수의 셀에서만 발현된 유전자도 제외합니다. 이러한 필터링을 통해 **죽은 세포나 빈 액적** 등 생물학적 신뢰도가 낮은 데이터 포인트를 제거하여 다운스트림 분석의 신뢰성을 높입니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Before%20analysing%20the%20single%E2%80%90cell%20gene,fraction%20of%20mitochondrial%20counts%20are)). (필요시, **빈 드롭릿**으로부터 오는 배경 노이즈를 차단하거나 ambient RNA 보정을 하는 등의 추가 정제도 적용할 수 있습니다.)
    
- **Normalization**: 서로 다른 셀 간 **라이브러리 사이즈(시퀀싱 깊이)** 차이를 보정하기 위해 **정규화**를 수행합니다. 일반적인 방법은 **글로벌 스케일링**으로, 모든 셀의 total counts를 동일한 기준으로 스케일한 후 **로그 변환(log1p)**하여 데이터 분포를 안정화시킵니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=these%20steps,gene%20expression%20abundances%20between%20cells)). 정규화를 통해 세포 간 **상대적 유전자 발현량**이 비교 가능하게 조정되며, 샘플링으로 인한 차이를 보정할 수 있습니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Normalization%20addresses%20this%20issue%20by,gene%20expression%20abundances%20between%20cells)). 최근에는 Seurat의 **SCTransform**이나 Bioconductor의 **scran**처럼 **모델 기반 정규화** 방법이 도입되어 기술 노이즈를 보다 효과적으로 제거하고 변이를 안정화하는 추세입니다. (예: **SCTransform**은 회귀모델로 UMI counts를 보정하고 variance stabilization을 함께 수행합니다.)
    

아래는 Python **Scanpy**를 이용하여 **QC, 필터링, 정규화**를 간단히 수행하는 예시입니다:

```python
import scanpy as sc

# 예시 데이터 불러오기 (10x Genomics 형식 가정)
adata = sc.read_10x_mtx("sample1_filtered_feature_bc_matrix/")

# 세포 및 유전자 필터링
sc.pp.filter_cells(adata, min_genes=200)    # 세포 당 최소 200개 유전자
sc.pp.filter_genes(adata, min_cells=3)     # 3개 미만 셀에서 검출된 유전자 제거

# QC 지표 계산 (예: 미토콘드리아 유전자 비율)
adata.var['mt'] = adata.var_names.str.startswith('MT-')
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)
# QC 기준에 따라 저품질 세포 제거 (예: MT 비율 5% 초과 셀 제거)
adata = adata[adata.obs.pct_counts_mt < 5, :]

# 라이브러리 크기 정규화 및 로그 변환
sc.pp.normalize_total(adata, target_sum=1e4)  # 셀마다 총 counts를 1만으로 스케일링
sc.pp.log1p(adata)  # log(1+x) 변환으로 분포 압축
```

> **참고:** 실제 QC 단계에서는 상자 그림이나 히스토그램 등을 통해 QC 지표들의 분포를 시각화하고 임계값을 결정합니다. 또한 doublet 검출을 위해 `scrublet` 패키지를 활용하여 `adata.obs`에 doublet 확률을 추가하고 cut-off를 적용하는 식으로 이중세포를 제거할 수도 있습니다.

## 2. 클러스터링 (Clustering)

전처리가 완료된 데이터에 대해 **세포 군집화(clustering)**를 수행하여 **유사한 발현 패턴을 가진 세포 그룹**을 식별합니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=covering%20essential%20steps%20like%20quality,ensuring%20reliable%20results%20across%20experiments)). 클러스터링 단계는 보통 **특징 선택(feature selection)**, **차원 축소(dimension reduction)**, 그리고 **군집 알고리즘** 적용 순으로 이루어집니다.

- **Feature Selection (고변이 유전자 선택)**: 전체 유전자 중 **높은 변이를 보이는 유전자(Highly Variable Genes, HVGs)**만 선택하여 이후 분석에 사용합니다. HVG 선택은 기술 잡음보다 **생물학적 차이**를 잘 반영하는 유전자에 초점을 맞추기 위한 것으로, 통상적으로 변이계수(CV)나 분산 대비 평균값을 이용해 상위 1,000~3,000개 유전을 선정합니다. 이렇게 하면 차원 축소와 클러스터링의 **계산 효율**이 높아지고, 노이즈에 의한 군집 교란을 줄일 수 있습니다. _(팁: 정규화 이후 **Scaling(표준화)** 및 HVG 선정 시, 이미 데이터가 log1p 등으로 변환되었다면 분산 계산 방법에 유의합니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=%E2%80%A2)).)_
    
- **Dimensionality Reduction**: 선택된 특징 유전자 공간(수천 차원)을 저차원으로 투영하여 **주요한 변이 구조**를 추출합니다. 가장 널리 쓰이는 방법은 **주성분 분석(PCA)**으로, 데이터 공분산을 최대한 설명하는 **주성분(pc)**들을 계산하여 50개 내외의 차원으로 줄입니다. PCA 결과로 얻어진 **주성분 점수**는 이후 군집화 알고리즘의 입력으로 사용됩니다. (필요에 따라 t-SNE, UMAP 등의 **비선형 차원축소**도 적용 가능하지만, 이는 주로 시각화용으로 활용되며 클러스터 검출 자체는 PCA 기반으로 충분합니다.)
    
- **Clustering Algorithm**: 차원축소된 표현(PCA 좌표 등)을 사용하여 **세포 군집**을 식별합니다. 일반적으로 **최근접 이웃 그래프(Nearest-Neighbor Graph)** 기반의 **커뮤니티 탐지 알고리즘**을 적용하는데, 대표적으로 **Louvain**과 **Leiden** 방법이 널리 쓰입니다. **Leiden 알고리즘**은 Louvain 방법을 개선한 것으로, 더 **안정적이고 일관된 클러스터**를 생성하기 때문에 현재 single-cell 분석에서 **표준 옵션**으로 권장됩니다 ([scanpy.tl.leiden — scanpy](https://scanpy.readthedocs.io/en/stable/generated/scanpy.tl.leiden.html#:~:text=Cluster%20cells%20into%20subgroups%20,%2C%202019)). 분석자는 **해당 그래프의 해상도(resolution) 파라미터**를 조정하여 얻고자 하는 클러스터의 크기(갯수)를 컨트롤할 수 있습니다. 클러스터링 결과로 각 세포에 클러스터 ID(Label)가 부여되며, 이는 잠재적인 세포 아형(subpopulation)을 의미합니다. (_참고:_ 클러스터의 “정답 개수”는 존재하지 않으며, 해상도에 따라 세분화 정도가 달라집니다. 주어진 목적에 맞게 클러스터링 결과를 **재귀적으로 세분화**하거나 통합적으로 볼 수 있습니다.)
    

아래는 **Scanpy**를 이용한 **특징 유전자 선택, PCA 및 Leiden 클러스터링** 코드 예시입니다 (위 `adata` 이어서 수행):

```python
# 고변이 유전자 선택 (상위 2000개 변이 유전자 선택)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
adata = adata[:, adata.var.highly_variable]  # HVGs만 subset

# PCA 차원축소 (예: 주요 50개 PC 계산)
sc.pp.pca(adata, n_comps=50, use_highly_variable=True, svd_solver='arpack')

# 최근접 이웃 그래프 구성 (통상 PCA score 기반)
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=50)

# Leiden 군집화 실행 (예: resolution=0.5)
sc.tl.leiden(adata, resolution=0.5)
print(adata.obs['leiden'].value_counts())  # 각 클러스터에 속한 셀 수 출력
```

> **참고:** `sc.pp.neighbors`는 PCA 공간에서 셀들 간 k-Nearest Neighbors 그래프를 만들고, `sc.tl.leiden`은 그 그래프 상에서 커뮤니티 검출을 수행하여 `adata.obs['leiden']`에 클러스터 레이블을 저장합니다. 기본적으로 Leiden은 Louvain보다 향상된 방식으로 single-cell 데이터에 적용됩니다 ([scanpy.tl.leiden — scanpy](https://scanpy.readthedocs.io/en/stable/generated/scanpy.tl.leiden.html#:~:text=Cluster%20cells%20into%20subgroups%20,%2C%202019)).

## 3. Annotation (셀 타입 주석)

클러스터링으로 얻어진 각각의 세포 군집에 **생물학적 의미**를 부여하는 과정이 **Annotation** 단계입니다. 즉, 각 클러스터를 어떤 **셀 타입 또는 상태(cell type or state)**에 해당하는지 해석하게 됩니다 ([Chapter 5 Clustering | Basics of Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.14/OSCA.basic/clustering.html#:~:text=Clustering%20is%20an%20unsupervised%20learning,as%20cell%20types%20or%20states)). 이를 위해 **marker gene 분석**을 통해 클러스터 특이적 유전자를 찾아내고, 이를 기존의 생물학적 지식과 대조합니다.

- **Marker Gene Identification**: 클러스터별로 **특이적으로 발현되는 유전자(마커 유전자)**를 찾아냅니다. 흔히 **차등 발현 분석(differential expression)** 기법을 사용하여, **한 클러스터 vs. 나머지 모든 셀** 간에 유의하게 높게 발현되는 유전자를 선별합니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=using%20data%E2%80%90derived%20marker%20genes%20or,Clusters%20can%20be)). 예를 들어, **Wilcoxon rank-sum 검정**이나 t-test 등을 통해 각 클러스터에 대해 **상위 랭크된 유전자 목록**을 얻고, 이러한 유전자들을 해당 클러스터의 후보 마커로 간주합니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=using%20data%E2%80%90derived%20marker%20genes%20or,Clusters%20can%20be)). 상위 마커 유전자들은 그 클러스터를 특징짓는 분자 지표이며, 보통 여러 마커들의 조합으로 클러스터의 정체성을 추론합니다. (여러 조건의 샘플이 통합된 경우, **Conserved marker** 분석으로 조건 간 공통 마커를 찾기도 합니다.)
    
- **Cluster Annotation**: 도출된 마커 유전자들을 바탕으로 클러스터의 **세포 유형**을 지정합니다. 대표 마커들이 알려진 어떤 세포의 마커 세트와 부합한다면 해당 클러스터를 그 세포 타입으로 **주석(annotation)**합니다. 예를 들어 면역세포 데이터에서 CD3D, CD3E 등의 마커가 높은 클러스터는 T 세포로, CD19, MS4A1 마커가 높은 군집은 B 세포로 명명하는 식입니다. 이 과정에서는 **문헌 또는 데이터베이스의 기존 마커** 정보를 활용할 수 있습니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=respective%20test%20statistic%20are%20regarded,dataset%20to%20facilitate%20cell%E2%80%90identity%20annotation)). 최근에는 대규모 reference atlas를 활용한 **자동 주석 도구**도 발전하고 있어서, SingleR, CellTypist, Azimuth 등 알고리즘이 **참조 데이터세트의 표현 공간**에 신규 데이터 클러스터를 매핑하여 **자동으로 세포 유형을 예측**해주기도 합니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=%2A%20Automated%20Annotation%3A%20AI,supporting%20developmental%20and%20disease%20research)). 이러한 방법들은 수작업에 의존했던 세포 주석 단계를 표준화하고 고속화하는 최근의 추세입니다.
    

아래는 Scanpy에서 **마커 유전자 식별** 및 **클러스터 주석**을 수행하는 간단한 코드 예시입니다:

```python
# 클러스터별 마커 유전자 발현 비교 (Wilcoxon rank-sum 테스트)
sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon')

# 클러스터 '0'의 상위 5개 마커 유전자 조회
markers_cluster0 = adata.uns['rank_genes_groups']['names']['0'][:5]
print("Cluster0 top markers:", markers_cluster0)

# 예시: 미리 알고 있는 셀 타입 마커 기반으로 클러스터를 수동 주석
# (여기서는 가상의 예로 클러스터 0/1/2를 T, B, Monocyte로 라벨링)
cluster_to_celltype = {'0': 'T cell', '1': 'B cell', '2': 'Monocyte'}
adata.obs['cell_type'] = adata.obs['leiden'].map(cluster_to_celltype)
adata.obs['cell_type'].cat.add_categories('Unknown', inplace=True)  # 미리 정의되지 않은 클러스터는 Unknown
adata.obs['cell_type'].fillna('Unknown', inplace=True)
print(adata.obs[['leiden','cell_type']].head(10))
```

이처럼 각 클러스터에 대해 특징적인 유전자들을 찾아보고, 이를 토대로 세포 타입명을 부여하게 됩니다. 최종적으로 클러스터 ID 대신 세포 타입 이름(예: T cell, B cell 등)이 할당되면 해석이 용이해집니다. 또한 최근에는 **대용량 참조 데이터베이스**와의 비교를 자동화하는 방법들이 활발히 연구되어, 사람 뇌 세포 아틀라스나 면역세포 아틀라스 등과 대조하여 **클러스터->세포타입 매핑**을 정량적으로 수행하기도 합니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=respective%20test%20statistic%20are%20regarded,dataset%20to%20facilitate%20cell%E2%80%90identity%20annotation)).

## 4. 시각화 (Visualization)

군집화 결과와 데이터의 구조는 **시각화**를 통해 직관적으로 파악할 수 있습니다. 고차원 유전자 발현 데이터를 2차원으로 투영하여 **세포 간 관계를 시각적으로 표현**하는 것이 일반적이며, 주요 방법으로 **PCA**, **t-SNE**, **UMAP** 등이 사용됩니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=covering%20essential%20steps%20like%20quality,ensuring%20reliable%20results%20across%20experiments)). 최신 경향으로는 **UMAP**이 뛰어난 속도와 구조 보존 특성으로 인해 가장 널리 활용되고 있습니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Common%20alternatives%20to%20t%E2%80%90SNE%20are,are%20not%20aware%20of%20any)).

- **PCA 시각화**: PCA의 **주요 두 개 PC (PC1 vs PC2)**를 좌표로 산점도를 그리면 데이터의 **거시적인 분포**를 볼 수 있습니다. PCA는 선형 변환이므로 크게 **분산이 높은 방향**을 강조하며, 일부 주요 세포군을 구분하는 데 유용할 수 있습니다. 다만, PC1/PC2만으로 모든 세포 유형을 분리하기는 한계가 있어 주로 보조적인 시각화로 쓰입니다.
    
- **t-SNE**: **t-Distributed Stochastic Neighbor Embedding** 알고리즘은 국소적으로 유사한 데이터 포인트들을 2차원에서 모이게 하는 비선형 투영 기법입니다. scRNA-seq 분야에서 한때 표준으로 많이 사용되었지만, **perplexity 등의 파라미터에 민감**하고 배치(batch)에 따라 결과가 달라질 수 있다는 점이 한계로 지적됩니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=overlook%20potential%20connections%20between%20these,Becht)). 소규모 데이터셋의 세부 구조를 살피는 데는 여전히 유용하나, 대규모 데이터나 배치 통합된 데이터에서는 결과 해석에 주의가 필요합니다.
    
- **UMAP**: **Uniform Manifold Approximation and Projection**은 현재 single-cell 데이터 시각화에 가장 인기있는 방법으로, **고차원 공간의 구조적인 인접관계**를 비교적 충실히 2D에 보존하면서도 t-SNE보다 **계산이 빠르고 대규모 데이터에 잘 스케일링**됩니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=%28Weinreb%20et%C2%A0al%2C%202018%29,are%20not%20aware%20of%20any)). 그 결과 UMAP은 scRNA-seq 탐색적 데이터 분석에 **사실상 표준(best practice)**으로 권장되고 있습니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=,are%20not%20aware%20of%20any)). UMAP plot에서 인접한 점들은 발현 패턴이 유사한 세포들로, 앞서 구한 클러스터들이 공간적으로 모여 나타나므로 군집 형성 여부를 시각적으로 확인할 수 있습니다. (필요시 3D UMAP도 가능하며, 매우 복잡한 데이터의 경우 **PAGA(graph abstraction)**와 같은 기법과 결합해 보는 사례도 있습니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=An%20alternative%20to%20classical%20visualization,with%20large%20numbers%20of%20cells)) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=We%20recommend%20UMAP%20for%20exploratory,PCA%20for%20trajectory%20inference%20summarization)).)
    

아래는 **UMAP** 좌표를 계산하고 시각화하는 예시입니다:

```python
# UMAP 차원축소 (neighbors 그래프 기반으로 수행됨)
sc.tl.umap(adata)
# UMAP 결과 좌표는 adata.obsm['X_umap']에 저장됨
print(adata.obsm['X_umap'][:5, :])  # 첫 5개 셀의 UMAP 좌표 출력

# 클러스터 또는 셀 타입을 색상으로 하는 UMAP plot (주피터 노트북 등에서 사용 가능)
# sc.pl.umap(adata, color=['leiden'])           # 클러스터 레이블로 색상 표시
# sc.pl.umap(adata, color=['cell_type'])        # 셀 타입 레이블로 색상 표시
```

> **참고:** 상기 코드의 `sc.pl.umap` 부분은 그래프를 그리는 함수로, 본 환경에서는 실행하지 않았습니다. UMAP 시각화 결과는 보통 여러 군집이 2차원 공간에 점 구름 형태로 나타나며, **클러스터 간의 거리**와 **상대적 위치**를 통해 세포군들의 관계를 해석합니다. UMAP은 특히 대규모 데이터에서 t-SNE 대비 효율적이고 안정적인 결과를 주기 때문에 현재 대부분의 scRNA-seq 논문에서 UMAP plot이 사용되고 있습니다 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=%28Weinreb%20et%C2%A0al%2C%202018%29,a%20suitable%20alternative%20to%20PCA)).

## 5. 통합 분석 (Integration)

마지막으로, 서로 다른 샘플이나 다양한 데이터 유형을 **통합 분석**하는 단계입니다. 통합 분석은 크게 **멀티 샘플 통합**(여러 실험 배치의 scRNA-seq 데이터 통합)과 **멀티 모달 통합**(다른 종류의 single-cell 데이터 간 통합)으로 구분할 수 있습니다.

- **Multi-sample Integration (배치 통합 분석)**: 서로 다른 실험에서 얻은 scRNA-seq 데이터나 기술적으로 다른 플랫폼으로 생성된 데이터는 **배치 효과(batch effect)**로 인해 직접 비교가 어려울 수 있습니다. 이를 해결하기 위해 **배치 교정(batch correction)** 기법을 적용하여, **동일한 세포 타입들이 배치에 상관없이 가까이** 모이도록 데이터를 조정합니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=t,ensuring%20reliable%20results%20across%20experiments)). 예를 들어, Seurat v3의 **CCA(Canonical Correlation Analysis)** 기반 통합, MNN(Mutual Nearest Neighbors) 교정법 ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=2021%20%29,omics%20data%20and%20their%20applications) ), Harmony 알고리즘 등이 널리 사용됩니다. 이러한 도구들은 서로 다른 데이터셋을 **공통 표현 공간**으로 정렬하여, downstream 분석 (예: 클러스터링, marker 검정)을 **통합된 데이터**에 대해 수행할 수 있게 합니다. 통합 결과, 같은 세포 유형은 배치에 관계없이 그룹화되고, **잘못된 군집 분리나 섞임 현상**을 줄여 신뢰도 높은 생물학적 결론을 도출할 수 있습니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=t,ensuring%20reliable%20results%20across%20experiments)).
    
- **Multi-modal Integration (다중 모달 통합)**: 최근 single-cell 기술의 발전으로 하나의 세포에 대해 **여러 종류의 분자 데이터** (예: 전사체+크로마틴 접근성, 전사체+단백질 등)를 동시 획득하는 **멀티-오믹스** 실험이 증가하고 있습니다 ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=single,comprehensively%20understand%20cell%20state%20and) ). 이런 **다중 모달 데이터**를 통합 분석하면, 한 세포의 다양한 분자층 정보를 결합하여 **더 깊은 생물학적 통찰**을 얻을 수 있습니다. 예를 들어, scRNA-seq + scATAC-seq 통합을 위해 Seurat v4에서 제안된 **WNN(Weighted Nearest Neighbors)** 알고리즘이나, **MOFA+, LIGER** 같은 행렬 분해 기반 방법, **TotalVI**와 같은 딥러닝 기반 통합모델 등이 개발되어 있습니다 ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=results%20of%20the%20integration,Tangram%20and%20Cell2location%20are%20based) ). Multi-modal integration에서는 각 modality의 데이터를 적절히 정규화 및 표현하여 **공통의 저차원 공간**으로 결합하거나, 하나의 modality를 기반으로 다른 modality의 특징을 예측(mapping)하는 방식 등이 활용됩니다. 이러한 접근을 통해, 예를 들어 **유전자 발현과 크로마틴 상태를 연계**하여 유전자 조절 기작을 밝히거나, **전사체와 단백질** 발현을 함께 고려하여 세포 상태를 정밀하게 정의할 수 있습니다 ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=multimodal%20omics%20methods%20have%20been,cell%20data%20integration%20tools) ) ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=Single,and%20proteome%20provides%20more%20comprehensive) ). 멀티 모달 통합은 현재 활발한 연구 분야로, 향후 대규모 공개 DB의 multi-omics 데이터를 통합하여 **멀티모달 세포 아틀라스**를 구축하려는 시도가 진행 중입니다 ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=single,comprehensively%20understand%20cell%20state%20and) ).
    

아래는 **여러 샘플의 scRNA-seq 데이터**를 **통합**하는 간단한 예시 코드입니다 (Python Scanpy 기준):

```python
# 예시로 두 개 샘플의 anndata 객체를 읽어옴
adata1 = sc.read_h5ad("sample1.h5ad")
adata2 = sc.read_h5ad("sample2.h5ad")

# 배치 통합을 위해 두 데이터를 하나로 합치고 'batch' 컬럼 추가
adata_combined = adata1.concatenate(adata2, batch_key="batch")

# 배치 효과 교정: BBKNN (Batch Balanced KNN)을 이용한 통합
import scanpy.external as sce
sce.pp.bbknn(adata_combined, batch_key='batch')  # 배치 정보 고려하여 이웃 그래프 구성

# 통합된 데이터에 대해 UMAP과 클러스터링 수행
sc.tl.umap(adata_combined)
sc.tl.leiden(adata_combined, resolution=0.5)

# UMAP 시각화 (배치 별 색과 클러스터 색 등으로 확인 가능)
# sc.pl.umap(adata_combined, color=['batch', 'leiden'])
```

위 코드에서는 단순히 두 batch를 `concatenate`한 뒤 **BBKNN** 방법을 적용하여 배치 간 균형 잡힌 이웃 그래프를 생성하였습니다 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=t,ensuring%20reliable%20results%20across%20experiments)). 이처럼 통합된 데이터에서는 `batch`에 따른 군집 분리가 최소화되고 **진정한 생물학적 군집**만 드러나게 됩니다. 멀티모달 통합의 경우 Python에서는 **scVI-tools**, **scanpy**의 `muon` 패키지 등 특화된 툴을 사용하며, 분석 절차는 각 모달리티 데이터를 안맞추어 joint embedding을 학습하는 형태로 진행됩니다.

---

요약하면, **scRNA-seq 분석 워크플로우**는 (1) 데이터를 정제하는 **전처리** 단계 ([Powerful scRNA-seq Data Analysis Tools in 2025](https://www.nygen.io/resources/blog/single-cell-scrna-seq-multi-omics-data-analysis-tools#:~:text=covering%20essential%20steps%20like%20quality,ensuring%20reliable%20results%20across%20experiments)), (2) 셀들을 그룹화하는 **클러스터링** 단계 ([scanpy.tl.leiden — scanpy](https://scanpy.readthedocs.io/en/stable/generated/scanpy.tl.leiden.html#:~:text=Cluster%20cells%20into%20subgroups%20,%2C%202019)), (3) 군집에 의미를 부여하는 **Annotation** 단계 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=using%20data%E2%80%90derived%20marker%20genes%20or,Clusters%20can%20be)) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=respective%20test%20statistic%20are%20regarded,dataset%20to%20facilitate%20cell%E2%80%90identity%20annotation)), (4) 결과를 이해하기 쉽게 **시각화**하는 단계 ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=%28Weinreb%20et%C2%A0al%2C%202018%29,a%20suitable%20alternative%20to%20PCA)), (5) 여러 데이터셋이나 모달리티를 **통합**하여 분석하는 단계로 구성됩니다. 이러한 단계별 모범 사례들은 커뮤니티의 **최신est practice**에 따라 계속 발전 중이며 (예: Leiden 클러스터링 채택, UMAP 활용 증가, batch 통합 알고리즘 발전, 참조 기반 자동 셀 타입 주석 등), 대규모 단일세포 데이터 통합을 통해 **포괄적인 세포 아틀라스**를 구축하려는 방향으로 나아가고 있습니다 ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=single,comprehensively%20understand%20cell%20state%20and) ). 이번 워크플로우 정리는 Python을 활용한 구현 예시와 함께, single-cell 분석의 전 과정을 개괄적으로 보여줌으로써 최신 분석 동향을 파악하는 데 도움을 주고자 합니다.

**Sources:** 주요 개념 및 방법들은 Luecken _et al_. (2019) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Before%20analysing%20the%20single%E2%80%90cell%20gene,fraction%20of%20mitochondrial%20counts%20are)) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=count%20depth%2C%20few%20detected%20genes%2C,Doublet%20Finder%3A%20McGinnis%20et%C2%A0al%2C%202018)) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=these%20steps,gene%20expression%20abundances%20between%20cells)) ([Current best practices in single‐cell RNA‐seq analysis: a tutorial | Molecular Systems Biology](https://www.embopress.org/doi/10.15252/msb.20188746#:~:text=Common%20alternatives%20to%20t%E2%80%90SNE%20are,are%20not%20aware%20of%20any))의 싱글셀 RNA-seq 분석 모범 사례 튜토리얼과, 최근 single-cell 통합 분석 리뷰(Jin _et al_., 2023) ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=2021%20%29,omics%20data%20and%20their%20applications) ) ( [Progress in single-cell multimodal sequencing and multi-omics data integration - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10937857/#:~:text=results%20of%20the%20integration,Tangram%20and%20Cell2location%20are%20based) ) 등을 참고하였습니다.