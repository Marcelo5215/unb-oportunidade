(function() {

  angular.module('unbOportunidade')
    .component('enterprisedata', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/adminConfig/financialdata.html',
      controller: FinancialController
    });

  function FinancialController($scope) {
    $scope.pj_id = 1;
    $scope.pf_id = 2;

  }



})();
