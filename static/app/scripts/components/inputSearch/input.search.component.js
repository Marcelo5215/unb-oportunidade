(function () {

  angular.module('unbOportunidade')
    .component('inputSearch', {
      templateUrl: 'static/app/scripts/components/inputSearch/input-search.html',
      controller: InputSearchController
    });

  function InputSearchController($scope, $state) {

    $scope.search = function() {
      $state.go('vacancyListing');
    }

    $scope.cursos = {
      curso1: {
        nome: 'Ciência da Computção',
        sigla: 'CIC'
      },
      curso2: {
        nome: 'Psicologia',
        sigla: 'PSI'
      },
      curso3: {
        nome: 'Engenharia da Computação',
        sigla: 'ENC'
      }
    }

  }


})();
