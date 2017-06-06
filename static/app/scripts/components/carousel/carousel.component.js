(function () {

  angular.module('unbOportunidade')
    .component('carousel', {
      templateUrl: 'static/app/scripts/components/carousel/carousel.html',
      controller: CarouselController
    });

  function CarouselController($scope, $state) {

    $scope.empresas = {
      empresa1: {
        cnpj: null,
        razao_social: 'Universidade de Brasilia',
        nome_fatansia: 'UnB',
        conveniada: true,
        usuario: null,
        imagem: null
      },
      empresa2: {
        cnpj: null,
        razao_social: 'Universidade de Brasilia',
        nome_fatansia: 'UnB',
        conveniada: true,
        usuario: null,
        imagem: null
      },
      empresa3: {
        cnpj: null,
        razao_social: 'Universidade de Brasilia',
        nome_fatansia: 'UnB',
        conveniada: true,
        usuario: null,
        imagem: null
      }

    }

  }


})();
