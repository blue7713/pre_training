import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawl_test_css.html")
soup = BeautifulSoup(res.content, "html.parser")
# items = soup.select('li > a') # ul 태그 바로 밑의 a 태그 선택
items = soup.select("ul#dev_course_list > li.course.paid")  # ul 태그 밑의 a 태그 선택
# items = soup.select('.course') # course class 선택
# items = soup.select('#start') # id = start 의미
# items = soup.select('li.course.paid') # li 태그의 cource paid class 선택
for item in items:
    print(item.get_text())

data = soup.select_one("ul#dev_course_list > li.course.paid")
print(data.get_text())

res = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
soup = BeautifulSoup(res.content, "html.parser")

items = soup.select("tr")  # 행 데이터 가져오기
for item in items:
    columns = item.select("td")  # 행 안의 열 정보 가져오기
    row_str = ""
    for column in columns:
        row_str += ", " + column.get_text()
    print(row_str[2:])
