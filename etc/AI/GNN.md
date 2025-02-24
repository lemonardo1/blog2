**그래프 신경망 (Graph Neural Networks, GNNs)**

그래프 신경망(GNN)은 그래프 데이터에서 직접 학습할 수 있도록 설계된 신경망 아키텍처의 한 종류입니다. 그래프에서는 **노드(Node, 정점)**가 개체(Entity)를 나타내고, **엣지(Edge, 간선)**가 개체 간의 관계를 나타냅니다. GNN은 이러한 네트워크 구조를 그대로 반영하여 학습하는 데 강점을 가지며, 대표적인 응용 분야로는 **소셜 네트워크, 분자 구조, 지식 그래프(Knowledge Graph), 교통 네트워크** 등이 있습니다.

---

## **핵심 개념**

### 1. **그래프 표현 (Graph Representation)**

- 그래프 GG는 보통 **노드 집합** VV와 **엣지 집합** EE로 정의됩니다.
- 각 노드 $v∈Vv \in V$에는 **특징 벡터** $xv\mathbf{x}_v$가 할당될 수 있습니다.
- 각 엣지 $(u,v)∈E(u, v) \in E$ 역시 **특징 벡터** $euv\mathbf{e}_{uv}$를 가질 수 있으며, 이는 노드 $uu$와 $vv$ 사이의 관계를 설명하는 정보입니다.

### 2. **메시지 패싱 (Message Passing)**

- GNN에서는 **메시지 패싱(Message Passing)** 또는 **이웃 정보 집계(Neighborhood Aggregation)** 과정을 통해 노드 간 정보를 교환합니다.
- 각 레이어에서 노드는 다음 단계를 거칩니다:
    1. **이웃 노드로부터 정보를 집계** (예: 평균, 합산, 가중합 등)
    2. **자신의 기존 정보와 결합하여 업데이트**
- 여러 레이어를 거치면서 한 노드는 점점 더 많은 이웃의 정보를 포함한 **임베딩(Embedding)**을 형성하게 됩니다.

### 3. **그래프 컨볼루션 레이어 (Graph Convolutional Layers)**

- 대표적인 GNN 모델 중 하나인 **GCN(Graph Convolutional Network)**의 업데이트 규칙은 다음과 같습니다:

$$hv(k+1)=σ(∑u∈N(v)∪{v}1∣N(v)∣∣N(u)∣W(k) hu(k))\mathbf{h}_v^{(k+1)} = \sigma\Bigg(\sum_{u \in \mathcal{N}(v) \cup \{v\}} \frac{1}{\sqrt{|\mathcal{N}(v)|}\sqrt{|\mathcal{N}(u)|}} \mathbf{W}^{(k)}\, \mathbf{h}_u^{(k)}\Bigg)$$

- hv(k)\mathbf{h}_v^{(k)}는 kk번째 레이어에서 노드 vv의 임베딩입니다.
    
- N(v)\mathcal{N}(v)는 노드 vv의 이웃 노드 집합입니다.
    
- W(k)\mathbf{W}^{(k)}는 학습 가능한 가중치 행렬입니다.
    
- σ\sigma는 활성화 함수(예: ReLU)입니다.
    
- 다른 GNN 모델(예: GraphSAGE, GAT, GIN)은 이웃 정보를 집계하는 방식에서 차이가 있습니다.
    

### 4. **풀링 및 리드아웃 (Pooling / Readout)**

- 그래프 전체를 하나의 벡터로 표현해야 하는 경우, **리드아웃(Readout) 연산** 또는 **풀링(Pooling) 연산**이 사용됩니다.
    - 노드 임베딩들의 **합(Sum), 평균(Mean), 최댓값(Max)**을 취하는 방식
    - **계층적 풀링(Hierarchical Pooling)** 기법을 활용해 점진적으로 그래프를 축소하는 방식

### 5. **작업 유형 (Types of Tasks)**

- **노드 분류 (Node-Level Tasks)**: 개별 노드의 속성을 예측 (예: 소셜 네트워크에서 봇 계정 탐지)
- **엣지 예측 (Edge-Level Tasks)**: 엣지 존재 여부 또는 엣지 속성을 예측 (예: 추천 시스템에서 사용자-아이템 연결 예측)
- **그래프 분류 (Graph-Level Tasks)**: 그래프 전체의 속성을 예측 (예: 분자의 독성 여부 판단)

---

## **대표적인 GNN 아키텍처**

1. **GCN (Graph Convolutional Network)**
    
    - 가장 널리 사용되는 GNN 모델 중 하나
    - **스펙트럼 기반 컨볼루션**을 적용하여 노드 간 관계를 학습
    - 반지도 학습(Semi-Supervised Learning)에서 주로 사용
2. **GAT (Graph Attention Network)**
    
    - **어텐션 메커니즘(Attention Mechanism)**을 적용하여 이웃 노드의 중요도를 학습
    - 단순 평균이 아니라 학습 가능한 가중치를 통해 정보 집계
3. **GraphSAGE**
    
    - **샘플링(Sampling) 기법**을 활용하여 대규모 그래프도 처리 가능
    - 평균, LSTM, 가중합 등 다양한 집계 방식 지원
4. **GIN (Graph Isomorphism Network)**
    
    - 그래프 구조를 보다 강력하게 구별할 수 있도록 설계됨
    - 단순한 구조이지만 표현력이 뛰어남
5. **MPNN (Message Passing Neural Network)**
    
    - GNN을 일반화한 프레임워크로, 다양한 메시지 패싱 기법을 포괄
    - 분자 구조 분석 등에서 활용

---

## **GNN의 주요 응용 분야**

1. **소셜 네트워크 분석**
    
    - 친구 추천, 커뮤니티 탐색, 악성 계정 탐지
2. **의약/화학**
    
    - 분자 특성 예측, 신약 개발, 단백질-약물 상호작용 분석
3. **추천 시스템**
    
    - 사용자-아이템 관계를 그래프로 모델링하여 추천 정확도 향상
4. **지식 그래프 (Knowledge Graph)**
    
    - 엔터티(개체) 분류, 관계 추론, 질의 응답 시스템
5. **컴퓨터 비전**
    
    - 이미지 내 객체 간 관계 분석, 장면 그래프(Scene Graph) 생성
6. **교통 및 네트워크 분석**
    
    - 교통 흐름 예측, 최적 경로 탐색

---

## **장점과 과제**

### ✅ **장점**

- **관계 정보 학습 가능**: 그래프 구조 자체를 활용하여 데이터 간의 연결을 효과적으로 학습
- **가변 크기의 입력 처리 가능**: CNN이나 RNN과 달리 노드 수가 변하는 데이터를 다룰 수 있음
- **유연성**: 다양한 그래프 기반 태스크에 적용 가능

### ⚠ **과제**

- **확장성(Scalability)**: 대규모 그래프에서는 계산 비용이 높음 → 샘플링 기법 필요
- **과도한 스무딩(Over-Smoothing)**: 너무 많은 메시지 패싱은 노드 간 표현이 동일해지는 문제 발생
- **이질적 그래프(Heterogeneous Graphs)**: 노드/엣지 타입이 다양한 경우 모델링이 복잡해짐
- **동적 그래프(Dynamic Graphs)**: 시간에 따라 변화하는 그래프를 처리하는 방법이 필요

---

## **시작하기**

1. **라이브러리 및 프레임워크**
    
    - [PyTorch Geometric (PyG)](https://pytorch-geometric.readthedocs.io/)
    - [DGL (Deep Graph Library)](https://www.dgl.ai/)
    - [Graph Nets (DeepMind)](https://github.com/deepmind/graph_nets)
2. **기본 코드 (PyTorch Geometric)**
    
    ```python
    import torch
    import torch.nn.functional as F
    from torch_geometric.nn import GCNConv
    
    class SimpleGCN(torch.nn.Module):
        def __init__(self, in_channels, hidden_channels, out_channels):
            super().__init__()
            self.conv1 = GCNConv(in_channels, hidden_channels)
            self.conv2 = GCNConv(hidden_channels, out_channels)
    
        def forward(self, x, edge_index):
            x = self.conv1(x, edge_index).relu()
            x = self.conv2(x, edge_index)
            return F.log_softmax(x, dim=1)
    ```
    

---

## **요약**

GNN은 그래프 데이터에서 관계와 패턴을 학습하는 강력한 도구입니다. 다양한 분야에서 활용되며, 실용적인 과제(확장성, 과적합 등)를 해결하는 연구가 활발히 진행되고 있습니다.