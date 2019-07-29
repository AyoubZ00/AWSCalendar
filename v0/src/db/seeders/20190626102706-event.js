'use strict';

module.exports = {
  up: (queryInterface, Sequelize) => {

    return queryInterface.bulkInsert('event', [{
      id: 1,
      calendar_id: 1,
      recurrence: '0 8 * * mon-fri 2019',
      name: 'Trip 1',
      description: 'Morning Trip',
      duration: 3600,
      createdAt: new Date()
    }, {
      id: 2,
      calendar_id: 1,
      recurrence: '0 14 * * mon-fri 2019',
      name: 'Trip 2',
      description: 'Evening Trip',
      duration: 3600,
      createdAt: new Date()
    }, {
      id: 3,
      calendar_id: 2,
      recurrence: '0 10 * * mon-fri 2019',
      name: 'Trip 3',
      description: 'Late Morning Trip',
      duration: 3600,
      createdAt: new Date()
    }], {});
  },

  down: (queryInterface, Sequelize) => {
    // return queryInterface.bulkDelete('domain', null, {});
  }
};
