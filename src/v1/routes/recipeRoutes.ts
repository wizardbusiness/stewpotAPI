import express from 'express';
import { getAllRecipes, getRecipeById } from '../controllers/recipeController';

const recipeRouter = express.Router();

recipeRouter.get('/', getAllRecipes);

recipeRouter.get('/:recipeId', getRecipeById);

export default recipeRouter;

