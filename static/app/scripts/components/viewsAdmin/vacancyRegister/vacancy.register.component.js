(function() {

  angular.module('unbOportunidade')
    .component('vacancyRegister', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/vacancyRegister/vacancy-register.html',
      controller: VacancyRegisterController
    });

  function VacancyRegisterController($scope, $state) {

    $scope.voltar = voltar;

    function voltar() {
      $state.go('vacancyList');
    }

  }

})();
