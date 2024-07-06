from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# ChromeDriver 설정
service = ChromeService(executable_path=ChromeDriverManager().install())

# WebDriver 초기화
driver = webdriver.Chrome(service=service)

try:
    # 웹 페이지 열기
    driver.get('https://en.dict.naver.com/')  # 여기에 실제 검색 페이지의 URL을 입력하세요.

    # input 요소 찾기
    search_box = driver.find_element(By.ID, 'ac_input')

    # 검색어 입력
    search_query = 'example search'  # 검색어를 여기에 입력하세요.
    search_box.send_keys(search_query)

    # 검색 실행 (Enter 키 누르기)
    search_box.send_keys(Keys.RETURN)

    # 검색 결과가 로드될 때까지 대기 (필요에 따라 시간 조정)
    time.sleep(5)

    # 검색 결과 가져오기 (예시: 검색 결과의 타이틀을 가져오기)
    results = driver.find_elements(By.CSS_SELECTOR, '.result')  # 검색 결과의 CSS 셀렉터를 여기에 입력하세요.

    # 결과 출력
    for result in results:
        title = result.find_element(By.TAG_NAME, 'h2').text  # 결과 타이틀의 태그를 여기에 입력하세요.
        print(title)
finally:
    # 브라우저 닫기
    driver.quit()
