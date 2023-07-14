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