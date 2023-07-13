// import recipeDb from '../../all_recipe_metadata.json';
import sampleDb from '../../sample_db.json';

type Author = {'@type': string, name: string}[];

type Image = {
  '@type': string,
  url: string,
  height?: number
  width?: number
}

type Logo = {
  '@type': string,
  url: string,
  width?: number,
  height?: number,
}

type Publisher = {
  '@type': string, 
  name: string,
  url: string,
  logo?: Logo,
  brand?: string,
  publishingPrinciples: string,
  sameAs?: string[]
}

type Nutrition = {
  '@type': string,
  calories: string,
  carbohydrateContent: string,
  cholestrolContent?: string,
  cholesterolContent?: string,
  fiberContent: string,
  proteinContent: string,
  saturatedFatContent: string,
  sodiumContent: string,
  sugarContent: string, 
  fatContent: string, 
  unsaturatedFatContent: string,
}

type RecipeInstructions = {'@type': string, text: string}[];

// interface Recipe {
//   [K: string]: Recipe[keyof Recipe] | {} 
//   id: number,
//   datePublished: string,
//   dateModified: string,
//   author: Author,
//   description: string,
//   image: Image,
//   publisher: Publisher,
//   publishingPrinciples?: string,
//   name: string,
//   cookTime: string,
//   nutrition: Nutrition,
//   prepTime: string, 
//   recipeCategory: string[],
//   recipeCuisine: string[],
//   recipeIngredient: string[],
//   recipeInstructions: RecipeInstructions,
//   recipeYield: number
// }

interface UnfilteredRecipe {
  [K: string]: UnfilteredRecipe[keyof UnfilteredRecipe]
  '@context'?: string,
  '@type'?: {},
  headline?: string,
  mainEntityOfPage:{},
  id: number,
  datePublished: string,
  dateModified: string,
  author: Author,
  description: string,
  image: Image,
  publisher: Publisher,
  name: string,
  cookTime: string,
  nutrition: Nutrition,
  prepTime: string, 
  recipeCategory: string[],
  recipeCuisine: string[],
  recipeIngredient: string[],
  recipeInstructions: RecipeInstructions,
  recipeYield: string[]
}

type FilteredRecipeData<T> = {
  [K in keyof T as T[K] extends Required<T>[K] ? K : never]: T[K]
}

const getAllRecipes = () => {
  return sampleDb;
}

const filterRecipeProperties = (fetchedObj: UnfilteredRecipe): FilteredRecipeData<UnfilteredRecipe> => {
  const filteredRecipeKeys: Array<keyof FilteredRecipeData<UnfilteredRecipe>> = [
    'id', 
    'datePublished', 
    'dateModified',
    'author',
    'description',
    'image',
    'publisher',
    'publishingPrinciples',
    'name',
    'cookTime',
    'nutrition',
    'prepTime', 
    'recipeCategory',
    'recipeCuisine',
    'recipeIngredient',
    'recipeInstructions',
    'recipeYield'
  ];
  
  const partiallyFilteredRecipe = {} as FilteredRecipeData<UnfilteredRecipe>;
  filteredRecipeKeys.forEach((key) => {
    partiallyFilteredRecipe[key] = fetchedObj[key]
  })

  const filteredPublisher = {} as FilteredRecipeData<Publisher>;
  const filteredPublisherKeys: Array<keyof FilteredRecipeData<Publisher>> = 
    [
      '@type',
      'name',
      'url',
      'publishingPrinciples',
    ];

    filteredPublisherKeys.forEach(key => {
      filteredPublisher[key] = partiallyFilteredRecipe['publisher'][key]
    });

    const filteredRecipe = {
      ...partiallyFilteredRecipe,
      publisher: filteredPublisher
    }
  return filteredRecipe;
}

const filtRec = filterRecipeProperties(sampleDb[0])

export default getAllRecipes;

