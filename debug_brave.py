from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_brave_with_fixed_driver():
    try:
        print("프로그램 시작")
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        
        options = Options()
        options.binary_location = brave_path
        options.add_argument("--start-maximized")
        
        # 불필요한 옵션 제거
        # options.add_argument("--disable-dev-shm-usage")  # 주로 Linux에서만 필요한 옵션
        # options.add_argument("--no-sandbox")  # 보안상 권장되지 않음
        
        # webdriver-manager 대신 간단한 방식 사용
        driver = webdriver.Chrome(options=options)
    
        print("구글 접속 시도...")
        driver.get("https://www.perplexity.ai/")
        print(f"현재 URL: {driver.current_url}")
        print(f"페이지 제목: {driver.title}")
        time.sleep(1000)
        return True
        
    except Exception as e:
        print(f"오류 발생: {e}")
        return False
    finally:
        if 'driver' in locals():
            driver.quit()
            print("드라이버 종료")


            
# 파일의 맨 아래에 다음 코드를 추가
if __name__ == "__main__":
   
    test_brave_with_fixed_driver()