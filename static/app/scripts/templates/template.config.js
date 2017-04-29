angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider
      .state('templateHome', {
        url: '/template/home',
        views: {
          'content@': {
              templateUrl: 'static/app/scripts/templates/home.html',
              controller: 'controllerTemp'
          }
        }
      });

    $stateProvider
      .state('templateListagem', {
        url: '/template/listagem',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/listagem.html',
            controller: 'controllerTemp'
          }
        }
      });

    $stateProvider
      .state('templateCarrousel', {
        url: '/template/carrousel',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/2carrossel.html',
            controller: 'controllerTemp'
          }
        }
      });

    $stateProvider
      .state('loginTeste', {
        url: '/template/login',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/login-teste.html',
            controller: 'controllerTemp'
          }
        }
      });

  });
