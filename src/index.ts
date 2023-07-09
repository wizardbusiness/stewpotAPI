import express, {Request, Response, NextFunction} from 'express';
import v1Router from './v1/routes';

const app = express();

const PORT: number | string = process.env.PORT || 3000;

app.use('/api/v1', v1Router)

app.listen(PORT, () => {
  console.log(`'API listening on port ${PORT}`);
});