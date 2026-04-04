# 🎯 분석 전략: 셀러 모집 채널별 ROI 극대화 전략
**Olist B2B 마케팅 퍼널 × E-commerce 통합 분석**

## 1. 분석 배경 및 목표
> "Paid Search, Organic, Social 등 각 채널로 모집한 셀러 중, 누가 플랫폼에 가장 높은 장기 매출을 만들었는가? 그 채널에 예산을 집중하면 ROI가 극대화되는가?"

마케팅 채널로 모집된 셀러(B2B)가 실제 플랫폼 매출(B2C)로 이어지는 전 과정을 데이터로 추적해, **채널별 ROI를 산정하고 예산 배분 전략**을 제안하는 것이 본 프로젝트의 핵심 목표입니다.

---

## 2. 데이터 연결 경로 (Data Path)
분석은 아래와 같은 경로로 데이터를 조인하여 수행됩니다.
`MQL.origin(채널)` → `CLOSED_DEALS.seller_id` → `ORDER_ITEMS` → `ORDERS(매출)`
(상세 데이터 연결 구조는 **[통합 ERD 설계](unified_erd.md)** 참조)

---

## 3. 5단계 분석 흐름 (Analysis Pipeline)

| 순서 | 분석 주제 | 핵심 질문 |
|:---:|:---|:---|
| **1** | **채널별 전환율** | MQL 중 실제 계약(입점)까지 간 비율이 채널별로 다른가? |
| **2** | **채널별 RFM** | 계약한 셀러가 채널별로 얼마나 자주, 많이 팔았는가? |
| **3** | **Attribution** | 어느 유입 채널이 실제 플랫폼 매출에 가장 많이 기여했는가? |
| **4** | **LTV + Time-lag** | 어느 채널 셀러가 장기적으로 돈이 됐고, 매출 발생까지 얼마나 걸렸는가? |
| **5** | **Forecast** | 채널 예산을 최적화하여 재배분하면 전체 매출이 어떻게 달라지는가? |

---

## 4. 최종 결론 및 기대 효과
"어떤 채널에 셀러 모집 예산을 집중해야 하고, 어떤 셀러 프로필(업종·지역·규모)을 타겟해야 플랫폼 ROI가 극대화되는가?"

본 분석을 통해 BM(Business Manager) 분들의 **셀러 페르소나 수립 및 세그먼트 전략**에 직접적인 데이터 근거를 제공합니다.

---

## 🔗 관련 문서
- [Seller AARRR 분석 프레임워크 웹에서 보기](https://raw.githack.com/yoonjikimkr/olist-business-analysis-marketing/main/html/seller_aarrr_analysis_framework.html) / [소스 코드](../html/seller_aarrr_analysis_framework.html)
- [기초 탐색적 데이터 분석(EDA) 리포트](eda_report.md)
