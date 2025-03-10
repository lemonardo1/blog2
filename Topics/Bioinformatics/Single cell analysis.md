[[single cell analysis pipeline]]
[[scanpy]]

# 싱글 셀 분석 (Single Cell Analysis)

## 개요
싱글 셀 분석(Single Cell Analysis)은 개별 세포 수준에서의 생물학적 데이터를 탐색하고 분석하는 방법을 의미한다. 이 기술은 세포 간의 이질성을 이해하고, 각각의 세포가 어떻게 기능하는지를 밝히는 데 중요한 역할을 한다. 특히, 종양학, 면역학, 발달생물학 등의 분야에서 혁신적인 발견을 가능하게 한다.

## 기술
### 샘플 준비
싱글 셀 분석을 위해서는 먼저 단일 세포를 분리하고 준비해야 한다. Fluorescence-activated cell sorting (FACS) 또는 microfluidics와 같은 기술이 자주 이용되며, 이를 통해 정확하게 단일 세포를 분리할 수 있다.

### 유전자 발현 분석
단일세포 RNA 시퀀싱(single-cell RNA sequencing, scRNA-seq)은 가장 일반적으로 사용되는 기법 중 하나로서, 각 세포의 유전자 발현 패턴을 탐색할 수 있게 해준다. 이를 통해 세포 유형 식별 및 기능적 상태를 평가할 수 있다.

### 프로테오믹스 및 메타볼로믹스
단백질과 대사산물 수준에서도 싱글 셀 분석이 가능하다. Mass spectrometry와 같은 첨단 기법을 활용하여 단일세포 프로테오믹스(single-cell proteomics)와 메타볼로믹스(single-cell metabolomics)를 수행함으로써 보다 심층적인 생물학적 통찰력을 제공한다.

## 생물학적 기전
싱글 셀 분석은 여러 생물학적 기전을 이해하는 데 필수적인 도구로 자리 잡고 있다.

1. **세포 이질성(Cellular Heterogeneity)**: 동일한 조직 내에서도 서로 다른 기능과 특성을 가진 다양한 유형의 세포들이 존재한다는 것을 밝혀낸다.
2. **발달 및 분화(Development and Differentiation)**: 줄기세포가 특정한 기능을 가진 성숙한 세포로 변형되는 과정을 추적하며 이해할 수 있게 한다.
3. **종양 미세환경(Tumor Microenvironment)**: 암 조직 내 다양한 세포 구성 요소와 그 상호작용을 규명하여 암 발생과 진행에 대한 새로운 시각을 제공한다.
4. **면역 반응(Immuno Response)**: 각각의 면역세포가 병원체에 반응하는 방식을 개별적으로 연구함으로써 백신 개발 및 면역 치료에 도움을 준다.

## 응용 분야
- **암 연구**: 종양 내 이질성을 파악하여 개인 맞춤형 치료법 개발에 기여한다.
- **신경과학**: 뇌의 복잡한 네트워크를 구성하는 다양한 뉴런들의 기능과 연결성을 이해하는 데 활용된다.
- **줄기세포 연구**: 줄기세포가 다양한 종류의 조직으로 분화되는 과정에서 각 단계별 특징을 규명한다.

## 결론
싱글 셀 분석은 현대 생명 과학 연구에서 필수불가결한 도구로 자리매김하고 있으며, 앞으로도 다양한 분야에서 혁신적인 연구 결과를 도출할 것으로 기대된다. 이를 통해 우리는 더욱 복잡한 생명 현상들을 명확하게 이해하고 해결책을 찾아낼 수 있을 것이다.


## 파이썬 Single cell analysis


## 파이썬을 활용한 싱글 셀 분석

파이썬은 싱글 셀 분석에서 강력한 도구로 사용되며, 다양한 라이브러리와 패키지를 통해 데이터를 처리하고 시각화할 수 있다. 이 섹션에서는 파이썬을 활용한 싱글 셀 분석의 기본적인 개념과 도구를 소개한다.

### 주요 라이브러리 및 툴

1. **Scanpy**
   - Scanpy는 대규모 싱글 셀 RNA 시퀀싱 데이터 세트를 처리하고 분석하기 위한 파이썬 기반의 오픈 소스 라이브러리이다.
   - 기본적인 데이터 전처리, 차원 축소, 클러스터링, 시각화 등 다양한 기능을 제공한다.

2. **Pandas**
   - Pandas는 데이터 조작과 분석을 위한 파이썬 패키지로서, 테이블 형식의 데이터를 쉽게 다룰 수 있는 DataFrame 객체를 제공한다.
   - 데이터를 정리하고 요약 통계를 계산하는 데 유용하다.

3. **NumPy**
   - NumPy는 대규모 다차원 배열과 행렬 연산을 지원하는 파이썬 라이브러리로, 수학적 계산에 주로 사용된다.
   - 빠른 배열 연산과 함께 과학 컴퓨팅에 필수적이다.

4. **Matplotlib & Seaborn**
   - Matplotlib는 데이터를 시각화하기 위한 기본적인 플롯팅 라이브러리이다.
   - Seaborn은 Matplotlib를 기반으로 하여 더욱 미려하고 복잡한 통계적 그래프를 쉽게 그릴 수 있도록 돕는다.

5. **Louvain & Leiden Algorithms**
   - 이 알고리즘들은 네트워크 커뮤니티 탐지를 위해 개발된 알고리즘으로, 싱글 셀 RNA-seq 데이터의 클러스터링에 자주 사용된다.
   
### 예제 워크플로우

다음은 Scanpy와 다른 라이브러리를 사용하여 간단히 싱글 셀 RNA-seq 데이터를 처리하고 분석하는 예제이다:

```python
import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
adata = sc.read_10x_mtx(
    'path_to_data/',  # 경로 수정 필요
    var_names='gene_symbols',
    cache=True)

# 전처리: 품질 제어 및 정규화
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# 고변이 유전자 식별
sc.pp.highly_variable_genes(adata)
adata = adata[:, adata.var['highly_variable']]

# PCA와 UMAP을 통한 차원 축소
sc.tl.pca(adata)
sc.pl.pca_variance_ratio(adata)  # 주성분의 설명력 시각화

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.umap(adata)

# 클러스터링 (Louvain 알고리즘)
sc.tl.louvain(adata)

# 시각화: UMAP 플롯 생성
sc.pl.umap(adata, color=['louvain'])

plt.show()
```

### 결론

파이썬은 다양한 오픈 소스 라이브러리를 통해 싱글 셀 분석을 용이하게 한다. 연구자는 이러한 도구들을 활용하여 대량의 생물학적 데이터를 효율적으로 처리하고 의미 있는 결과를 얻을 수 있다. 앞으로도 이러한 기술들은 생물학 연구에서 더 큰 역할을 할 것으로 기대된다.




---
### 대한민국 single cell 분석 연구실 목록

[주영석 교수님 KAIST](https://gsmse.kaist.ac.kr/boards/view/professor_01/21)
[박종은 교수님 KAIST](https://gsmse.kaist.ac.kr/boards/view/professor_01/12)
[최정균 교수님 KAIST](https://bioeng.kaist.ac.kr/index.php?mid=bio_03_01&document_srl=6860)