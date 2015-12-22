(function() {
  'use strict';

  angular
    .module('misgui')
    .controller('LineController', ['$http', LineController]);

  /** @ngInject */
  function LineController($http) {
    $http.get("http://localhost:5000/api/database/linechart").then(function(res){
        var data = res.data;
        var chart = c3.generate({
            bindto: '#chart',
            data: {
              columns: data
            }
        });
    });
  }
})();

