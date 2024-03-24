import requests
from datetime import datetime
import csv
from bs4 import BeautifulSoup as bs

##이름을 넣어보세요. 내 이름이 얼마나 많은 사람들이 사용하고 있는지 알려드립니다!

try:
    myName = input('이름을 입력하세요:')
    headers = {}
    # 헤더 없이도 요청되는 착한 사이트(근데 애들도 api따오는 듯...)
    response = requests.get(f"https://www.name-ranking.com/name/{myName}", headers=headers)
    
    if response.status_code == 200:
        html_text = response.text
        soup = bs(response.text, 'html.parser')
        
        today = datetime.now().strftime('%Y-%m-%d')
        
        file = open(f"{today}MynameCounter.csv", mode='w', newline='')
        writer = csv.writer(file)
        writer.writerow(['이름', '랭킹', '사용자수', '남자비율'])        
        #몇명
        cnt = soup.find(class_='cnt').text
        print(cnt)
        #랭킹
        rank = soup.find(class_='ranking').find('span').text
        print(rank)
        #남지비율
        male = soup.find(class_='lgd m').find('span').text
        print(male)
        
        writer.writerow([myName, rank, cnt, male])
        
        file.close()
    else:
        print(f"Error {response.status_code}")

except requests.exceptions.RequestException as e:
    print(e)