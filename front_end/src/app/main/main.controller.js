(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController() {
    var vm = this;
    vm.slides = [
        {image: 'assets/images/angular.png'},
        {image: 'assets/images/bootstrap.png'}
    ]

  }
})();
