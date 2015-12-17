(function() {
  'use strict';

  angular
    .module('misgui')
    .config(routerConfig);

  /** @ngInject */
  function routerConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'app/main/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })

      .state('database', {
        url: '/database',
        templateUrl: 'app/database/database.html',
        controller: 'DBController',
        controllerAs: 'db'
      })

      .state('scheduling', {
        url: '/scheduling',
        templateUrl: 'app/scheduling/scheduling.html',
        controller: 'SchedulingController',
        controllerAs: 'scheduling'
      })

      .state('gantt', {
        url: '/gantt',
        templateUrl: 'app/gantt/gantt.html',
        controller: 'GanttController',
        controllerAs: 'gantt'
      })

      .state('line', {
        url: '/line',
        templateUrl: 'app/line/line.html',
        controller: 'LineController',
        controllerAs: 'line'
      });

    $urlRouterProvider.otherwise('/');
  }

})();
