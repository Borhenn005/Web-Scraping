import requests
from bs4 import BeautifulSoup
import csv

date = input("Please enter a date in the following format : MM/DD/YYYY :")
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")


def main(page):
    #content : renvoie le page web en byte code 
    src = page.content
    soup = BeautifulSoup(src,"lxml")

    championships = soup.find_all('div',{'class' : 'matchCard'})


    def get_match_info(championship):
        championship_title = championship.contents[1].find('h2').text.strip()
        print(championship_title)


    for index in range(len(championships)):
        get_match_info(championship = championships[index])


main( page = page )