# 03-116: Web Scrapper

import requests
from bs4 import BeautifulSoup
import datetime

def web_scrapper_titulares_rt(url = 'actualidad.rt.com'):

    print(f'URL por defecto: {url}')

    user_url = input('Pulsa ENTER para continuar, o introduce la nueva URL - https://')

    if user_url == '':
        final_url = 'https://' + url

    else:
        if user_url.startswith('http'):
            final_url = user_url
        else:
            final_url = f'https://{user_url}'

    
    url_content = requests.get(final_url)

    site_parsed = BeautifulSoup(url_content.text, 'html.parser' )

    headlines = site_parsed.find_all('a', class_='Link-root Link-isFullCard')

    print('Noticias en fecha: ', datetime.datetime.now())

    for headline in headlines:
        titular = headline.get_text(strip=True)
        link = headline.get('href')
        print(f'\nTitular : {titular} \nLink al articulo: {final_url}{link}')

web_scrapper_titulares_rt()

"""
Extraer los titulares del index de actualidad.rt.com:

1. Estructura:

class="Section-block Section-is1to4-sm_is1to2-xs_is1to1 p-24" -> 
<article> class="Card-root Card-isHoverScale Card-default"
<div class="Card-content">
<div class="Card-title"><div class="HeaderNews-root HeaderNews-type_5 "><a href="/actualidad/541714-reino-unido-proporcionar-millones-ucrania" class="Link-root Link-isFullCard ">
                Reino Unido proporcionará más de 2.000 millones de dólares para misiles de defensa aérea a Ucrania
            </a></div></div></div>


LINK + Titular


"""



"""

import requests
from bs4 import BeautifulSoup
import datetime



def web_scrapper_titulares_rt(url = 'actualidad.rt.com'):

    print(f'URL por defecto: {url}')

    user_url = input('Pulsa ENTER para continuar, o introduce la nueva URL - https://')

    if user_url is '':
        final_url = 'https://' + url

    else:
        if user_url.startswith('http'):
            final_url = user_url
        else:
            final_url = f'https://{user_url}'

    
    url_content = requests.get(final_url)

    # Debug
    # print(url_content) # 200, ok

    site_parsed = BeautifulSoup(url_content.text, 'html.parser' )
    # Debug
    # print(site_parsed)

    headlines = site_parsed.find_all('a', class_='Link-root Link-isFullCard')
    links = site_parsed.find_all('href')

    print('Noticias en fecha: ', datetime.datetime.now())

    for headline in headlines:
        titular = headline.get_text(strip=True)
        link = headline.get('href')
        print('\nTitular : ', titular)
        print('Link al articulo: ', f'{url}{link}')

web_scrapper_titulares_rt()
"""




"""

La idea es buena, pero la web despliega su contenido a través de js, por lo que dejamos de necesitar requests,
para usar selenium. Idea fuera.


Let's scrap an Index content from:

devcamp.com/pt-full-stack-development-javascript-python-react



Modules:
class=syllabus-section-header
href=#syllabus-section-X

Guides:

a href= link to post
    class title



Python modules to use:

requests
inflection - It's a string transformation library. It could be useful to .lower(), .upper(), and also singularize-pluralize english words with some "inteligence"
bs4 - extracting elements lubrary


Dentro de:
1. Div class syllabus-header col-md-12
queremos extraer el: div class information ->  div class title -> el titulo del curso.

2. Dentro del syllabus-content-container col-md-12 están todos los modulos, y los sub-cursos de cada modulo, de la siugiente forma:

syllabus-content-container col-md-12 -> div class syllabus-contenet -> div class syllabus-section-header -> div class details -> div class title .... El título de cada módulo

# Attempt 2

import requests
from bs4 import BeautifulSoup

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# selenium opts
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



course = 'https://basque.devcamp.com/pt-full-stack-development-javascript-python-react'

get_the_course = driver.get(course)

course_content = BeautifulSoup(get_the_course.content, 'html.parser')
print('DEBUG: \n', course_content.prettify())

#module_title = course_content.find('div', class_='syllabus-header col-md-12').find('div', class_='information').find('div', class_='title').get_text(strip=True)
#print(module_title)



# ATTEMPT 1
http_request = requests.get('https://devcamp.com/pt-full-stack-development-javascript-python-react')

parser = BeautifulSoup(http_request.text, 'html.parser')

data_parser = parser.find( attrs={'id' : '__NEXT_DATA__'}  ).text

printer_data = json.loads(data_parser)


printer = parser.find_all('title', class_ = 'syllabus-section-header')

print(printer)
"""