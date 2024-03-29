'use strict';

const fs = require('fs');
const path = require('path');
const basename = path.basename(__filename);

const services = {};

fs
  .readdirSync(__dirname)
  .filter(file => {
    return (file.indexOf('.') !== 0) && (file !== basename) && (file.slice(-3) === '.js');
  })
  .forEach(file => {
    let serviceName = file.slice(0, file.length - 3);

    const service = require(path.join(__dirname, serviceName));
    services[serviceName] = service;
  });

module.exports = services;