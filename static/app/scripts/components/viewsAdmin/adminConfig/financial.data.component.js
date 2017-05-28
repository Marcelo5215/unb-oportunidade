(function() {

  angular.module('unbOportunidade')
    .component('financialData', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/adminConfig/financialdata.html',
      controller: FinancialDataController
    });

  function FinancialDataController($scope) {
    $scope.pj_id = 1;
    $scope.pf_id = 2;

  }



})();
