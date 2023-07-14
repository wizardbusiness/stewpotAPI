import json;

def extract_recipe_urls(url_data):
  extracted_urls = []
  for url_collection in url_data:
    url_obj_list = url_collection['itemListElement']
    for url_obj in url_obj_list:
      extracted_urls.append(url_obj['url']) 
  return extracted_urls 

def appendRecipeUrl(): 
  recipes = json.load(open('../rawData/allRecipes/all_recipe_metadata.json'))
  url_data = json.load(open('../rawData/allRecipes/recipe_urls.json', 'r'))

  all_recipe_urls = extract_recipe_urls(url_data)

  all_recipes_with_urls = []

  for index, recipe in enumerate(recipes):
    recipe['recipeUrl'] = all_recipe_urls[index]
    all_recipes_with_urls.append(recipe)

  with open('recipes_metadata_with_urls.json', 'w') as recipes_with_urls:
    json.dump(all_recipes_with_urls, recipes_with_urls, indent=2)

def filterAllRecipesData():
  # keys for filtered recipe that will be inserted into database which api connects to.
  key_map = [
    'id', 
    'datePublished', 
    'dateModified',
    'author',
    'description',
    'image',
    'publisher',
    'name',
    'cookTime',
    'nutrition',
    'prepTime', 
    'recipeCategory',
    'recipeCuisine',
    'recipeIngredient',
    'recipeInstructions',
    'recipeYield',
    'aggregateRating',
    'recipeUrl'
  ]
  # unneeded keys which will not be present in filtered recipe
  unused_key_map = [
    '@context',
    '@type',
    'headline',
    'totalTime',
    'mainEntityOfPage',
    'about',
    'video',
    'keywords',
    'numberOfItems',
    'contributor',
    'itemListElement',
    
  ]
  all_expected_keys = key_map + unused_key_map 
  # keys for publisher property
  publisher_key_map = [
    '@type',
    'name',
    'url',
    'publishingPrinciples',
  ]

  data = json.load(open('all_recipes_metadata.json', 'r'))
  filtered_recipes = []
  recipes_with_bad_keys = []
  for recipe in data:
    bad_keys = []
    recipe_with_bad_keys = {'id': recipe['id'], 'bad_keys': bad_keys}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    filtered_recipe = {}
    for key in recipe:
      # filters out non-recipe entries
      if 'recipeInstructions' not in recipe:
        continue
      if key in key_map:
        if key == 'publisher': 
          filtered_recipe[key] = {}     
          for k in publisher_key_map:
            # if k in filtered_recipe[key]:
            filtered_recipe[key][k] = recipe[key][k]
        else:
          filtered_recipe[key] = recipe[key]
      elif key not in all_expected_keys: 
        bad_keys.append(key)
    if len(bad_keys) > 0: 
      recipes_with_bad_keys.append(recipe_with_bad_keys)
    if filtered_recipe:
      filtered_recipes.append(filtered_recipe)
  with open('recipes_with_bad_keys.json', 'w', encoding='utf-8') as recipes_with_bad_keys_json:
    json.dump(recipes_with_bad_keys, recipes_with_bad_keys_json, indent=2)
  with open('./src/database/recipe_db.json', 'w', encoding='utf-8') as filtered_recipe_json:
    json.dump(filtered_recipes, filtered_recipe_json, indent=2)
  return
         
def find_incomplete_ingredient_lists():
  recipes_with_missing_ing = []
  with open('filtered_db.json') as recipeDb_json:
    recipes = json.load(recipeDb_json)
    for recipe in recipes:
        suspect_recipe = {'id': recipe['id']}
        if 'recipeIngredient' in recipe:
          suspect_recipe['recipeIngredient'] = recipe['recipeIngredient']
        if 'name' in recipe:
          suspect_recipe['name'] = recipe['name']
        if 'recipeIngredient' not in recipe or len(recipe['recipeIngredient']) <= 2:  
          suspect_recipe['recipeInstructions'] = recipe['recipeInstructions']
          recipes_with_missing_ing.append(suspect_recipe)
    print(len(recipes_with_missing_ing))
    with open('ingredient_check.json', 'w') as ingredient_check:
      json.dump(recipes_with_missing_ing, ingredient_check, indent=2)
  return

filterAllRecipesData()
# find_incomplete_ingredient_lists()


