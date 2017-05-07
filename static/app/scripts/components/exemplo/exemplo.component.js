(function () {

  angular.module('unbOportunidade')
    .component('exemploComp', {
      templateUrl: 'static/app/scripts/components/exemplo/exemplo.html',
      controller: ExemploController
    });

  function ExemploController($scope) {
      $scope.textoExemplo = 'opa, tudo bom?';
  }

})();
