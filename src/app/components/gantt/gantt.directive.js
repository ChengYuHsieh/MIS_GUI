(function() {
  'use strict';

  angular
    .module('misgui')
    .directive('gantt', gantt);

  /** @ngInject */
  function gantt($http) {
    var directive = {
      restrict: 'E',
      replace: true,
      template: '<div class="amchart"></div>',
      link: link 
    };

    return directive;

    /** @ngInject */
    function link($scope, $el) {
      var id = $el[0].id;

      AmCharts.useUTC = true;
      $http.get('http://gdoggg2032.github.io/haha.json').then(function(res){
        var chart = AmCharts.makeChart( id, {
            "type": "gantt",
            "theme": "light",
            "marginRight": 70,
            "period": "hh",
            "dataDateFormat":"YYYY-MM-DD",
            "balloonDateFormat": "JJ:NN",
            "columnWidth": 0.5,
            "valueAxis": {
                "type": "date",
                "minimum": 7,
                "maximum": 31
            },
            "brightnessStep": 10,
            "graph": {
                "fillAlphas": 1,
                "balloonText": "<b>[[task]]</b>: [[open]] [[value]]"
            },
            "rotate": true,
            "categoryField": "category",
            "segmentsField": "segments",
            "colorField": "color",
            "startDate": "2015-01-01",
            "startField": "start",
            "endField": "end",
            "durationField": "duration",
            "dataProvider": res.data,
            "valueScrollbar": {
                "autoGridCount":true
            },
            "chartCursor": {
                "cursorColor":"#55bb76",
                "valueBalloonsEnabled": false,
                "cursorAlpha": 0,
                "valueLineAlpha":0.5,
                "valueLineBalloonEnabled": true,
                "valueLineEnabled": true,
                "zoomable":false,
                "valueZoomable":true
            },
            "export": {
                "enabled": true
             }
        });
      })
    }
  }

})();

