import express from 'express';

const v1Router = express.Router();

v1Router.route('/').get((req, res) => {
  res.send(`<h2>Hello from ${req.baseUrl} </h2>`);
});

export default v1Router;