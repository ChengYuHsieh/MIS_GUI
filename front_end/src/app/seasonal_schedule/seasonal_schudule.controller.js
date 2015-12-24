(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('SeasonalScheduleController', ['$filter', '$http', 'NgTableParams', '$interval', SeasonalScheduleController]);

  /** @ngInject */
  function SeasonalScheduleController($filter, $http, NgTableParams, $interval) {
    var vm = this;

    $http.get("/api/database/seasonal_schedule").then(function(res){
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
    vm.progressMax = 100;
    vm.progress = 0;
    vm.newDailySched = function(){
        vm.progress = 0;
        vm.isProcessing = true;
        var stop = $interval(function(){
            if(vm.progress<100){
                vm.progress+=20
            }
        }, 1000);
    };
    vm.closeAlert = function(){
       vm.alerts.splice(0, 1); 
    };
    vm.alerts = [{type: 'success', msg: 'Daily Schedule completed!'}];
  }
})();

