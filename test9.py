from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


WEB_URL = "https://en.dict.naver.com/"


def findWordMean(word):
    # ChromeDriver 설정
        service = ChromeService(executable_path=ChromeDriverManager().install())
        # WebDriver 초기화
        driver = webdriver.Chrome(service=service)
        try:
            # 웹 페이지 열기
            driver.get(WEB_URL)  # 여기에 실제 검색 페이지의 URL을 입력하세요.
            # input 요소 찾기
            search_box = driver.find_element(By.ID, 'ac_input')
            # 검색어 입력
            search_query = word  # 검색어를 여기에 입력하세요.
            search_box.send_keys(search_query)
            # 검색 실행 (Enter 키 누르기)
            search_box.send_keys(Keys.RETURN)


            # # 유의어사전 버튼 클릭
            # thesaurus_button = driver.find_element(By.ID, 'redirectThesaurusdict')
            # thesaurus_button.click()
            # # 새로 열린 페이지로 전환 (예시)
            # handles = driver.window_handles
            # driver.switch_to.window(handles[-1])  # 마지막으로 열린 탭으로 전환
            time.sleep(1)
            # BeautifulSoup을 사용하여 페이지 파싱
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Find the <a> tag
            a_tag = soup.find('a', class_='link')

            # Extract the href attribute
            href_value = a_tag['href']

            newUrl = WEB_URL + href_value
            print(newUrl)
            driver.get(newUrl)
            
            time.sleep(3)
            # # 관련 단어 목록 가져오기
            entries = soup.find_all('div', class_='entry_mean_item')

            # 각 요소에서 meaning 클래스 안의 내용 추출
            for entry in entries:
                meaning = entry.find('p', class_='meaning').text
                print(meaning)
        finally:
            # 브라우저 닫기
            driver.quit()



# dicts = findWoedRelationship('rude')
# print(dicts)

findWordMean('rude')



