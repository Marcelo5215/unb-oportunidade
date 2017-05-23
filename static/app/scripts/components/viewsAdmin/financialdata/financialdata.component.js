(function() {

  angular.module('unbOportunidade')
    .component('enterprisedata', {
      templateUrl: 'static/app/scripts/components/adminconfig/financialdata/financialdata.html',
      controller: FinancialController
    });

  .controller("FinancialController", ["$scope", function($scope) {
    $scope.pj_id = 1;
    $scope.pf_id = 2;

  }]);

})();
