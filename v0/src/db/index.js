'use strict';

const Sequelize = require('sequelize');
const env = process.env.ENVIRONMENT || 'local';
const config = require('./databases')[env];
const db = {};

let sequelize = new Sequelize(config.database, config.username, config.password, config);

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;