(function() {

  angular.module('unbOportunidade')
    .component('financialData', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/adminConfig/financialdata.html',
      controller: FinancialDataController
    });

  function FinancialDataController($scope, $state) {
    $scope.pj_id = 1;
    $scope.pf_id = 2;

    $scope.financialDataState = financialDataState;
    $scope.virtualQueueState = virtualQueueState;
    $scope.candidateListState = candidateListState;
    $scope.vacancyListState = vacancyListState;
    $scope.enterpriseDataState = enterpriseDataState;

    function financialDataState() {
        $state.go('financialData');
    }

    function virtualQueueState() {
      $state.go('virtualQueue');
    }

    function candidateListState() {
      $state.go('candidateList');
    }

    function vacancyListState() {
      $state.go('vacancyList');
    }

    function enterpriseDataState() {
      $state.go('enterpriseData');
    }

  }



})();
