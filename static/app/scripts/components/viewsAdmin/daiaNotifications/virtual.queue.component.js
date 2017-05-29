(function() {

  angular.module('unbOportunidade')
    .component('virtualQueue', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/daiaNotifications/virtualQueue.html',
      controller: VirtualQueueController
    });

  function VirtualQueueController($scope, $state) {

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
