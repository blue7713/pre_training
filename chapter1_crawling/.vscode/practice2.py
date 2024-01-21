# 1. 라이브러리 임포트
import requests  # 웹페이지 가죠오기 라이브러리
from bs4 import BeautifulSoup  # 웹페이지 분석(크롤링) 라이브러리

# 2. 웹페이지 가져오기 res.content 확인하기
res = requests.get("https://davelee-fun.github.io/blog/crawl_test")
# ctrl + shift + i -> 오픈 크롬 개발자 모드 참고

html = """
<html> 
    <body>
        <h1 id='title'>[1]크롤링이란?</h1>
            <p class='cssstyle>웹페이지에서 필요한 데이터를 추출하는 것</p>
            <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
        </body>
</html>
"""

# 3. 웹페이지 파싱(문자열의 의미 분석)하기, soup에 HTML 파일을 파싱한 정보가 들어감
soup = BeautifulSoup(
    res.content, "html.parser"
)  # (분석할 주소, 파싱 지정) -> soup에 구조화된 주소의 html 정보가 들어감

# 4. 필요한 데이터 추출하기, soup.find()함수로 원하는 부분을 지정, 변수.get_text()함수로 추출한 부분을 가져올 수 있음
section = soup.find("ul", id="dev_course_list")
titles = section.find_all("li", "course")
# data = soup.find('p', class='cssstyle')
# data = soup.find('p', 'cssstyle')
# data = soup.find('p', attr = {'align': 'center'})
# data = soup.find(id='body')

for index, item in enumerate(titles):
    print(str(index + 1) + ".", item.get_text().split("[")[0].split("-")[1].strip())
# print(data)
# print(data.get_text())
# print(data.string)

# 마크업 언어 : 문서나 데이터의 구조를 표현하는 언어(HTML, CSS)
