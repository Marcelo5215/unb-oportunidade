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
      .state('templateListaAlunos', {
        url: '/template/lista-alunos',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/lista-alunos.html',
            controller: 'controllerTemp'
          }
        }
      });

    $stateProvider
      .state('templateLogin', {
        url: '/template/login',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/login.html',
            controller: 'controllerTemp'
          }
        }
      });

    $stateProvider
      .state('templateCurriculo', {
        url: '/template/curriculo',
        views: {
          'content@': {
            templateUrl: 'static/app/scripts/templates/curriculo.html',
          }
        }
      });

  });
