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
        controllerAs: 'vm'
      })

      //.state('database', {
        //url: '/database',
        //templateUrl: 'app/database/database.html',
        //controller: 'DatabaseController',
        //controllerAs: 'vm'
      //})

      .state('scheduling', {
        url: '/scheduling',
        templateUrl: 'app/scheduling/scheduling.html',
        controller: 'SchedulingController',
        controllerAs: 'vm'
      })

      .state('seasonal_schedule', {
        url: '/seasonal_schedule',
        templateUrl: 'app/seasonal_schedule/seasonal_schedule.html',
        controller: 'SeasonalScheduleController',
        controllerAs: 'vm'
      })

      .state('gantt', {
        url: '/gantt',
        templateUrl: 'app/gantt/gantt.html',
        controller: 'GanttController',
        controllerAs: 'vm'
      })

      .state('line', {
        url: '/line',
        templateUrl: 'app/line/line.html',
        controller: 'LineController',
        controllerAs: 'vm'
      });

    $urlRouterProvider.otherwise('/');
  }

})();
