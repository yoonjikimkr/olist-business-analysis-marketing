import pandas as pd
import re
import os

WORDS_CSV  = r"c:/Users/L095544/Olist/olist-business-analysis-marketing/dashboard/review_sentiment_words.csv"
DATA_DIR   = "data/brazilian-ecommerce"
OUT_PATH   = "data/processed/review_sentiment_words.csv"

def count_word_in_text(word, text):
    if not isinstance(text, str):
        return 0
    return len(re.findall(r'\b' + re.escape(word) + r'\b', text.lower()))

def main():
    # 1. 기존 큐레이션 단어 목록 (word, english, sentiment, count, specificity)
    words_df = pd.read_csv(WORDS_CSV)
    word_list = words_df["word"].tolist()
    word_meta = words_df.set_index("word")[["english", "sentiment", "specificity"]]
    print(f"Curated words: {len(word_list)} ({words_df['sentiment'].value_counts().to_dict()})")

    # 2. 원본 리뷰 + order_items + sellers 로드
    reviews = pd.read_csv(f"{DATA_DIR}/olist_order_reviews_dataset.csv",
                          usecols=["order_id", "review_comment_message", "review_score"])
    items   = pd.read_csv(f"{DATA_DIR}/olist_order_items_dataset.csv",
                          usecols=["order_id", "seller_id"]).drop_duplicates("order_id")
    sellers = pd.read_csv(f"{DATA_DIR}/olist_sellers_dataset.csv",
                          usecols=["seller_id", "seller_state"])

    df = (reviews[reviews["review_comment_message"].notna()]
          .merge(items,   on="order_id",  how="inner")
          .merge(sellers, on="seller_id", how="inner"))
    print(f"Reviews with text: {len(df):,}")

    # 3. 각 리뷰에서 큐레이션 단어 등장 횟수 추출
    rows = []
    for _, row in df.iterrows():
        text = row["review_comment_message"]
        for word in word_list:
            cnt = count_word_in_text(word, text)
            if cnt > 0:
                rows.append({
                    "word":         word,
                    "order_id":     row["order_id"],
                    "seller_state": row["seller_state"],
                    "count":        cnt,
                })

    result = pd.DataFrame(rows)

    # 4. 메타데이터(english, sentiment, specificity) 붙이기
    result = result.join(word_meta, on="word")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    result.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")
    print(f"Rows: {len(result):,}  |  Unique words: {result['word'].nunique()}"
          f"  |  Unique orders: {result['order_id'].nunique():,}")
    print(f"Columns: {list(result.columns)}")

    # 검증: 단어별 count 합계 vs 원본
    agg = result.groupby("word")["count"].sum().reset_index()
    check = agg.merge(words_df[["word","count"]], on="word", suffixes=("_new","_orig"))
    check["diff"] = check["count_new"] - check["count_orig"]
    print("\nTop-5 단어 검증 (new vs orig count):")
    print(check.nlargest(5, "count_orig")[["word","count_new","count_orig","diff"]].to_string(index=False))

if __name__ == "__main__":
    main()
