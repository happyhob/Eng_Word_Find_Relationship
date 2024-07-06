from bs4 import BeautifulSoup
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
    search_query = 'rude'  # 검색어를 여기에 입력하세요.
    search_box.send_keys(search_query)

    # 검색 실행 (Enter 키 누르기)
    search_box.send_keys(Keys.RETURN)

    # 검색 결과가 로드될 때까지 대기 (필요에 따라 시간 조정)
    time.sleep(1)

    # 유의어사전 버튼 클릭
    thesaurus_button = driver.find_element(By.ID, 'redirectThesaurusdict')
    thesaurus_button.click()

    # 새로 열린 페이지로 전환 (예시)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])  # 마지막으로 열린 탭으로 전환
    
    time.sleep(10)
    # BeautifulSoup을 사용하여 페이지 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 관련 단어 목록 가져오기
    word_items = soup.find_all(class_='similar_word step2')

    # 데이터 출력
    for item in word_items:
        word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'}).text
        print(word)

    # 관련 단어 목록 가져오기
    word_items2 = soup.find_all(class_='similar_word step3')

    # 데이터 출력
    for item in word_items2:
        word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'}).text
        print(word)

    # 관련 단어 목록 가져오기
    word_items3 = soup.find_all(class_='similar_word step4')

    # 데이터 출력
    for item in word_items3:
        word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'}).text
        print(word)

finally:
    # 브라우저 닫기
    driver.quit()
