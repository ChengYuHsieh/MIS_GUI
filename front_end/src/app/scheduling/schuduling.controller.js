(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('SchedulingController', ['$filter', '$http', 'NgTableParams', '$interval', SchedulingController]);

  /** @ngInject */
  function SchedulingController($filter, $http, NgTableParams, $interval) {
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

    $http.get("/api/database/demand").then(function(res){
        vm.data = res.data;
        var datalen = res.data.length;
        vm.tableParams = new NgTableParams({count: 20, page: 1}, 
            { total: datalen, counts: [], getData: function($defer, params){
            var filteredData = params.filter() ?
                $filter('filter')(vm.data, params.filter()) : vm.data;

            var orderedData = params.sorting() ?
                $filter('orderBy')(filteredData, params.orderBy()) : filteredData;
            var page = orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count());
            $defer.resolve(page);
        }});
    })   
    vm.isProcessing = false;
    vm.newSeasonalSched = function(){
        vm.isProcessing = true;
        vm.progress = 0;
        $interval(function(){if(vm.progress<100)vm.progress+=2}, 1000);
        //$http.post("/api/create/seasonalSchedule").then(function(res){ 
        //})
    }
    vm.progressMax = 100;
    vm.progress = 0;
    vm.closeAlert = function(){
       vm.alerts.splice(0, 1); 
    };
    vm.alerts = [{type: 'success', msg: 'Seasonal Schedule completed!'}];
    

  }
})();

