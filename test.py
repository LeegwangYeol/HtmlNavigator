from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import datetime
import time

class ProgrammingBot:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.project_state = {}
        
    def start_4_minute_cycle(self):
        # 4분 간격으로 봇 실행
        self.scheduler.add_job(
            func=self.execute_programming_cycle,
            trigger=IntervalTrigger(minutes=4),
            id='programming_bot',
            name='Programming Bot Cycle'
        )
        self.scheduler.start()
        
    def execute_programming_cycle(self):
        """4분마다 실행되는 메인 프로세스"""
        try:
            # 1. 현재 프로젝트 상태 분석
            current_state = self.analyze_project_state()
            
            # 2. AI에게 상황 보고 및 다음 작업 요청
            task_result = self.interact_with_ai(current_state)
            
            # 3. 결과 저장 및 프로젝트 상태 업데이트
            self.save_and_update_project(task_result)
            
        except Exception as e:
            self.log_error(f"Cycle execution failed: {e}")
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def get_perplexity_answer(prompt: str):
    driver = None
    try:
        # 기존 옵션 설정
        options = uc.ChromeOptions()
        options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # 드라이버 설정
        driver = uc.Chrome(
            options=options,
            use_subprocess=False,
            service_log_path='chromedriver.log'  # 로그 파일 지정
        )
        # 1. 브라우저 설정 (Brave 브라우저 경로 지정 및 감지 회피 옵션)
        options = uc.ChromeOptions()
        
        # Windows 기준 Brave 브라우저 경로 (Mac의 경우 경로 수정 필요)
        # 예: /Applications/Brave Browser.app/Contents/MacOS/Brave Browser
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        options.binary_location = brave_path
        
        # 자동화 탐지를 회피하기 위한 옵션들
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # 2. Undetected ChromeDriver 실행
        driver = uc.Chrome(
            options=options,
            use_subprocess=False # 메모리 사용량 감소에 도움
        )
        
        # navigator.webdriver 속성을 undefined로 변경하여 탐지 회피
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # 3. Perplexity.ai 접속
        print("Perplexity.ai에 접속합니다...")
        driver.get("https://www.perplexity.ai")
        
        # 페이지 로드를 위한 대기
        time.sleep(random.uniform(2, 4))
        
        # 4. 질문 입력창 찾기 (WebDriverWait 사용)
        wait = WebDriverWait(driver, 15)
        textarea = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder*='Ask anything']"))
        )
        
        # 5. 인간처럼 자연스럽게 질문 입력
        print(f"질문을 입력합니다: '{prompt}'")
        for char in prompt:
            textarea.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15)) # 0.05초에서 0.15초 사이의 랜덤 딜레이
            
        time.sleep(random.uniform(0.5, 1.0))

        # 6. 전송 버튼 클릭
        submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label*='Submit']"))
        )
        submit_button.click()
        print("질문을 전송했습니다. 답변을 기다립니다...")

        # 7. 답변이 생성될 때까지 대기 및 결과 가져오기
        # 답변 영역은 여러 개의 div로 구성되어 있어, 상위 컨테이너를 기다림
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='prose']"))
        )
        
        # 답변을 포함하는 모든 텍스트 블록을 수집
        answer_elements = driver.find_elements(By.CSS_SELECTOR, "div[class*='prose'] p")
        
        # 결과 텍스트를 하나로 합침
        full_answer = "\n".join([elem.text for elem in answer_elements if elem.text.strip()])
        
        return full_answer

    except Exception as e:
        print(f"오류 발생: {str(e)}")
        return None
    finally:
        # 드라이버 종료 방식 변경
        try:
            if driver:
                driver.quit()
        except:
            pass
        print("브라우저 세션을 정리했습니다.")


if __name__ == "__main__":
    try:
        question = "오늘 서울 날씨는 어떠니"
        print(f"질문: {question}")
        answer = get_perplexity_answer(question)
        
        if answer:
            print("\n--- Perplexity 답변 결과 ---")
            print(answer)
            print("--------------------------")
            
    except Exception as e:
        print(f"메인 실행 중 오류 발생: {e}")
    finally:
        import gc
        gc.collect()  # 가비지 컬렉션 강제 실행