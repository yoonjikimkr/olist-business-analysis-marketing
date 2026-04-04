# Seller AARRR Analysis Framework

---

## 1. Acquisition
### 판매자 유입 — 어느 채널에서 리드가 오는가
> **분석 1 · 채널별 전환율**

| 주요 이벤트 | 사용 테이블 & Join | KPI |
| :--- | :--- | :--- |
| **랜딩페이지 최초 유입**<br>`mql_leads.first_contact_date`<br>`mql_leads.landing_page_id` | **기본 테이블**<br>`mql_leads`, `closed_deals` | **채널별 MQL 수 (월별)**<br>`COUNT(mql_id)`<br>`GROUP BY origin, month` |
| **MQL 생성 (리드 등록)**<br>`mql_leads.mql_id` 생성<br>`mql_leads.origin` 기록 | **Join 키**<br>`mql_leads.mql_id = closed_deals.mql_id` | **채널별 전환율 (CVR)**<br>`COUNT(won) / COUNT(mql_id)`<br>`GROUP BY origin` |
| **채널 분류**<br>organic_search / paid_search<br>social / email / other | **핵심 필드**<br>`origin`, `first_contact_date`, `won_date`, `seller_id` | **MQL 월별 성장률**<br>`(이번달 MQL - 전달) / 전달`<br>`GROUP BY origin` |

---

## 2. Activation
### 딜 성사 & 첫 판매 — 리드가 실제 셀러가 되는가
> **분석 1·4 · 전환율 + Time-lag**

| 주요 이벤트 | 사용 테이블 & Join | KPI |
| :--- | :--- | :--- |
| **딜 클로즈 (won)**<br>`closed_deals.won_date`<br>`closed_deals.seller_id` 생성 | **기본 테이블**<br>`mql_leads + closed_deals + order_items + orders` | **채널별 Sales Cycle**<br>`AVG(won_date - first_contact_date)`<br>`GROUP BY origin` |
| **셀러 첫 주문 수령**<br>`order_items.seller_id`<br>최초 `order_id` 등장 | **Join 키**<br>`closed_deals.seller_id = order_items.seller_id` | **Time-to-First-Sale**<br>`AVG(첫 order_items 날짜 - won_date)`<br>`GROUP BY origin` |
| **첫 상품 배송 완료**<br>`orders.order_status = 'delivered'` (첫 건) | **파생 컬럼**<br>`won_date → first_order_date`<br>`time_to_first_sale` (일수) | **채널별 입점 후 미판매율**<br>`seller_id in closed_deals` BUT NOT in `order_items` |

---

## 3. Retention
### 셀러 활성 지속 — 채널별 셀러가 꾸준히 파는가
> **분석 2 · 채널별 RFM**

| 주요 이벤트 | 사용 테이블 & Join | KPI — RFM per 채널 |
| :--- | :--- | :--- |
| **월별 지속 판매**<br>`order_items.seller_id` 월별 연속 등장 | **기본 테이블**<br>`closed_deals + order_items + orders + products` | **Recency — 마지막 판매일**<br>`MAX(order_purchase_timestamp)`<br>`GROUP BY seller_id, origin` |
| **카테고리 확장**<br>`seller_id`별 `product_category` 다양화 | **Join 키**<br>`seller_id` (3-way join)<br>`order_id`, `product_id` | **Frequency — 월 평균 주문 건수**<br>`COUNT(order_id) / active_months`<br>`GROUP BY seller_id, origin` |
| **셀러 이탈 (Churn)**<br>전월 활성 but 당월 0건 판매 | **파생 컬럼**<br>`active_months`, `churn_flag`<br>`category_diversity_count` | **채널별 셀러 Churn Rate**<br>`이탈 seller / 전월 활성 seller`<br>`GROUP BY origin` |

---

## 4. Referral
### 셀러 품질 → 구매자 바이럴 — 좋은 셀러가 플랫폼 평판을 높이는가
> **분석 3 · Attribution**

| 주요 이벤트 | 사용 테이블 & Join | KPI |
| :--- | :--- | :--- |
| **구매자 고평점 리뷰**<br>`order_reviews.review_score ≥ 4`<br>`seller_id` 기준 집계 | **기본 테이블**<br>`closed_deals + order_items + orders + order_reviews` | **채널별 평균 리뷰 점수**<br>`AVG(review_score)`<br>`GROUP BY origin` |
| **저평점 리뷰 (역효과)**<br>`review_score ≤ 2`<br>채널별 불량 셀러 비율 | **Join 키**<br>`seller_id → order_id → review_id` | **채널별 NPS 대리지표**<br>`(score≥4 비율) - (score≤2 비율)`<br>`GROUP BY origin` |
| **배송 준수율**<br>`delivered ≤ estimated_delivery_date` 비율 | **파생 컬럼**<br>`avg_review_score_by_seller`<br>`on_time_delivery_rate` | **채널별 배송 준수율**<br>`on_time orders / total orders`<br>`GROUP BY origin` |

---

## 5. Revenue
### 어느 채널 셀러가 돈이 됐는가
> **분석 3·4·5 · Attribution + LTV + Forecast**

| 주요 이벤트 | 사용 테이블 & Join | KPI |
| :--- | :--- | :--- |
| **셀러 월별 GMV 발생**<br>`order_items.price + freight_value`<br>`seller_id`별 월 합산 | **기본 테이블**<br>`closed_deals + mql_leads + order_items + orders + products + category_translation` | **채널별 총 GMV 기여**<br>`SUM(price + freight_value)`<br>`GROUP BY origin` |
| **고가 카테고리 판매**<br>`products.category × order_items.price` 분포 | **Join 키**<br>`origin → seller_id → order_id → payment_value` | **셀러 LTV (채널별)**<br>`SUM(GMV) / seller_id`<br>`GROUP BY origin (누적)` |
| **선언 매출 vs 실 매출**<br>`declared_monthly_revenue` vs 실제 `order` 매출 | **파생 컬럼**<br>`seller_GMV`, `seller_LTV`, `revenue_per_origin` | **채널 ROI**<br>`GMV_from_origin / estimated_CAC_by_origin`<br><br>**Forecast 변수**<br>`CVR × LTV × 예산 시나리오` → 예상 추가 GMV |

---

## 최종 결론 프레임
### "어디에 예산을 집중하고, 어떤 셀러를 타겟할 것인가"

| 채널 예산 우선순위 결정 기준 | 타겟 셀러 프로필 기준 |
| :--- | :--- |
| **1순위**: `CVR × LTV` 가 모두 높은 채널 — 전환도 잘 되고 오래 판매 | **업종**: `business_segment × GMV` 상위 — 실제 돈이 되는 카테고리 셀러 우선 |
| **2순위**: `CVR` 낮지만 `LTV` 매우 높은 채널 — 소수 고품질 셀러 확보용 | **지역**: `seller_state × GMV` 밀도 — 물류 커버 가능하고 수요 높은 주(state) |
| **축소**: `CVR` 높지만 `LTV` 낮고 `Churn` 빠른 채널 — 볼륨만 채우는 채널 | **규모**: `declared_monthly_revenue × LTV` 상관 — 자기신고 매출이 실적 예측에 유효한지 검증 |
| **제거**: `CVR·LTV` 모두 낮고 `review_score` 도 낮은 채널 | **프로파일**: `lead_behaviour_profile × CVR` — hunter·fisher 중 어느 프로필이 전환율 높은지 |
