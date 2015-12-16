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

      .state('gantt', {
        url: '/gantt',
        templateUrl: 'app/gantt/gantt.html',
        controller: 'GanttController',
        controllerAs: 'gantt'
      });

    $urlRouterProvider.otherwise('/');
  }

})();
