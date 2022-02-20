from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from time import sleep

def write_to_file(file, lst_of_ratings, lst_of_movies):
    with open(file, mode='w') as file1:
        for ind in range(len(lst_of_movies)):
            file1.write(lst_of_movies[ind][0] + '\n')
            file1.write("Rating of the movie: " + lst_of_ratings[ind] + '\n')
            file1.write("Link of the movie: " + lst_of_movies[ind][1] + "\n\n")

def get_movies(driver, file):

    lst_of_movies = [] 
    lst_of_ratings = []
    
    movies = driver.find_elements_by_class_name('titleColumn')
    ratings = driver.find_elements_by_class_name('ratingColumn')

    for movie in movies[:10]:
        movie_name = movie.text.split('. ', 1)[1][:-7]
        movie_link = driver.find_element_by_link_text(movie_name).get_attribute('href')
        lst_of_movies.append([movie.text.split('. ', 1)[1], movie_link])
        
    for elem in ratings[:19]:
        if elem.text != '':
            lst_of_ratings.append(elem.text)
            
    write_to_file(file, lst_of_ratings, lst_of_movies)

title_of_the_page = 'Top 250 Movies - IMDb'
s = Service(r'C:\Users\User\Desktop\automation_things\chromedriver.exe')

chrome_browser = webdriver.Chrome(service=s)
chrome_browser.maximize_window()
chrome_browser.get('https://www.imdb.com/chart/top/')

assert title_of_the_page in chrome_browser.title

select_dropdown = Select(chrome_browser.find_element_by_id('lister-sort-by-options'))

select_dropdown.select_by_index(0)
get_movies(chrome_browser, 'movies_by_ranking.txt')

select_dropdown.select_by_index(1)
get_movies(chrome_browser, 'movies_by_imdb_rating.txt')

select_dropdown.select_by_index(2)
get_movies(chrome_browser, 'movies_by_release_date.txt')

select_dropdown.select_by_index(3)
get_movies(chrome_browser, 'movies_by_number_of_ratings.txt')

select_dropdown.select_by_index(4)
get_movies(chrome_browser, 'movies_by_your_rating.txt')

sleep(5)

chrome_browser.close()