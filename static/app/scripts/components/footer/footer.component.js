(function () {

  angular.module('unbOportunidade')
    .component('footerComp', {
      templateUrl: 'static/app/scripts/components/footer/footer.html',
      controller: FooterController // Retirar?
    });

  function ExemploController($scope) {
      $scope.textoExemplo = 'opa, tudo bom?';
  }

})();
