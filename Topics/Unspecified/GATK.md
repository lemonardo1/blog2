#bioinformatics
# Genome Analysis ToolKit (GATK)

## 소개

**Genome Analysis Toolkit (GATK)**는 Broad Institute에서 개발한 **유전체 변이 분석 툴킷**으로, **NGS(Next-Generation Sequencing) 데이터**를 기반으로 변이(SNP, Indel 등)를 분석할 수 있도록 설계된 소프트웨어입니다. 이 툴킷은 다양한 서브 프로그램을 포함하며, **exomeSeq**, **whole genome sequencing (WGS)**, **RNA-seq** 등의 데이터를 처리할 수 있습니다.

GATK는 **인간 유전체(human genome)**뿐만 아니라 모든 생물 종의 유전체 분석에도 사용할 수 있으며, 다양한 **시퀀싱 기술**에서 생성된 데이터를 지원합니다.

---

## 주요 특징

### 1. **변이 분석의 산업 표준**

GATK는 **SNP**와 **Indel**과 같은 변이를 분석하는 데 표준으로 자리 잡았습니다. 최근에는 **체세포 단일 변이(somatic short variant)**, **복제 수 변이(copy number variant, CNV)** 및 **구조적 변이(structural variation, SV)** 분석 기능도 추가되었습니다.

### 2. **Best Practices 워크플로우**

- GATK는 데이터를 **reads-to-results**로 처리하는 **Best Practices** 워크플로우를 제공합니다.
- 이 워크플로우는 Broad Institute의 대규모 데이터 분석 환경에서 검증된 프로세스로, 정확성과 계산 효율성을 극대화하도록 설계되었습니다.
- GATK4는 다양한 변이 유형(germline 및 somatic variants, CNV, SV)에 대해 최적화된 Best Practices 워크플로우를 제공합니다.

### 3. **다양한 플랫폼 지원**

- GATK는 **Linux** 및 **MacOS X**에서 작동하며, **POSIX 호환 플랫폼**을 지원합니다.
- 주요 요구 사항은 **Java 1.8**이며, 일부 도구는 추가적으로 **R** 또는 **Python** 종속성을 요구합니다.
- GATK4는 **Docker 컨테이너**를 통해 쉽게 배포할 수 있으며, 클라우드 환경 및 Apache Spark 아키텍처를 활용하여 병렬 처리를 지원합니다.

---

## 데이터 입력 및 출력

### **입력**

- GATK는 **BAM 파일**을 기본 입력으로 사용합니다.
- BAM 파일은 위치별로 정렬된 데이터여야 하며, 이를 위해 **SAMtools sort** 명령을 사용하여 정렬할 수 있습니다.

### **출력**

- 결과는 **VCF (Variant Call Format)** 파일로 제공됩니다.
- VCF 파일은 변이에 대한 상세 정보를 포함하며, 후속 분석(GWAS, Genotyping 등)에 활용됩니다.

---

## GATK의 주요 분석 과정

### 1. **참조 서열 매핑**

GATK를 사용하기 전에 **Bowtie2**, **BWA**와 같은 aligner를 사용해 reads를 참조 서열(reference genome)에 매핑해야 합니다.

- Genome(WGS, GBS): Bowtie2, BWA
- Transcriptome(RNA-seq): STAR

### 2. **중복 제거**

- GATK를 실행하기 전, **Picard MarkDuplicates**를 사용해 **중복 reads**를 제거합니다.
- 단, **GBS**와 같은 데이터의 경우 제한효소로 인해 생성된 reads는 중복으로 간주하지 않는 경우도 있습니다.

### 3. **RNA-seq 데이터 처리**

RNA-seq 데이터를 사용할 경우, GATK의 **SplitNCigarReads**를 사용해 전처리를 진행한 후 변이 분석을 수행해야 합니다.

### 4. **변이 분석 단계**

#### **Germline Variant Calling Pipeline**

- **HaplotypeCaller**를 사용해 개체별로 SNP 및 Indel 변이를 탐지합니다.
- 주요 변이 유형:
    - **SNP (Single Nucleotide Polymorphism)**: 단일 염기 차이에 의해 발생.
    - **Indel (Insertion & Deletion)**: 염기의 삽입/삭제로 인한 변이.
    - **Structural Variation**: 유전체 구조의 차이로 인한 변이.

#### **Variant Discovery**

- **CombineGVCF**, **GenotypeGVCF**, **SelectVariants**를 통해 변이를 통합 및 필터링합니다.
- 결과 데이터는 **vcftools**, **PLINK** 등을 사용해 GWAS(Gene-Wide Association Study)와 같은 추가 분석에 활용할 수 있습니다.

---

## GenomicsDBImport

- 샘플 수가 1,000개를 초과할 경우, **CombineGVCF** 대신 **GenomicsDBImport**를 사용하는 것이 권장됩니다.
- GenomicsDBImport는 DB 형태로 데이터를 관리하며, 효율적으로 변이 통합 작업을 수행할 수 있습니다.

---

## 기술적인 요구 사항

- **운영체제**: Linux, MacOS X (Windows 미지원).
- **필수 소프트웨어**: Java 1.8, 일부 도구는 R 또는 Python 필요.
- **배포 방식**: Docker 이미지 지원, 클라우드 및 병렬 처리 환경 최적화.

---

GATK는 NGS 데이터를 효율적으로 처리하고 유전체 변이를 분석할 수 있는 강력한 도구입니다. Best Practices 워크플로우와 다양한 서브 프로그램을 통해 정밀하고 신뢰할 수 있는 결과를 얻을 수 있습니다.