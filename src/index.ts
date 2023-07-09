import express, {Request, Response, NextFunction} from 'express';
import recipeRoutes from './v1/routes/recipeRoutes';

const app = express();

const PORT: number | string = process.env.PORT || 3000;

app.use('/api/recipes', recipeRoutes)

app.listen(PORT, () => {
  console.log(`'API listening on port ${PORT}`);
});