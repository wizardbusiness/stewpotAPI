import {Request, Response, NextFunction} from 'express';
import { getAllRecipesService, getRecipeByIdService } from '../services/recipeService'

export const getAllRecipes = (req: Request, res: Response) => {
  const allRecipes = getAllRecipesService();
  res.send({status: 200, data: allRecipes});
};

export const getRecipeById = (req: Request, res: Response) => {
  const recipeById = getRecipeByIdService();
  res.send("get a recipe by id");
};

