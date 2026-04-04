# 🛒 Olist Business Analysis & Marketing Strategy

## 🎯 분석 주제 및 목표
**「셀러 모집 채널별 ROI 극대화 전략」 — Olist B2B 마케팅 퍼널 × E-commerce 통합 분석**
> "Paid Search, Organic, Social 등 각 채널로 모집한 셀러 중, 누가 플랫폼에 가장 높은 장기 매출을 만들었는가? 그 채널에 예산을 집중하면 ROI가 극대화되는가?"

- **핵심 로직**: `MQL.origin(채널)` → `CLOSED_DEALS.seller_id` → `ORDER_ITEMS` → `ORDERS(매출)`
- **상세 전략 및 분석 파이프라인**: [분석 전략 문서 보기](md/analysis_strategy.md)

---

## 👥 팀원 및 협업 안내
- **총 인원**: 6명
- **주요 목표**: MQL(Marketing Qualified Leads) 데이터와 실제 주문 데이터를 결합하여 **데이터 기반의 마케팅 의사결정 시나리오** 도출

---

## 📅 프로젝트 진행 현황 (Timeline)

### ✅ 완료된 작업
- **2026-04-04**
  - [x] **탐색적 데이터 분석(EDA) 완료**: 9개 데이터셋을 통합하여 결제, 주문 추이, 고객 분포, 리뷰 점수 등 기초 통계 분석 완료 ([리포트 보기](md/eda_report.md))
  - [x] **Seller AARRR 분석 프레임워크 설계**: 판매자 관점의 획득(Acquisition)부터 수익(Revenue)까지의 KPI 지표 정의 ([프레임워크 보기](html/seller_aarrr_analysis_framework.html))
  - [x] **프로젝트 구조 최적화**: 폴더 정리 및 문서 내 링크 정규화

---

## 🚀 프로젝트 로드맵 (예시)
보내주신 **5단계 분석 파이프라인**과 **AARRR 프레임워크**를 결합한 상세 실행 계획입니다.

### 📊 분석 흐름 시각화 (Connectivity Map)
> 💡 [통합 ERD(데이터 관계도) 상세 보기](md/unified_erd.md) | [프리미엄 HTML 맵 보기](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/connectivity_map.html)

```text
[ Step 1. 유입 채널 ]  ──(전환율 분석)──▶  [ Step 2. 입점 셀러 ]
       (Acquisition)                         (Activation)
                                                  │
                                            (RFM/활동성 체크)
                                                  │
                                                  ▼
[ Step 5. 전략/ROI ]   ◀──(LTV/예측)───  [ Step 3 & 4. 매출 기여 ]
        (Strategy)                           (Revenue)
```

🔗 **상세 인터랙티브 맵**: [웹에서 보기(추천)](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/connectivity_map.html) / [소스 코드](html/connectivity_map.html)

### 💡 단계별 연결 고리 (Why & How)
팀원 6명이 각 단계를 수행할 때, 우리 작업이 어떻게 연결되는지 정의합니다.

*   **Phase 1 (기초)**: "어떤 채널에서 온 셀러가 진짜 우리 파트너가 되는가?"를 정의합니다. (수량 중심)
*   **Phase 2 (심층)**: "입점한 셀러가 실제로 돈을 벌어다 주는가?"를 검증합니다. (질적 평가)
*   **Phase 3 (전략)**: "앞으로 어디에 돈을 써야 가장 효율적인가?"를 시뮬레이션합니다. (의사결정)

---

### [Phase 1] 데이터 연결 및 마케팅 퍼널 기초 분석
- [ ] **Step 1. 채널별 전환율 (Conversion)**: `MQL.origin` → `Contract` 전환율 분석 (Acquisition/Activation)
  - 채널별 MQL 수 및 계약 성공(won) 비율 산출
  - 유입 경로별 Sales Cycle(리드 생성~계약) 소요 시간 분석
  - **결과물(Output)**: 채널별 입점 전환율 리포트 & 계약 셀러 리스트
- [ ] **Step 2. 채널별 RFM 분석 (Retention)**: 입점 셀러의 활동성 평가
  - 채널별 셀러의 평균 주문 빈도(Frequency) 및 최근 판매일(Recency) 비교
  - Churn Seller(이탈 셀러) 비중이 높은 채널 식별
  - **결과물(Output)**: 채널별 활성/이탈 셀러 세그먼트 데이터

### [Phase 2] 수익성(ROI) 심층 분석 및 기여도 평가
- [ ] **Step 3. 매출 기여도(Attribution) 분석 (Revenue)**: 플랫폼 실매출 연결
  - 어느 채널(Origin) 셀러가 가장 높은 총 GMV를 기록했는가?
  - 매출 기반 상위 10% 판매자의 유입 경로 추적
  - **결과물(Output)**: 채널별 총 매출(GMV) 기여도 매핑
- [ ] **Step 4. LTV + Time-lag 분석**: 장기적 가치 및 매출 발생 지연 시간
  - 입점 후 12개월 이상 활동 셀러의 누적 수익(LTV) 산출
  - 첫 주문 수령까지의 Time-lag가 LTV에 미치는 영향 분석
  - **결과물(Output)**: 채널별 예상 LTV(고객 평생 가치) 지표

### [Phase 3] 전략 제언 및 시뮬레이션
- [ ] **Step 5. 예산 최적화 예측(Forecast)**: 마케팅 예산 재부분 시나리오
  - 채널별 ROI(LTV/CAC) 기반 차년도 예산 최적화안 도출 (BM 전략 연계)
  - 고가치 셀러 페르소나(업종·지역·규모) 정의 및 타겟팅 전략 수립
  - **결과물(Output)**: 채널별 마케팅 예산 재배분 권고안 및 타겟 페르소나 정의
- [ ] **최종 결과물 정리**: 
  - [ ] 종합 대시보드(BI) 구성 및 인사이트 도출
  - [ ] 비즈니스 제언 중심의 최종 발표 Deck 제작 (6인 공동 발표용)

---

## 📂 주요 폴더 구조
- `data/`: 데이터셋 보관
    - `raw/`: 원본 CSV ([데이터 수집 가이드](scripts/setup_data.py))
    - `processed/`: [마스터 테이블(ABT)](data/processed/marketing_sales_base.csv) ([생성 스크립트](scripts/generate_master_table.py))
- `scripts/`: 데이터 수집 및 가공 유틸리티
- `images/`: 분석 시각화 이미지 (PNG)
- `md/`: 분석 리포트 및 [통합 ERD 설계](md/unified_erd.md)
- `html/`: 인터랙티브 [AARRR 프레임워크 웹으로 보기](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/seller_aarrr_analysis_framework.html) / [소스 코드](html/seller_aarrr_analysis_framework.html)

---

## 🛠️ 분석 시작하기 (Getting Started)
팀원들은 아래 순서로 로컬 환경을 세팅해 주세요.

1. **데이터 수집**: `python3 scripts/setup_data.py` (Kaggle에서 데이터 자동 다운로드 및 배치)
2. **마스터 테이블 생성**: `python3 scripts/generate_master_table.py` (분석용 통합 CSV 생성)
3. **분석 착수**: `data/processed/marketing_sales_base.csv` 파일을 사용해 각 단계 분석 수행

### 🤝 팀 협업 데이터 워크플로우 (Data Workflow)
우리가 사용하는 마스터 테이블(`marketing_sales_base.csv`)은 아래 로직으로 생성됩니다.
- **Join Key**: `seller_id` (마케팅 계약 데이터와 실제 이커머스 판매 데이터의 유일한 연결 고리)
- **Left Join**: '계약은 했으나 매출이 없는' 리드까지 포함하여 **진정한 전환율(Conversion)**을 계산하기 위함
- **Data Granularity**: 1 Row = 1 MQL (각 리드별 마케팅 정보 + 해당 셀러의 성과 요약)