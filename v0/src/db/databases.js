'use strict';

let databases = {};

let DBConfig = {
  database: 'util',
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  host: process.env.DB_URL,
  dialect: 'postgres',

  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  },

  migrationStorage: 'sequelize',
  migrationStorageTableName: 'sequelize_meta',
  seederStorage: 'sequelize',
  seederStorageTableName: 'sequelize_data'
};

databases.DEV = Object.assign({}, DBConfig);
databases.PROD = Object.assign({}, DBConfig);
databases.local = Object.assign({}, DBConfig);

databases.local.username = 'postgres';
databases.local.password = null;
databases.local.host = 'localhost';

module.exports = databases;
