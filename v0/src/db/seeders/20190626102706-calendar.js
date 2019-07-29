'use strict';

module.exports = {
  up: (queryInterface, Sequelize) => {

    return queryInterface.bulkInsert('calendar', [{
      id: 1,
      name: 'Calendar 1',
      description: 'First Calendar',
      createdAt: new Date()
    },{
        id: 2,
        name: 'Calendar 2',
        description: 'Second Calendar',
        createdAt: new Date()
      },{
        id: 3,
        name: 'Calendar 3',
        description: 'Third Calendar',
        createdAt: new Date()
      }], {});
  },

  down: (queryInterface, Sequelize) => {
    // return queryInterface.bulkDelete('domain', null, {});
  }
};
