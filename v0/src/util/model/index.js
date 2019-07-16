'use strict';

const fs = require('fs');
const path = require('path');
const basename = path.basename(__filename);

const db = require('../../db');

const models = {
  Sequelize: db.Sequelize
};

fs
  .readdirSync(__dirname)
  .filter(file => {
    return (file.indexOf('.') !== 0) && (file !== basename) && (file.slice(-3) === '.js');
  })
  .forEach(file => {
    const model = db.sequelize['import'](path.join(__dirname, file));
    models[model.name] = model;
  });

Object.keys(models).forEach(modelName => {
  if (models[modelName].associate) {
    models[modelName].associate(db);
  }
});

module.exports = models;
