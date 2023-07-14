import requests
from bs4 import BeautifulSoup
import json
import time
import random

recipeId = 1

def sleep(): 
  time.sleep(random.randint(0, 3))
  return None

def get_recipe_metadata(url):
  global recipeId
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  head_tag = soup.find('head')
  script_tag = head_tag.find('script', {'class': 'comp allrecipes-schema mntl-schema-unified', 'id': 'allrecipes-schema_1-0'})
  if not script_tag: return None
  script_data = script_tag.string
  metadata = json.loads(script_data)[0]
  metadata_sans_reviews = {k: v for k, v in metadata.items() if k != 'review'}
  metadata_sans_reviews['id'] = recipeId
  recipeId += 1
  return metadata_sans_reviews

def scrape_category(url): 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    category_urls = []
    list_group = soup.find('div', {'class': 'comp tax-sc__recirc-list card-list mntl-document-card-list mntl-card-list mntl-block'})
    if not list_group: return None
    recipe_list = list_group.find_all('a', href=True)
    if not recipe_list: return None
    for recipe in recipe_list: 
        sleep()
        recipe_link = recipe['href']
        if not recipe_link: return None
        category_urls.append(recipe_link) 
    return category_urls

def scrape_all_categories():
    base_url = 'https://www.allrecipes.com/recipes-a-z-6735880'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_recipe_urls = []
    all_recipe_metadata = []
    group_lists = soup.find('div', {'class': 'comp alphabetical-list mntl-block'})
    list_groups = group_lists.find_all('div', { 'class': 'alphabetical-list__group' })
    for group in list_groups: 
        list = group.find('ul', {'class': 'loc link-list'})
        list_items = list.find_all('li')
        sleep()
        for item in list_items: 
            url_for_category = item.find('a', href=True)['href']
            category_urls = scrape_category(url_for_category)
            all_recipe_urls = [*all_recipe_urls, category_urls]
            sleep()
    for recipe_url in all_recipe_urls: 
        #  metadata not including reviews
        metadata = get_recipe_metadata(recipe_url)
        all_recipe_metadata.append(metadata)
    with open('all_recipe_metadata.json', 'w', encoding='utf-8') as file:
        json.dump(all_recipe_metadata, file, indent=2)
    sleep()
    return

# scrape_all_categories()

def get_all_recipes_metadata():
  all_recipes_metadata = []
  with open('recipe_urls.json') as json_file:
    metadata = json.load(json_file)
    for data in metadata:
       url_list = data['itemListElement']
       for list_item in url_list:
          url = list_item['url']
          recipe_metadata = get_recipe_metadata(url) 
          all_recipes_metadata.append(recipe_metadata)
          print(recipe_metadata)
          sleep()

  with open('all_recipe_metadata.json', 'w', encoding='utf-8') as file:
        json.dump(all_recipes_metadata, file, indent=2)
  return 

# get_all_recipes_metadata()
     
    

    
        
        


