import os
import shutil
import subprocess
import sys

def install_package(package):
    """Installs a python package via pip."""
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def setup_data():
    """Downloads Olist datasets and organizes them in /data/."""
    try:
        import kagglehub
    except ImportError:
        install_package("kagglehub")
        import kagglehub

    # Define paths
    base_dir = os.getcwd()
    data_dir = os.path.join(base_dir, "data")
    ecommerce_dir = os.path.join(data_dir, "brazilian-ecommerce")
    funnel_dir = os.path.join(data_dir, "marketing-funnel")

    # Ensure directories exist
    os.makedirs(ecommerce_dir, exist_ok=True)
    os.makedirs(funnel_dir, exist_ok=True)

    print("--- 🚀 Olist 데이터 세팅 시작 ---")

    # 1. Marketing Funnel
    print("📥 Marketing Funnel 데이터 다운로드 중...")
    funnel_path = kagglehub.dataset_download("olistbr/marketing-funnel-olist")
    print(f"✅ 다운로드 완료: {funnel_path}")
    
    for f in os.listdir(funnel_path):
        if f.endswith(".csv"):
            shutil.copy2(os.path.join(funnel_path, f), funnel_dir)
            print(f"   ㄴ 복사됨: {f} -> data/marketing-funnel/")

    # 2. Brazilian E-commerce
    print("\n📥 Brazilian E-commerce 데이터 다운로드 중...")
    ecommerce_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
    print(f"✅ 다운로드 완료: {ecommerce_path}")
    
    for f in os.listdir(ecommerce_path):
        if f.endswith(".csv"):
            shutil.copy2(os.path.join(ecommerce_path, f), ecommerce_dir)
            print(f"   ㄴ 복사됨: {f} -> data/brazilian-ecommerce/")

    print("\n--- ✨ 모든 설정이 완료되었습니다! ---")
    print("이제 'git add data/'를 통해 데이터를 깃허브에 푸시할 수 있습니다.")

if __name__ == "__main__":
    setup_data()
