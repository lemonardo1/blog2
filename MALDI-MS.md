다음은 "Matrix-assisted laser desorption/ionization"에 대한 내용을 한국어로 번역한 문서입니다. 의학 및 과학 용어는 영어로 유지하였으며, 자연스럽고 정확한 한국어로 작성되었습니다.

---

# Matrix-assisted Laser Desorption/Ionization (MALDI)

## 개요

질량 분석법(mass spectrometry)에서 **Matrix-assisted laser desorption/ionization (MALDI)**은 레이저 에너지를 흡수하는 매트릭스를 사용하여 큰 분자들을 최소한의 단편화(fragmentation)로 이온화하는 기술입니다. 이 방법은 **DNA**, **proteins**, **peptides**, **carbohydrates**와 같은 생체 분자(biomolecules)와 다양한 유기 분자(예: **polymers**, **dendrimers**, 기타 거대 분자) 분석에 적용됩니다. 이러한 분자들은 기존의 이온화 방법으로 이온화될 때 쉽게 파괴되는 경향이 있습니다. **MALDI**는 **electrospray ionization (ESI)**와 성격이 유사하며, 둘 다 큰 분자를 기체 상태에서 낮은 단편화로 이온화하는 비교적 부드러운(soft) 기술입니다. 다만, **MALDI**는 일반적으로 다중 전하를 띤 이온(multi-charged ions)을 **ESI**보다 훨씬 적게 생성합니다.

**MALDI** 방법론은 세 단계로 이루어집니다.  
1. 샘플을 적절한 매트릭스 물질과 혼합하여 금속 플레이트에 도포합니다.  
2. 펄스 레이저(pulsed laser)가 샘플을 조사하여 샘플과 매트릭스 물질의 **ablation**과 **desorption**을 유도합니다.  
3. 분석 대상 분자(analyte molecules)가 뜨거운 기체 plume에서 양성자화(protonated) 또는 탈양성자화(deprotonated)되어 이온화되고, 이후 질량 분석기(mass spectrometer)로 가속되어 분석됩니다.

---

## 역사

**MALDI**라는 용어는 1985년 Franz Hillenkamp, Michael Karas 및 그들의 동료들에 의해 처음 만들어졌습니다. 이들은 아미노산 **alanine**을 **tryptophan**과 혼합하고 266 nm 파장의 펄스 레이저로 조사했을 때 더 쉽게 이온화된다는 것을 발견했습니다. **Tryptophan**이 레이저 에너지를 흡수하여 흡수하지 않는 **alanine**의 이온화를 도왔습니다. 이 "매트릭스"를 사용하면 2843 Da의 **peptide melittin**까지 이온화할 수 있었습니다.

큰 분자 레이저 탈착 이온화의 획기적인 발전은 1987년 Shimadzu Corporation의 Koichi Tanaka와 그의 동료들이 "초미세 금속과 액체 매트릭스 방법(ultra fine metal plus liquid matrix method)"을 개발하면서 이루어졌습니다. 이들은 30 nm 크기의 코발트 입자를 **glycerol**에 섞고 337 nm 질소 레이저를 사용하여 34,472 Da의 **protein carboxypeptidase-A**를 이온화했습니다. Tanaka는 적절한 레이저 파장과 매트릭스 조합으로 **protein**을 이온화할 수 있음을 입증하여 2002년 노벨 화학상을 공동 수상했습니다.

이후 Karas와 Hillenkamp는 **nicotinic acid** 매트릭스와 266 nm 레이저를 사용하여 67 kDa의 **protein albumin**을 이온화했습니다. 355 nm 레이저와 **cinnamic acid** 유도체(**ferulic acid**, **caffeic acid**, **sinapinic acid**)를 사용하면서 추가적인 개선이 이루어졌습니다. 1990년대 초반 저렴한 337 nm 질소 레이저와 상용 기기의 등장으로 **MALDI**는 점점 더 많은 연구자에게 보급되었습니다. 오늘날 **MALDI mass spectrometry**에는 주로 유기 매트릭스가 사용됩니다.

---

## 매트릭스(Matrix)

**MALDI**에서 매트릭스는 결정화된 분자들로 구성되며, 가장 흔히 사용되는 세 가지는 **sinapinic acid**, **α-cyano-4-hydroxycinnamic acid (α-CHCA)**, **2,5-dihydroxybenzoic acid (DHB)**입니다. 매트릭스 용액은 고순도 물과 유기 용매(예: **acetonitrile (ACN)** 또는 **ethanol**) 혼합물로 제조되며, 종종 **trifluoroacetic acid (TFA)**와 같은 카운터 이온(counter ion) 소스를 첨가하여 **[M+H]** 이온을 생성합니다. 예를 들어, 좋은 매트릭스 용액은 **sinapinic acid** 20 mg/mL를 **ACN:water:TFA (50:50:0.1)** 비율로 혼합한 것입니다.

### 주요 매트릭스 목록

| 화합물명                                      | 다른 이름              | 용매                          | 파장(nm)       | 응용 분야                          |
|---------------------------------------------|-----------------------|------------------------------|----------------|-----------------------------------|
| **2,5-dihydroxybenzoic acid (DHB)**         | Gentisic acid         | Acetonitrile, water, methanol, acetone, chloroform | 337, 355, 266 | **Peptides**, **nucleotides**, **oligonucleotides**, **oligosaccharides** |
| **3,5-dimethoxy-4-hydroxycinnamic acid**    | **Sinapinic acid (SA)** | Acetonitrile, water, acetone, chloroform | 337, 355, 266 | **Peptides**, **proteins**, **lipids** |
| **4-hydroxy-3-methoxycinnamic acid**        | **Ferulic acid**      | Acetonitrile, water, propanol | 337, 355, 266 | **Proteins**                     |
| **α-cyano-4-hydroxycinnamic acid (CHCA)**   | Alpha-cyano           | Acetonitrile, water, ethanol, acetone | 337, 355      | **Peptides**, **lipids**, **nucleotides** |
| **Picolinic acid (PA)**                     | -                     | Ethanol                      | 266            | **Oligonucleotides**             |
| **3-hydroxy picolinic acid (HPA)**          | -                     | Ethanol                      | 337, 355       | **Oligonucleotides**             |

---

## 매트릭스의 역할 및 특성

적합한 매트릭스 화합물은 시행착오를 통해 결정되지만, 몇 가지 분자 설계 요소를 기반으로 합니다.  
- 낮은 분자량(쉽게 기화되도록)  
- 낮은 증기압(샘플 준비 중 증발하지 않도록)  
- 산성(양성자 공급원 역할)  
- UV 또는 IR 범위에서 강한 광학 흡수(레이저 조사 흡수 효율)  
- 극성 그룹으로 기능화(수용액 사용 가능)  

매트릭스 용액은 분석 대상(예: **protein-sample**)과 혼합됩니다. 물과 유기 용매의 혼합은 소수성(hydrophobic) 및 수용성(hydrophilic) 분자를 용해시킵니다. 이 용액은 **MALDI plate**에 점적되고, 용매가 증발하면서 분석 대상 분자가 매트릭스 결정에 내포된 상태로 재결정화(co-crystallization)됩니다.

생물학적 시스템 분석에서는 **inorganic salts**가 이온화 과정을 방해할 수 있습니다. 이를 제거하기 위해 **solid phase extraction** 또는 냉수로 건조된 점적을 세척하는 방법이 사용됩니다.

---

## 기기(Instrumentation)

**MALDI** 기술은 다양한 변형이 있으며, 학술적 분석부터 고속 처리(high-throughput) 산업 용도까지 다양한 목적으로 사용됩니다. 가장 널리 사용되는 질량 분석기는 **time-of-flight mass spectrometer (TOF)**로, 큰 질량 범위를 다룰 수 있습니다. **MALDI-TOF** 기기는 종종 **reflectron**(이온 거울)을 장착하여 이온 비행 경로를 늘리고 해상도를 높입니다.

### 레이저(Laser)

**MALDI**는 주로 UV 레이저(예: 337 nm 질소 레이저, 355 nm 및 266 nm Nd:YAG 레이저)를 사용합니다. 적외선(IR) 레이저(예: 2.94 μm **Er:YAG laser**, 10.6 μm 이산화탄소 레이저)도 부드러운 이온화와 생물학적 샘플에 유용합니다.

### 대기압(Atmospheric Pressure)

**Atmospheric pressure (AP) MALDI**는 진공 대신 대기압 환경에서 작동하며, 감도 개선으로 **attomole** 수준의 검출이 가능합니다. 이는 **proteomics**, **drug discovery** 등 다양한 응용 분야에서 사용됩니다.

---

## 응용 분야(Applications)

### 생화학(Biochemistry)
- **Proteomics**: **MALDI-TOF**는 **gel electrophoresis**로 분리된 **proteins**를 빠르게 식별하며, **peptide mass fingerprinting**에 널리 사용됩니다.
- **Post-translational modifications**: **Protein methylation**, **demethylation** 등을 분석합니다.

### 유기 화학(Organic Chemistry)
- **Catenanes**, **rotaxanes**, **dendrimers**와 같은 합성 거대 분자를 분석합니다.

### 고분자 화학(Polymer Chemistry)
- **Molar mass distribution** 측정에 유용하며, **dithranol** 또는 **AgTFA**가 매트릭스로 사용됩니다.

### 미생물학(Microbiology)
- **MALDI-TOF**는 박테리아, 곰팡이 등 미생물 식별에 사용되며, **biotyping**을 통해 종을 결정합니다.

### 의학(Medicine)
- **Necrotizing enterocolitis (NEC)**, **pancreatic cancer** 진단에 활용되며, 항생제 내성 예측에도 사용됩니다.

---
