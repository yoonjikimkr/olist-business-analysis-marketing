# 🇧🇷 Olist Business Analysis & Marketing Strategy
> **AARRR Framework 기반 셀러 생애주기 분석 및 마케팅 최적화 프로젝트**

이 프로젝트는 브라질 최대 이커머스 플랫폼 **Olist**의 데이터를 활용하여, 잠재 셀러의 유입부터 입점, 전환, 매출 기여, 그리고 플랫폼 평판 형성까지의 전 과정을 분석하고 데이터 기반의 비즈니스 전략(Action Items)을 제안합니다.

---

## 💎 핵심 분석 요약 (AARRR Insights & Reports)
각 단계별 상세 분석 내용과 리포트 링크입니다. (상세 내용은 각 링크를 클릭하여 확인할 수 있습니다.)

### 1. Acquisition (유입)
- **핵심 발견**: `Organic Search`와 `Paid Search`가 전체 리드의 50%를 차지하며 매출 기여도가 가장 높음.
- **주요 리포트**: 
  - [Acquisition 심층 분석](md/Acquisition_Deep_Analysis.md) : 채널별 유입 패턴 분석
  - [리드 전환 성과 분석](md/Acquisition.md) : 채널별 최종 전환 수정치
  - [마케팅 채널 성과 (Web)](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/Acquisition.html)
- **인사이트**: `unknown` 채널은 UTM 유실된 검색 트래픽임을 입증.

### 2. Activation (활성화)
- **핵심 발견**: 리드 접촉 후 **14일 이내**에 계약을 완료한 셀러의 활성화율이 54.7%로 가장 높음.
- **주요 리포트**: 
  - [Part 2: 리드 전환 정밀 분석](md/Part2_리드전환분석.md) : 영업 단계별 병목 구간 탐지
  - [셀러 AARRR 프레임워크 (Web)](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/seller_aarrr_analysis_framework.html)

### 3. Retention (유지)
- **핵심 발견**: `Social` 채널 유입 셀러는 매출은 낮으나 고객 만족도가 높아 플랫폼 평판 형성에 기여함.
- **주요 리포트**: 
  - [Retention 심층 분석](md/Retention.md) : 셀러 이탈 패턴 및 재구매 분석

### 4. Revenue (매출)
- **핵심 발견**: '가전(Small Appliances)', '시계(Watches)' 카테고리의 대형 온라인 벤더가 플랫폼의 핵심 수익원.
- **주요 리포트**: 
  - [스타 셀러 군집 분석](md/Olist_deep_eda_report.md#분석-c-매출-셀러-세그먼테이션-k-means) : K-Means 클러스터링을 통한 4개 우량 그룹 식별
  - [Revenue 분석 리포트](md/Revenue_analysis_report.md)

### 5. Referral (추처)
- **핵심 발견**: 배송 속도가 리뷰 점수(NPS)에 직결됨. 15일 초과 시 평점 급격히 하락.
- **주요 리포트**: 
  - [Referral 분석 리포트](md/Referral_Analysis_Report.md) : NLP 워드클라우드 기반 감성 분석
  - [Business Insight Report](md/Referral_Business_Insight_Report_haeun.md)

---

## 🎯 최종 전략 제언 (Action Items)
1. **예산 재배분**: Paid Search 비중을 70%까지 확대하여 고품질 MQL 확보에 집중.
2. **영업 프로세스 혁신**: 최초 컨택 후 14일 이내 온보딩을 완료하는 'VIP 패스트 트랙' 운영.
3. **물류 기반 관리**: 빠른 배송을 유지하는 스타 셀러에게 수수료 감면 및 노출 상단 보장 혜택 제공.

---

## 📊 시각화 및 설계도
- **통합 대시보드 설계**: [Tableau 대시보드 Mockup](Dashboard_Mokup.md)
- **데이터 관계도 (ERD)**: `mermaid` 다이어그램 기반 [통합 ERD 설계](md/unified_erd.md)
- **분석 흐름 시각화**: [Connectivity Map (Web)](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/connectivity_map.html)

---

## 📂 프로젝트 아카이브 (Archive)

### 📅 진행 현황 및 타임라인
| 날짜 | 주요 마일스톤 |
| :--- | :--- |
| **04-28** | ✅ AARRR 통합 리포트 발행 및 비즈니스 전략 수립 |
| **04-21** | ✅ K-Means 군집 분석 및 LTV 예측 모델링 |
| **04-14** | ✅ Activation 병목 구간 탐지 및 Retention 모델링 |
| **04-07** | ✅ 마케팅 채널 성과 분석 및 데이터 마스터셋 구축 |

### 🤝 팀 협업 워크플로우
1. **데이터 준비**: `python3 scripts/setup_data.py`
2. **마스터셋 생성**: `python3 scripts/generate_master_table.py`
3. **폴더 구조**: 
   - `data/`: Raw/Processed 데이터
   - `images/`: 분석 차트 60여 종 ([output_charts/](output_charts/))
   - `scripts/`: 자동화 유틸리티
