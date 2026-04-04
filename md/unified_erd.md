# 🗺️ 통합 ERD (Unified ERD: Funnel + E-Commerce)

이 다이어그램은 **Olist 마케팅 퍼널 데이터**와 **브라질 이커머스 매출 데이터**가 어떻게 연결되는지 보여줍니다. 핵심 연결 고리는 `mql_id`와 `seller_id`입니다.

```mermaid
erDiagram
    %% Marketing Funnel Dataset
    MQLs {
        string mql_id PK
        datetime first_contact_date
        string landing_page_id
        string origin
    }

    Closed_Deals {
        string mql_id FK
        string seller_id FK
        string sdr_id
        string sr_id
        datetime won_date
        string business_segment
        string lead_type
    }

    %% Brazilian E-Commerce Dataset
    Sellers {
        string seller_id PK
        string seller_zip_code_prefix
        string seller_city
        string seller_state
    }

    Order_Items {
        string order_id FK
        int order_item_id
        string product_id FK
        string seller_id FK
        float price
        float freight_value
    }

    Orders {
        string order_id PK
        string customer_id FK
        string order_status
        datetime order_purchase_timestamp
        datetime order_delivered_customer_date
    }

    Customers {
        string customer_id PK
        string customer_unique_id
        string customer_zip_code_prefix
        string customer_city
        string customer_state
    }

    Products {
        string product_id PK
        string product_category_name
        int product_weight_g
    }

    Order_Payments {
        string order_id FK
        int payment_sequential
        string payment_type
        float payment_value
    }

    Order_Reviews {
        string review_id PK
        string order_id FK
        int review_score
        string review_comment_message
    }

    %% Relationships
    MQLs ||--o| Closed_Deals : "mql_id"
    Closed_Deals ||--|| Sellers : "seller_id (Connects Funnel to Revenue)"
    Sellers ||--o{ Order_Items : "seller_id"
    Order_Items }|--|| Orders : "order_id"
    Order_Items }|--|| Products : "product_id"
    Orders ||--o{ Order_Payments : "order_id"
    Orders ||--o{ Order_Reviews : "order_id"
    Orders }|--|| Customers : "customer_id"
```

### 🔗 핵심 분석 경로 (The Golden Path)
1. **유입(Acquisition)**: `MQLs.origin` 을 통해 리드가 어디서 왔는지 파악
2. **전환(Conversion)**: `Closed_Deals` 에서 어떤 리드가 실제 셀러가 되었는지 확인
3. **성과(Revenue)**: `Order_Items` 와 `Orders` 를 조인하여 해당 셀러가 발생시킨 실제 매출액 산출
4. **결론**: **MQL Origin별 평균 매출(LTV)과 ROI**를 계산하여 마케팅 예산 최적화
