(function() {

  angular.module('unbOportunidade')
    .component('virtualQueue', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/daiaNotifications/virtualQueue.html',
      controller: VirtualQueueController
    });

  function VirtualQueueController($scope, $state) {

    /* Atenção, isso está do jeito que está, pois foi tudo desenvolvido com muita pressa (LP),
      então se der pra arrumar, arrume!
    */

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
