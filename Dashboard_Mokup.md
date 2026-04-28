# 📊 Business Intelligence System: Olist Seller Strategy
> **Comprehensive Multi-Page Dashboard Design based on AARRR Analysis**

---

## 🎨 Dashboard Design Overview
이 대시보드 설계 프로젝트의 목표는 20개 이상의 개별 리포트에 흩어져 있는 인사이트(K-Means, NLP, ROI 시뮬레이션 등)를 하나의 의사결정 시스템으로 통합하는 것입니다.

---

## 🖥️ Screen 1: Marketing Funnel Deep-Dive (Acquisition & Activation)
*Goal: 유입 채널의 효율성을 진단하고 입점 병목 구간(15일 골든타임)을 추적합니다.*

```text
====================================================================================================
 [ 🛰️ MONITOR 1: MARKETING TUNNEL EFFICIENCY ]                     | FILTERS: ORIGIN, LP, PERIOD |
====================================================================================================

 [📊] LEAD QUALITY MATRIX (CVR vs SALES CYCLE)        | [📉] ACTIVATION GOLDEN TIME (15d)
------------------------------------------------------|---------------------------------------------
  CVR (%)                                             |  Active (%)
   ^                                                  |   ^   [#######] 54.7% (Fast: <14d)
   | (Paid Search)                                    |   |
   |         (Organic)                                |   |         [###] 21.2% (Late: >30d)
   |                                                  |   |
   |              (Direct)                            |   |                 [#] 8.4% (No-Contact)
   |                         (Social)                 |   +------------------------------------->
   +--------------------------------------> CYCLE (d) |    
                                                      |  *Insight: 14일 초과 시 전환율 60% 급감
----------------------------------------------------------------------------------------------------
 [🏷️] LANDING PAGE PERFORMANCE (TOP 5)                | [🕵️] THE 'UNKNOWN' TRACE (UTM LOSS)
------------------------------------------------------|---------------------------------------------
 # | PAGE ID       | TRAFFIC | CONV.  | BOUNCE       |   - Trace Link: search_traffic_leakage.csv
 --|---------------|---------|--------|-------       |   - Findings: 56.7% of Unknown is 'SEO'
 1 | /sellers-lp1  | 2,450   | 15.2%  | 12%          |   - Impact: Organic ROI is undervalued
 2 | /join-olist   | 1,200   | 10.1%  | 25%          |   
 3 | /partner-v2   |   850   |  5.4%  | 40%          |           [########] 56.7% Search
 ...                                                  |           [###] 20.1% Direct
----------------------------------------------------------------------------------------------------
 [👥] SALES TEAM FUNNEL (SDR -> SR)
----------------------------------------------------------------------------------------------------
 MQL (8k) =======[ SDR Filter ]======> PQL (2.1k) =======[ SR Closing ]======> WON (842)
   Lead Loss: 74% (Quality Issue)       Closing Rate: 40.1% (High Priority Segments)
====================================================================================================
```

---

## 🖥️ Screen 2: Seller DNA & Segmentation (Revenue & Retention)
*Goal: K-Means 클러스터링 결과를 바탕으로 고가치 셀러를 식별하고 성장 전략을 수립합니다.*

```text
====================================================================================================
 [ 💎 MONITOR 2: SELLER VALUE SEGMENATION ]                        | FILTERS: SEGMENT, CATEGORY |
====================================================================================================

 [🎯] K-MEANS 4-CLUSTER PROFILES (STAR vs SMALL)      | [🏷️] CATEGORY LTV HEATMAP (TOP 10)
------------------------------------------------------|---------------------------------------------
 (Order Freq)                                         |  Cat: Watches          [########] R$ 8.2k
  ^                                                   |  Cat: Small Appl       [#######] R$ 7.9k
  |      [Growth]       [Star Sellers]                |  Cat: Electronics      [#####] R$ 5.1k
  |                                                   |  Cat: Baby             [####] R$ 4.2k
  |       [Small]      [Initial]                      |  Cat: Beauty           [###] R$ 3.8k
  |                                                   |
  +--------------------------------------> (GMV)      |  *Category Focus: Watches/Small Appl
                                                      |
----------------------------------------------------------------------------------------------------
 [📈] SELLER RETENTION OVER TIME (COHORT)             | [🚀] UPSell PIPELINE: GROWTH TO STAR
------------------------------------------------------|---------------------------------------------
 Month | M1     | M2     | M3     | Mn                |  - Segments: 'online_big', 'shark'
 ------|--------|--------|--------|-------            |  - Trigger: Listing < 10 products
 26.01 | 100%   | 45%    | 32%    | 22%               |  - Action: Automated Account Manager Assign
 26.02 | 100%   | 48%    | 35%    | -                 |  
 26.03 | 100%   | 52%    | -      | -                 |           [##################] 74% Potential
----------------------------------------------------------------------------------------------------
 [💰] TOP 10 GMV DRIVERS (STAR LIST)
----------------------------------------------------------------------------------------------------
 SELLER ID | LEAD TYPE    | CUM. GMV   | CLUSTER     | RETENTION SCORE
 ----------|--------------|------------|-------------|----------------------------------------------
 f42a...   | online_big   | R$ 12,402  | Star        | 98 (Very High)
 a18d...   | offline_resel| R$  9,850  | Growth      | 85 (High)
====================================================================================================
```

---

## 🖥️ Screen 3: Service Quality & Reputation (Referral)
*Goal: NLP 감성 분석과 물류 성과를 결합하여 고객 만족도의 근본 원인을 분석합니다.*

```text
====================================================================================================
 [ 🛡️ MONITOR 3: QUALITY & REPUTATION (NPS) ]                      | FILTERS: STATE, FREIGHT |
====================================================================================================

 [📅] DELIVERY SPEED vs REVIEW SCORE (CORRELATION)    | [☁️] SENTIMENT WORD CLOUD (NLP)
------------------------------------------------------|---------------------------------------------
  Score (1-5)                                         |  [POSITIVE]
   ^                                                  |   ** QUALIDADE ** | ** RÁPIDO ** | PERFEITO
   | [#####] 4.8 (Fast: <10d)                         |
   | [####] 3.2 (Mid: 15d)                            |  [NEGATIVE]
   | [#] 1.5 (Delayed: >20d)                          |   ** ATRASO ** | REEMBOLSO | DEFEITO
   |                                                  |
   +--------------------------------------> DAYS      |  *Alert: Delay > 15d triggers 1-star reviews
                                                      |
----------------------------------------------------------------------------------------------------
 [🗺️] GEOGRAPHIC FREIGHT COST MAP                     | [⭐️] STAR SELLER QUALITY PERFORMANCE
------------------------------------------------------|---------------------------------------------
 Region | Avg Freight | Delivery Time  | NPS          |   Star Sellers vs General Sellers
 -------|-------------|----------------|-------       |
 SP     | R$ 12.1     | 8 days         | 4.6          |   Star Group: [##################] 4.7 NPS
 RJ     | R$ 24.5     | 12 days        | 4.2          |   General:    [###########] 3.8 NPS
 BA     | R$ 45.0     | 18 days        | 3.1          |
====================================================================================================
```

---

## 🖥️ Screen 4: Strategy Simulation & ROI (The Decision Board)
*Goal: 분석 결과를 적용했을 때의 비즈니스 임팩트를 시뮬레이션합니다.*

```text
====================================================================================================
 [ 🎯 MONITOR 4: STRATEGIC ROI SIMULATOR ]                         | FILTERS: BUDGET, SCENARIO |
====================================================================================================

 [📊] BUDGET REALLOCATION (AS-IS vs TO-BE)            | [💰] EXPECTED REVENUE LIFT
------------------------------------------------------|---------------------------------------------
 AS-IS (SOCIAL 40%, SEARCH 30%)                       |  Current GMV: R$ 1,200,000
 | [####] Social (High Spend, Low ROI)                |
 | [###] Search (Low Spend, High ROI)                 |  Predicted GMV (To-Be): R$ 1,338,000
                                                      |
 TO-BE (SEARCH 70%, SOCIAL 10%)                       |  PERCENT LIFT: [ +11.5% ]
 | [#######] Search (Scale High-Value MQL)            |
 | [#] Social (Brand Only)                            |  CAC REDUCTION: [ -12.4% ]
                                                      |
----------------------------------------------------------------------------------------------------
 [📝] KEY ACTION ITEMS (BA CHECKLIST)
----------------------------------------------------------------------------------------------------
 1. PAID SEARCH 70% 집중 배정 (Acquisition)
 2. WATCHES/SMALL APPL 타겟팅 강화 (Revenue)
 3. 15일 이내 계약 패스트트랙 운영 (Activation)
 4. 배송 지연 셀러 실시간 노출 페널티 (Referral)
====================================================================================================
```

---

## 🔗 Technical Implementation (Tableau Specs)
- **Primary Join**: `mql_id` + `seller_id` (Marketing Funnel x Ecommerce Data)
- **Calculated Fields**:
  - `Activation_Speed_Group`: `DATEDIFF('day', [first_contact], [won_date])`
  - `High_Value_Cat`: `[Category] IN ('watches', 'small_appliances', 'electronics')`
  - `NPS_Volatility`: `STDEV([Review Score])`
- **Data Source**: `looker_studio_master.csv`
