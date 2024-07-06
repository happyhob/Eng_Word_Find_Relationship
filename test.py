from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ChromeDriver 경로 설정
chrome_driver_path = "C:\\Users\\caapb\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  # ChromeDriver 경로를 입력하세요.

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드 (브라우저 창을 띄우지 않음)

# WebDriver 생성
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 크롤링할 웹페이지 URL
url = 'https://www.thesaurus.com/'  # 검색 기능이 있는 웹페이지 URL을 입력하세요.

# 웹페이지 열기
driver.get(url)

# 페이지 로딩 대기
driver.implicitly_wait(10)

# 검색 입력 필드 찾기 및 텍스트 입력
search_input = driver.find_element(By.ID, 'global-search')
search_input.send_keys('example search term')  # 검색할 텍스트를 입력하세요.

# 검색 버튼 클릭
search_button = driver.find_element(By.CLASS_NAME, 'BPEynxB5UemsqiLj7s2H')
search_button.click()

# 결과 페이지 로딩 대기
driver.implicitly_wait(10)

# 필요한 작업 수행 (예: 검색 결과 추출)

# 예제: 결과 페이지에서 첫 번째 검색 결과의 텍스트 추출
first_result = driver.find_element(By.CSS_SELECTOR, 'your-result-selector')  # 결과를 찾을 수 있는 적절한 CSS 선택자를 입력하세요.
print(first_result.text)

# 브라우저 닫기
driver.quit()
