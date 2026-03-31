# Dataset 제안 – Olist + Marketing Funnel

## 1. Brazilian E-Commerce Public Dataset by Olist

- Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce[cite:265]
- 개요  
  - 2016–2018년 약 10만 건의 주문 데이터를 포함한 브라질 이커머스 실거래 데이터셋.[cite:259][cite:257]  
  - 주문, 고객, 결제, 배송, 리뷰, 제품, 판매자, 지리정보 등 8개 테이블로 구성되어 있어 주문을 여러 관점(상태, 가격, 결제, 배송 성과, 고객 위치, 상품 속성, 리뷰)에서 분석 가능.[cite:259][cite:261]

### 데이터 특징 (요약)

- 주문 단위 테이블: `orders`, `order_items`, `order_payments`, `order_reviews` 등.
- 고객/판매자: `customers`, `sellers`, `geolocation` 테이블로 지역·도시·주(state) 분석 가능.[cite:259][cite:261]
- 제품: 카테고리, 무게·치수 등 속성이 포함된 `products` 테이블.
- 기간: 약 2년(2016–2018) 동안의 주문·배송 데이터가 포함되어 시계열·코호트 분석에 적합.[cite:259][cite:265]

---

## 2. Marketing Funnel by Olist

- Kaggle: https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist[cite:113]
- Olist 공식 설명:  
  - 약 8k개의 **Marketing Qualified Leads (MQL)**가 포함된 마케팅 퍼널 데이터셋.[cite:149][cite:152]  
  - 리드 카테고리, 카탈로그 크기, 리드 출처(origin, 채널), 행동 프로필 등 리드 특성을 여러 차원에서 볼 수 있음.[cite:149][cite:152]  
  - `seller_id`로 브라질 이커머스 데이터셋과 조인 가능 → 리드·채널·세일즈 퍼널과 실제 주문/매출 데이터가 연결된다.[cite:149][cite:152]

### 데이터 특징 (요약)

- 리드 단위 정보:  
  - 리드 생성 날짜, 리드 소스(채널, origin), 세일즈 담당 단계(SDR, SR), 리드 상태 등.[cite:149][cite:232]
- 조인 구조:  
  - `seller_id`를 통해 브라질 이커머스 주문 데이터(100k orders)와 연결, 리드→판매자→주문·매출까지 추적 가능.[cite:149][cite:157]

---

## 3. 참고 자료 (레퍼런스)

- Olist 데이터셋 구조 정리:  
  - https://ngocyen99tb.lelouvincx.com/docs/olist/dataset/[cite:259]
- GitHub 분석 예시:  
  - https://github.com/Nikhilkohli1/Olist-Marketing-Analytics[cite:222]  
  - https://github.com/SophieHuGit/OlistEcommerceAnalytics[cite:157]

---

## 4. 가능한 분석 주제

### 4.1 세일즈 퍼널 & 채널 성과 분석

1. **리드→기회→딜→매출 퍼널 분석**
   - Marketing Funnel 데이터에서 리드 상태, SDR/SR 진행 단계, 클로즈 여부를 기반으로 단계별 전환율 계산.[cite:149][cite:232]
   - 브라질 이커머스 주문 데이터와 조인하여, 클로즈된 리드가 실제 어느 정도 매출로 이어졌는지 확인.

2. **채널(origin)별 리드 품질·전환율·매출 비교**
   - 채널별(Mail, Paid Search, Organic Search, Direct, Social 등) MQL 수, 딜 수, 전환율 계산.[cite:224][cite:232]
   - 채널별로 연결된 판매자의 주문 수·매출·리텐션(재구매율)을 비교하여 “양은 많은데 질이 낮은 채널 vs 양은 적어도 고가치 리드가 많은 채널” 식 인사이트 도출.

3. **세일즈 사이클·리드 속성별 성과**
   - 리드 속성(리드 카테고리, 카탈로그 크기, 비즈니스 세그먼트 등)에 따른 전환율·평균 세일즈 리드타임(리드 생성→첫 주문까지 걸린 시간)을 분석.[cite:149][cite:232]

---

### 4.2 고객·공급자(판매자) 성과 및 LTV 분석

1. **공급자(판매자) 성과 분석**
   - 판매자별 월 매출, 주문 수, 취소율, 배송 지연률, 리뷰 점수 산출.[cite:259][cite:261]
   - 상위 10% 판매자의 월별 매출 성장률과 전체 GMV(총 상품가치) 비중을 계산해 “Top sellers vs Long tail” 구조 파악.[cite:259]

2. **고객·판매자 리텐션 및 LTV 분석**
   - 고객/판매자 코호트(첫 구매/첫 주문 월 기준)별로 1·3·6개월 재구매율, 평균 주문 수, 평균 매출을 추적.[cite:259][cite:261]
   - 신규 vs 재구매 고객 비중, 고객별/판매자별 LTV(평균 주문 금액 × 재구매 횟수 추정) 비교.

3. **리드 채널별 LTV 차이**
   - 리드 소스(origin)별로 연결된 판매자의 매출과 코호트 리텐션을 비교하여, **채널별로 “고가치 판매자/고가치 고객을 얼마나 많이 데려오는지”** 평가.

---

### 4.3 AARRR 관점 퍼널 분석

- **Acquisition**  
  - Marketing Funnel의 리드 소스·캠페인별 유입량(신규 리드 수)을 Acquisition 지표로 사용.[cite:149][cite:232]

- **Activation**  
  - 리드가 실제로 Olist에서 첫 주문까지 이어지는 비율, 첫 주문까지 걸리는 시간 등으로 Activation 정의.

- **Retention**  
  - 고객/판매자 코호트별 반복 주문·재판매 패턴을 분석해 Retention 지표 산출.[cite:259][cite:261]

- **Revenue**  
  - 고객·판매자 단위 매출·마진(추정)을 기반으로 Revenue 지표 구성.

- **Referral (간접)**  
  - 리뷰 점수, 리뷰 내용(만족도) 등을 NPS 유사 지표로 활용해 입소문/추천 가능성 가정.

---

## 5. BA 관점에서의 활용 포인트

- “마케팅 퍼널(MQL→딜) + 실제 매출”을 한 번에 다루면서,  
  - 퍼널 KPI·OKR 설정  
  - 채널 전략 및 예산 재배분 시나리오  
  - 리드 스코어링 및 세일즈 파이프라인 운영  
까지 연결하는 **전사 관점 BA 스토리**를 만들기 좋다.[cite:149][cite:232][cite:222]

- 다만, 데이터셋에 **채널·캠페인별 ‘실제 마케팅 비용’ 컬럼은 없기 때문에**,  
  - 진짜 화폐 기준 ROI는 외부 단가(예: 채널별 리드 1건당 비용)를 가정해서 계산해야 한다.  
  - 대신, 전환율·LTV·리드 품질 지표를 활용해 **“ROI 사고방식”에 가까운 효율 평가와 시나리오 분석**은 충분히 가능하다.
