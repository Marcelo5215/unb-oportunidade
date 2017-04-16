angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider
      .state('templateHome', {
        url: '/template/home',
        templateUrl: 'static/app/scripts/templates/home.html'
      });

    $stateProvider
      .state('templateListagem', {
        url: '/template/listagem',
        templateUrl: 'static/app/scripts/templates/listagem.html'
      });

    $stateProvider
      .state('templateCarrousel', {
        url: '/template/carrousel',
        templateUrl: 'static/app/scripts/templates/2carrossel.html'
      });

  });
