# Burrows-Wheeler Aligner (BWA)

## 소개

BWA는 **참조 유전체(reference genome)**에 가까운 **sequence read**를 **mapping**하기 위한 소프트웨어로, Burrows-Wheeler Transform(BWT)를 기반으로 Heng Li에 의해 개발되었습니다. BWA는 대규모 참조 유전체, 예를 들어 인간 유전체와 같은 데이터를 처리하기 위해 설계되었습니다.

## BWA의 3가지 알고리즘

BWA는 3가지 주요 알고리즘으로 구성됩니다:

1. **BWA-backtrack**
    - Illumina short reads (100bp 이하)와 같은 짧은 reads를 처리하기 위해 설계되었습니다.
2. **BWA-SW**
    - 길이가 긴 reads(70bp~1Mbp)를 처리하며, **split alignment**와 **gap alignment**에 강점을 보입니다.
3. **BWA-MEM**
    - 최신 알고리즘으로, 빠르고 정확하며 다양한 길이의 reads를 처리할 수 있습니다.
    - BWA-backtrack과 BWA-SW를 대체할 수 있는 기능을 제공하며, 특히 70-100bp Illumina reads에서도 더 나은 성능을 보입니다.

## 각 알고리즘의 특징

### **BWA-backtrack**

- 짧은 reads(특히 Illumina short reads)에 적합합니다.
- 낮은 sequencing error rate(<2%)를 가정하며, **3'-end**에서 품질이 낮은 base를 잘라내어 더 많은 reads를 align할 수 있습니다.

### **BWA-SW**

- gap이 빈번한 alignment에서 더 민감한 결과를 제공합니다.
- **gene fusion** 또는 **reference misassembly**로 인해 발생하는 multi-hit reads를 처리할 수 있습니다.

### **BWA-MEM**

- split alignment를 지원하며, gene fusion과 같은 구조적 변이를 탐지할 수 있습니다.
- 속도와 정확도 면에서 우수하며, 긴 reads와 짧은 reads 모두에 적합합니다.
- **SAM format**에 대응하며, 추가적으로 Picard와 같은 툴과의 호환성을 위해 `-M` 옵션을 지원합니다.

## Multi-hit reads 처리

Multi-hit reads는 여러 개의 alignment를 가질 수 있는 경우를 말하며, **gene fusion**, **reference misassembly** 또는 **chimeric reads**와 같은 이유로 발생할 수 있습니다.

- BWA는 기본적으로 각 read에 대해 하나의 alignment를 보고합니다.
- `-M` 옵션을 사용하면 **shorter split hits**를 secondary alignment로 마킹하여 문제를 해결할 수 있습니다.

## Chimeric reads 탐지

**Chimeric reads**는 두 개 이상의 alignment를 가질 수 있는 reads입니다.

- BWA-SW와 BWA-MEM은 chimeric reads를 탐지할 수 있으며, 이를 통해 유전체 구조적 변이를 분석할 수 있습니다.

## BWA의 진화

2013년에 출시된 BWA-MEM은 이전 BWA-backtrack과 BWA-SW의 한계를 극복했습니다.

- **참조 유전체의 총 길이**가 4GB 이상이더라도 동작 가능하며, 개별 염색체의 길이가 2GB를 초과하지 않아야 했던 제한이 해결되었습니다.
- 0.6.x 버전부터 모든 BWA 알고리즘에서 이러한 제한이 제거되었습니다.

## FAQ

1. **BWA를 인용하려면?**
    
    - BWA-short:
        
        > Li H. and Durbin R. (2009) Fast and accurate short read alignment with Burrows-Wheeler Transform. Bioinformatics, 25:1754-60.
        
    - BWA-SW:
        
        > Li H. and Durbin R. (2010) Fast and accurate long-read alignment with Burrows-Wheeler Transform. Bioinformatics.
        
2. **최적의 알고리즘 선택 방법?**
    
    - **70bp 이상의 reads**: BWA-MEM 권장.
    - **짧은 sequences**: BWA-backtrack.
    - **gap이 빈번한 alignment**: BWA-SW.
3. **Sequencing error 허용 범위?**
    
    - BWA-backtrack: 2% 이하 권장.
    - BWA-SW/BWA-MEM: Alignment 길이에 따라 2%(100bp), 3%(200bp), 5%(500bp), 10%(1000bp 이상)까지 허용.
4. **BWA가 SNP을 호출하는가?**
    
    - 아니오, BWA는 alignment만 수행합니다.
    - SNP 호출을 위해서는 **SAMtools**, **GATK**와 같은 도구를 사용할 수 있습니다.
5. **참조 시퀀스의 길이 제한은?**
    
    - 0.6.x 이후 버전에서 참조 유전체 총 길이가 4GB를 초과해도 문제없이 동작합니다.

