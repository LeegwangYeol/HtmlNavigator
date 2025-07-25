from selenium import webdriver
import time

# 1. Brave 브라우저 실행 파일의 실제 경로를 지정합니다.
# 아래는 일반적인 Windows 경로이며, 사용자의 PC 환경에 맞게 수정해야 합니다.
# macOS 예시: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# 2. Selenium 웹 드라이버 옵션을 설정합니다.
options = webdriver.ChromeOptions()
options.binary_location = brave_path

driver = None  # driver 변수 초기화
try:
    # 3. 설정한 옵션으로 Brave 브라우저를 실행합니다.
    # 최신 Selenium은 호환되는 ChromeDriver를 자동으로 다운로드 및 관리해줍니다.
    print("Brave 브라우저를 실행합니다...")
    driver = webdriver.Chrome(options=options)

    # 4. 구글 홈페이지로 이동합니다.
    print("Google.com으로 이동합니다...")
    driver.get("https://www.google.com")

    # 5. 브라우저가 바로 닫히는 것을 방지하기 위해 10초간 대기합니다.
    print("10초 후에 브라우저가 자동으로 종료됩니다.")
    time.sleep(10)

except Exception as e:
    print(f"오류가 발생했습니다: {e}")
    print("Brave 브라우저의 경로가 올바른지, 또는 네트워크 연결을 확인해주세요.")

finally:
    # 6. 작업이 끝나면 브라우저를 종료합니다.
    if driver:
        driver.quit()
        print("브라우저를 종료했습니다.")
