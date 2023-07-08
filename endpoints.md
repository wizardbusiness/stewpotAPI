*********
security 
ssl
protocol: https://
*********
*********
api
route: api.stewpot.com
*********
*********
recipes
route: /recipes
filter by attributes
categories -
  *meal*
  - breakfast
  - lunch
  - dinner
  - snacks
  - dessert
  *diet*
  - vegetarian
  - vegan
  - lacto-vegetarian
  - keto
  - pescatarian
  - lactose-free
  - low-fat
  - raw
  - gluten-free
  *allergies*
  - nut / tree nut
    -- peanut
    -- other nuts
  - lactose
  - egg 
  - shellfish
  - soy
  - fish
  -- user selected other
  *appliances*
  - oven
  - stovetop
  - toaster over
  - air fryer
  - toaster
  - instant pot
  - slow cooker
  *convenience*
  - one pot
  - quick
  - easy prep
route: /category?meal=string&diet=string&allergies=string1+string2
*********
*********
filter by number of results
route: &results=# // return highest rated first
*********
*********
filter by rating
route: ?rating=# // and up
*********
*********
get all recipes by ingredients
/ingredients=a+amount,b+amount,c+amount,d+amount
sort by percent ingredients user has
?sortmethod=1
sort by total ingredients used
?sortmethod=2
*********
*********
api key
route: /key=# // unique identifier
