from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def findWoedRelationship(word):
    synonyms_1=[]
    synonyms_2=[]
    dicts={}
    dicts['title'] = word
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
        search_query = word  # 검색어를 여기에 입력하세요.
        search_box.send_keys(search_query)

        # 검색 실행 (Enter 키 누르기)
        search_box.send_keys(Keys.RETURN)

        # 검색 결과가 로드될 때까지 대기 (필요에 따라 시간 조정)
        # time.sleep(3)

        # 유의어사전 버튼 클릭
        thesaurus_button = driver.find_element(By.ID, 'redirectThesaurusdict')
        thesaurus_button.click()

        # 새로 열린 페이지로 전환 (예시)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])  # 마지막으로 열린 탭으로 전환

        time.sleep(1)


        # BeautifulSoup을 사용하여 페이지 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # "유의어" 섹션 전체 선택
        synonym_section = soup.find('div', class_='relation_word_group synonym multi')
        
        # 유의어 목록 가져오기
        synonyms = []
        word_areas = synonym_section.find_all('div', class_='word_area')
        for word_area in word_areas:
            word_list = word_area.find_all('li', class_='relation_word_item')
            for item in word_list:
                word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'})
                if word:
                    synonyms.append(word.text.strip())
        

        # print("유의어:")
        for synonym in synonyms:
            synonyms_1.append(synonym)
            # print(synonym)
            

        dicts['유의어'] = synonyms_1

        # "반의어" 섹션 전체 선택
        synonym_section2 = soup.find('div', class_='relation_word_group antonym')


        # 반의어 목록 가져오기
        synonyms2 = []
        word_areas2 = synonym_section2.find_all('div', class_='word_area')
        for word_area in word_areas2:
            word_list = word_area.find_all('li', class_='relation_word_item')
            for item in word_list:
                word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'})
                if word:
                    synonyms2.append(word.text.strip())

        # print("반의어:")
        for synonym in synonyms2:
            synonyms_2.append(synonym)
            # print(synonym)
        dicts['반의어'] = synonyms_2

        
    finally:
        # 브라우저 닫기
        driver.quit()
        return dicts


def test(dict):
    
    if '유의어' in dict:
        print()
        print(dict['유의어'])
    else:
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
            search_query = dict['title']  # 검색어를 여기에 입력하세요.
            search_box.send_keys(search_query)
            # 검색 실행 (Enter 키 누르기)
            search_box.send_keys(Keys.RETURN)


            # 유의어사전 버튼 클릭
            thesaurus_button = driver.find_element(By.ID, 'redirectThesaurusdict')
            thesaurus_button.click()
            # 새로 열린 페이지로 전환 (예시)
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])  # 마지막으로 열린 탭으로 전환
            time.sleep(1)
            # BeautifulSoup을 사용하여 페이지 파싱
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # 관련 단어 목록 가져오기
            word_items = soup.find_all('li', class_='relation_word_item')
            # 데이터 출력
            for item in word_items:
                word = item.find('span', {'data-type': 'ore', 'data-lang': 'en'}).text
                print(word)
        finally:
            # 브라우저 닫기
            driver.quit()


dicts = findWoedRelationship('rudeness')
print(dicts)

test(dicts)