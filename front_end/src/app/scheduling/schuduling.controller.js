(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('SchedulingController', ['NgTableParams', SchedulingController]);

  /** @ngInject */
  function SchedulingController(NgTableParams) {
    var vm = this;
    vm.weeks = [
    {
        num: 1, 
        sel: false
    },
    {
        num: 2, 
        sel: false
    },
    {
        num: 3, 
        sel: false
    },
    {
        num: 4, 
        sel: false
    },
    {
        num: 5, 
        sel: false
    },
    {
        num: 6, 
        sel: false
    },
    {
        num: 7, 
        sel: false
    },
    {
        num: 8, 
        sel: false
    },
    {
        num: 9, 
        sel: false
    },
    {
        num: 10, 
        sel: false
    },
    {
        num: 11, 
        sel: false
    },
    {
        num: 12, 
        sel: false
    }
    ];
    vm.allWeeks = false;
    vm.checkAllWeeks = function(){
        vm.allWeeks = !vm.allWeeks;
        angular.forEach(vm.weeks, function (week) {
            week.sel = vm.allWeeks;
        });
    }


    vm.data = [{name: "Moroni", age: 50} /*,*/];
    vm.tableParams = new NgTableParams({}, { dataset: vm.data});
  }
})();

