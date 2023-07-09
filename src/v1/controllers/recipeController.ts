import {Request, Response, NextFunction} from 'express';

export const getAllRecipes = (req: Request, res: Response) => {
  res.send("Get all recipes")
};

export const getRecipeById = (req: Request, res: Response) => {
  res.send("get a recipe by id");
};

