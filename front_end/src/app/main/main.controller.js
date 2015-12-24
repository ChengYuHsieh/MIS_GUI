(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController() {
    var vm = this;
    vm.myInterval = 5000;
    vm.slides = [
        {image: 'assets/images/airplane.png'},
        {image: 'assets/images/airplane1.png'},
        {image: 'assets/images/airplane2.png'}
    ]

  }
})();
