angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider
      .state('templateHome', {
        url: '/template/home',
        views: {
          'content@': {
              templateUrl: 'static/app/scripts/templates/home.html'
          }
        }
      });

    $stateProvider
      .state('templateListagem', {
        url: '/template/listagem',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/listagem.html'
          }
        }
      });

    $stateProvider
      .state('templateCarrousel', {
        url: '/template/carrousel',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/2carrossel.html'
          }
        }
      });

  });
