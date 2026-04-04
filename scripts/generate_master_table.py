import pandas as pd
import os

def generate_master_table():
    """Joins MQL, Closed Deals, and Order data to create an Analytical Base Table (ABT)."""
    print("--- 🛠️ 분석용 마스터 테이블(ABT) 생성 시작 ---")
    
    # 1. 원본 데이터 로드
    mql = pd.read_csv("data/marketing-funnel/olist_marketing_qualified_leads_dataset.csv")
    closed_deals = pd.read_csv("data/marketing-funnel/olist_closed_deals_dataset.csv")
    order_items = pd.read_csv("data/brazilian-ecommerce/olist_order_items_dataset.csv")
    
    print(f"📊 로드 완료: MQL({len(mql)}행), Closed Deals({len(closed_deals)}행), Order Items({len(order_items)}행)")

    # 2. MQL + Closed Deals (Left Join: 모든 잠재 고객 유지)
    # 어떤 채널(Origin)에서 온 리드가 계약까지 갔는지 확인 가능
    df = pd.merge(mql, closed_deals, on="mql_id", how="left")
    
    # 3. 셀러별 매출 데이터 집계
    # Order Items에서 셀러별 총 매출(Price)과 총 주문 건수 계산
    seller_stats = order_items.groupby("seller_id").agg(
        total_revenue=("price", "sum"),
        total_order_count=("order_id", "nunique"),
        first_sale_date=("shipping_limit_date", "min")
    ).reset_index()

    # 4. 마케팅 데이터 + 셀러 매출 데이터 결합 (Left Join)
    # 계약이 성사된 셀러 중 실제 판매가 발생한 데이터 연결
    final_df = pd.merge(df, seller_stats, on="seller_id", how="left")
    
    # 5. 파생 변수 생성
    # 계약 성공 여부 (is_won)
    final_df["is_won"] = final_df["won_date"].notna().astype(int)
    # 매출 발생 여부 (has_revenue)
    final_df["has_revenue"] = final_df["total_revenue"].notna().astype(int)
    # 결측치 처리 (매출이 없는 경우 0)
    final_df["total_revenue"] = final_df["total_revenue"].fillna(0)
    final_df["total_order_count"] = final_df["total_order_count"].fillna(0)

    # 6. 결과 저장
    output_path = "data/processed/marketing_sales_base.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_df.to_csv(output_path, index=False)
    
    print(f"\n✨ 생성 완료: {output_path}")
    print(f"📈 최종 마스터 테이블 행 수: {len(final_df)}행")
    print("-" * 40)
    print("마스터 테이블 활용 예시:")
    print(" - Origin(채널)별 전환율 (Conversion Rate)")
    print(" - Origin별 평균 매출 (LTV)")
    print(" - Business Segment별 성과 비교")

if __name__ == "__main__":
    generate_master_table()
