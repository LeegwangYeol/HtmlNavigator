from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def test_brave_connection():
    # Brave 브라우저 경로 설정
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    
    options = Options()
    options.binary_location = brave_path  # Brave 브라우저 경로 지정
    
    # 기본 옵션 설정
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # 사용자 에이전트 설정
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f'user-agent={user_agent}')

    # 1. Brave 브라우저로 구글 접속 테스트
    print("1. Brave 브라우저로 구글 접속 시도 중...")
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.google.com")
        print("✓ 구글 접속 성공")
        time.sleep(2)
    except Exception as e:
        print(f"✗ 구글 접속 실패: {str(e)}")
        return False
    finally:
        if driver:
            driver.quit()

    # 2. Perplexity 접속 테스트
    print("\n2. Brave 브라우저로 Perplexity 접속 시도 중...")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.perplexity.ai")
        time.sleep(5)  # 페이지 로드 대기
        
        if "perplexity" in driver.title.lower():
            print("✓ Perplexity 접속 성공")
            print(f"페이지 제목: {driver.title}")
        else:
            print("✗ Perplexity 접속 실패 - 차단된 것으로 보입니다.")
            print(f"실제 페이지 제목: {driver.title}")
            print("페이지 소스 일부:")
            print(driver.page_source[:500])  # 처음 500자만 출력
            
        return True
        
    except Exception as e:
        print(f"✗ Perplexity 접속 중 오류: {str(e)}")
        return False
    finally:
        if 'driver' in locals() and driver:
            try:
                driver.quit()
            except:
                pass

if __name__ == "__main__":
    print("=== Brave 브라우저 연결 테스트 시작 ===")
    test_brave_connection()
    input("\n테스트 완료. 결과를 확인하시고 엔터를 누르세요...")