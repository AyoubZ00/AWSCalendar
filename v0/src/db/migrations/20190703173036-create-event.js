'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('event', {
      id: {
        allowNull: false,
        primaryKey: true,
        type: Sequelize.UUID
      },calendarId: {
        allowNull: false,
        type: Sequelize.UUID,
        field: 'calendar_id'
      },
      recurrence: {
        type: Sequelize.STRING
      },
      name: {
        type: Sequelize.STRING
      },
      description: {
        type: Sequelize.STRING       
      },
      duration: {
        type: Sequelize.INTEGER
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: true,
        type: Sequelize.DATE
      }
    });
  },
  down: (queryInterface, Sequelize) => {
    return queryInterface.dropTable('event');
  }
};