import express, {Request, Response, NextFunction} from 'express';


const app = express();

const PORT: number | string = process.env.PORT || 3000;

app.get('/', (req: Request, res: Response) => {
  res.send("<h2>It's working!</h2>")
});

app.listen(PORT, () => {
  console.log(`'API listening on port ${PORT}`);
});