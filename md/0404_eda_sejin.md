# Olist Seller Channel Analysis — AARRR 기반 EDA 분석 보고서

---

## 1. 개요 및 목표

본 보고서는 Olist 플랫폼의 셀러 마케팅 채널 효율을 **AARRR (Acquisition, Activation, Retention, Referral, Revenue)** 프레임워크를 기반으로 분석한 결과입니다.

**최종 목적:**
*   셀러 모집 예산 집중 채널 선정
*   플랫폼 ROI 극대화를 위한 타겟 셀러 프로필(업종·지역·규모) 도출

---

## 2. 데이터셋 구조와 설명

분석에 사용된 데이터셋은 브라질 이커머스 기업 Olist의 마케팅 펀널 데이터와 일반 이커머스 거래 데이터를 기반으로 합니다.

### [핵심 데이터셋 구성]
*   **`mql_leads`**: 마케팅 채널을 통해 플랫폼에 관심을 보인 잠재 셀러 리드 정보 (8,000건)
*   **`closed_deals`**: MQL 중 실제로 Olist와 입점 계약을 체결한 셀러 정보 (842건)
*   **`sellers`**: 입점 셀러의 위치(주, 도시) 등 기본 정보
*   **`orders` & `order_items`**: 셀러가 판매한 주문 내역 및 개별 상품 상세 정보 (가격, 운송비, 상태 등)
*   **`order_reviews`**: 구매자가 셀러의 서비스에 대해 남긴 리뷰 점수 (1~5점)
*   **`products` & `category_translation`**: 판매 상품의 카테고리 정보 및 영문 번역 정보

---

## 3. 전처리 (Preprocessing)

데이터의 일관성을 확보하고 정확한 분석 지표를 산출하기 위해 다음과 같은 전처리 과정을 수행했습니다.

### [주요 전처리 단계]
1.  **날짜 형식 변환**: 문자열로 되어 있는 모든 날짜 데이터를 `datetime` 형식으로 변환하여 시간 흐름에 따른 분석이 가능하도록 했습니다.
2.  **테이블 결합 (Merging)**:
    *   `mql_leads`를 기준으로 `closed_deals`를 **LEFT JOIN** 하여 전환 여부를 판단했습니다.
    *   계약된 셀러(`seller_id`)를 기준으로 상품(`order_items`), 주문(`orders`), 리뷰(`order_reviews`) 정보를 순차적으로 결합했습니다.
3.  **핵심 파생 변수 생성**:
    *   **전환 여부 (`is_converted`)**: MQL 중 `closed_deals`에 기록이 있는 경우 `True`로 설정했습니다.
    *   **거래 발생 여부 (`is_active_seller`)**: 계약 후 실제 판매 활동(1건 이상 주문 발생)을 한 셀러를 구분했습니다.
    *   **GMV 산출**: 상품 가격(`price`)과 운송료(`freight_value`)를 합산하여 총 거래액을 정의했습니다.
4.  **최종 마스터 테이블 (`seller_master`) 생성**: 리드 유입부터 실제 매출 및 리뷰까지 한 셀러의 전 여정을 추적할 수 있는 펀널 통합 테이블을 구축했습니다.

---

## 4. AARRR 단계별 분석

본격적인 세부 분석에 앞서, Olist 셀러 데이터에 최적화된 **AARRR (Acquisition, Activation, Retention, Referral, Revenue)** 프레임워크의 구조를 요약합니다.

### [Olist Seller AARRR 프레임워크 요약]

![Olist Seller AARRR 프레임워크](images/olist_seller_aarrr_summary.png)

| 단계 | 정의 (Seller 관점) | 핵심 지표 (Core Metrics) | 분석 포인트 |
| :--- | :--- | :--- | :--- |
| **Acquisition** | 신규 셀러 리드 유입 | MQL (Marketing Qualified Leads) | 어떤 채널에서 고효율 리드가 유입되는가? |
| **Activation** | 리드의 실제 입점 및 첫 거래 | CVR (전환율), Sales Cycle (계약 기간) | 계약 성사가 빠르고 입점 후 즉시 판매하는가? |
| **Retention** | 셀러의 플랫폼 활동 지속 | Churn Rate (이탈률), Active Months | 매월 꾸준히 주문을 발생시키는 셀러인가? |
| **Referral** | 셀러가 플랫폼 평판에 기여 | Review Score (리뷰), On-time Delivery | 고객 서비스가 우수하여 선행 지표를 높이는가? |
| **Revenue** | 셀러의 매출 창출 및 장기 가치 | Seller LTV, GMV per MQL (ROI) | 플랫폼 매출에 실질적으로 얼마나 기여하는가? |

---

### [ACQUISITION] 채널별 MQL 유입 분석

**주요 지표 설명:**
*   **MQL (Marketing Qualified Lead)**: 마케팅 채널을 통해 유입된 잠재 셀러 리드입니다. `mql_leads` 테이블의 고유 ID(`mql_id`) 개수를 카운트하여 산출합니다.

**분석 결과:**
*   가장 많은 리드(MQL)를 유입시키는 채널은 **Organic Search** (2,296건, 약 28.7%)이며, **Paid Search** (1,586건, 약 19.8%)와 **Social** (1,350건, 약 16.9%)이 그 뒤를 잇습니다.
*   월별 추이를 보면 2018년 초부터 MQL 유입이 급격히 증가하는 추세를 보입니다.

![채널별 MQL 분포](images/acq_channel_dist.png)
![월별 MQL 유입 추이](images/acq_mql_trend.png)

> [!TIP]
> **핵심 인사이트 (Acquisition)**
> Organic 및 Paid Search가 전체 리드의 약 50%를 차지하며 검색 엔진 최적화 및 광고의 중요성이 매우 높음.

---

### [ACTIVATION] 채널별 전환율 및 딜 성사 분석

**주요 지표 설명:**
*   **CVR (Conversion Rate, 전환율)**: 유입된 MQL 중 실제로 Olist 입점 계약(`closed_deals`)까지 이어진 비율입니다. (계약 건수 / MQL 건수)
*   **Sales Cycle (영업 주기)**: 첫 접촉(`first_contact_date`)부터 계약 완료(`won_date`)까지 걸리는 평균 일수입니다.

**분석 결과:**
*   **전환율(CVR):** 평균 CVR은 약 10.5% 수준입니다. **Paid Search** (12.3%)와 **Organic Search** (11.8%)가 평균 이상의 높은 전환율을 보입니다.
*   **Sales Cycle:** MQL 유입 후 계약 체결까지의 기간(Sales Cycle)은 대부분의 채널에서 중앙값 기준 10~30일 내외로 나타납니다.
*   **CVR vs Lead Time:** Paid Search는 전환율이 높으면서도 계약 기간이 상대적으로 짧아 매우 효율적인 채널로 분류됩니다.

![채널별 전환율(CVR)](images/act_cvr.png)
![채널별 Sales Cycle 분포](images/act_sales_cycle.png)
![CVR vs Sales Cycle](images/act_cvr_vs_leadtime.png)

> [!TIP]
> **핵심 인사이트 (Activation)**
> Paid Search는 높은 전환율과 빠른 계약 성사라는 두 마리 토끼를 잡고 있는 핵심 동력원임.

---

### [RETENTION] 채널별 RFM 및 셀러 활성 지속 분석

**주요 지표 설명:**
*   **Churn Rate (이탈률)**: 플랫폼에서 판매 활동이 중단된 셀러의 비율입니다. 여기서는 전월 판매 이력이 있으나 당월 판매가 0건인 셀러의 비율로 계산했습니다.
*   **Recency (최근성)**: 마지막 판매일로부터 현재(데이터 마감일)까지 경과한 일수입니다.

**분석 결과:**
*   **이탈률(Churn Rate):** 시간이 지남에 따라 셀러들의 월간 이탈률이 변동성을 보이며, 일부 유료 채널 유입 셀러들의 유지력이 상대적으로 낮은 경향이 관찰됩니다.
*   위 시각화 자료를 통해 특정 기간에 모든 채널의 이탈률이 급증하는 구간이 확인되며, 이는 플랫폼 서비스 이슈나 계절성 요인일 가능성이 큽니다.

![채널별 월간 셀러 이탈률](images/ret_churn_rate.png)

> [!TIP]
> **핵심 인사이트 (Retention)**
> 입점 초기(1-2개월)에 이탈하는 셀러 비중이 높으므로 초기 안착을 돕는 온보딩 프로그램 강화가 필요함.

---

### [REFERRAL] 채널별 셀러 품질 — 리뷰·배송 분석

**주요 지표 설명:**
*   **NPS Proxy (순 추천 지수 대용)**: 구매자의 리뷰 점수를 바탕으로 산출한 셀러 평판 지표입니다. (리뷰 4, 5점 비율 - 1, 2점 이하 비율)로 정의하여, 해당 채널 유입 셀러가 플랫폼 신뢰도에 기입하는 정도를 측정합니다.

**분석 결과:**
*   **NPS Proxy:** 고객 만족도는 **Unknown** 및 **Social** 유입 셀러들이 상대적으로 높게 나타납니다.
*   배송 준수율 및 리뷰 점수는 플랫폼의 지속 가능성을 결정짓는 핵심 지표로, 채널 간 품질 차이가 존재함을 확인했습니다.

![채널별 NPS Proxy](images/ref_nps.png)

> [!TIP]
> **핵심 인사이트 (Referral)**
> Social 채널 유입 셀러들은 매출 규모는 작을 수 있으나 고객 만족도 면에서 긍정적인 기여를 하고 있음.

---

### [REVENUE] 채널별 매출 기여 및 LTV 분석

**주요 지표 설명:**
*   **GMV (Gross Merchandise Volume)**: 셀러가 판매한 총 거래액(상품가 + 운송비)입니다.
*   **LTV (Lifetime Value)**: 분석 기간 내 셀러 1인당 누적 총 거래액입니다. 해당 채널을 통해 입점한 셀러가 장기적으로 창출하는 매출 가치를 의미합니다.
*   **ROI Proxy (GMV per MQL)**: 채널 효율 지표입니다. (채널별 총 GMV / 채널별 MQL 수)로 계산하며, 마케팅 비용 투입 대비 산출되는 매출 성과를 가늠합니다.

**분석 결과:**
*   **총 GMV 기여도:** **Unknown** (기업 협약 등 추정) 채널과 **Organic Search**가 총 매출의 가장 큰 부분을 차지합니다.
*   **ROI Proxy (GMV per MQL):** 리드당 매출 기여도는 **Paid Search**가 약 114.7 BRL로 소셜(38.0 BRL) 대비 매우 높습니다.
*   **업종별 매출 히트맵:** 특정 업종(예: Health & Beauty, Watches)이 특정 채널에서 유입되었을 때 매출 성과가 극대화되는 경향이 있습니다.

![채널별 ROI Proxy](images/rev_roi.png)
![업종 x 채널 평균 GMV 히트맵](images/rev_heatmap.png)

---

## 3. 통합 분석 및 결론

### 채널 전략 2x2 매트릭스

**분석 방법:** 전환율(CVR)과 셀러당 평균 매출(LTV)을 두 축으로 하여 채널을 분류하였습니다.

![채널 전략 2x2 매트릭스](images/final_strategy_matrix.png)

*   **최우선 투자 (우상단):** **Paid Search**, **Organic Search**
    *   높은 전환 효율과 준수한 LTV를 보유. 예산 증액 시 즉각적인 매출 증대 기대.
*   **소수 정예 (좌상단):** **Email**, **Referral**
    *   전환율은 낮으나 유입된 셀러의 질(LTV)이 높음. 타겟팅 정교화 필요.
*   **볼륨 채널 (우하단):** **Direct Traffic**
    *   전환은 쉬우나 매출 기여도가 낮음. 셀러 교육 및 고단가 상품 취급 유도 필요.

---

### 최종 인사이트 요약

#### [채널 예산 전략]
1.  **최우선 투자: Paid Search**
    *   이유: CVR 12.3% (전체 상위), 리드당 ROI가 약 115 BRL로 매우 효율적임.
2.  **유지/최적화: Organic Search**
    *   이유: 가장 많은 리드를 저비용으로 유입시키며 안정적인 매출 기여도를 보임.
3.  **축소/제거: Social**
    *   이유: 유입량은 많으나 전환율(5.6%) 및 리드당 ROI(38 BRL)가 현저히 낮아 광고비 효율이 떨어짐.

#### [타겟 셀러 프로필]
*   **최적 업종:** Health & Beauty, Watches & Accessories, Housewares (LTV 상위 기여 업종)
*   **최적 행동 프로파일:** 리드 유입 후 10일 이내에 계약을 완료하는 'Fast-Mover' 프로토타입.
*   **특이점:** 소규모 셀러(declared_revenue가 낮은 경우)라 할지라도 Paid Search 유입 시 초기 안착 속도가 빠름.

#### [핵심 데이터 한계]
*   분석 기간: 2017-06 ~ 2018-06 (Funnel 데이터 기준)
*   실제 채널별 마케팅 집행 비용(CPC/CPL) 정보 부재로 MQL 수 기반의 Proxy 지표 사용.
*   구매자 유입 경로와 셀러 유입 경로 간의 상관관계는 본 데이터셋으로 확인 불가.
