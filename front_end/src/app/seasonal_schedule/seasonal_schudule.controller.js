(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('SeasonalScheduleController', ['$filter', '$http', 'NgTableParams', SeasonalScheduleController]);

  /** @ngInject */
  function SeasonalScheduleController($filter, $http, NgTableParams) {
    var vm = this;

    $http.get("http://localhost:5000/api/database/seasonal_schedule").then(function(res){
        vm.data = res.data;
        vm.tableParams = new NgTableParams({count: 1, page: 1}, 
            { total: 3, counts: [], getData: function($defer, params){
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
    vm.progress = 50;
    vm.newDailySched = function(){
        vm.isProcessing = true;
    };
  }
})();

