angular.module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap'
  ])
  .config(['$httpProvider', '$urlRouterProvider', '$stateProvider', appConfig]);

function appConfig($httpProvider, $urlRouterProvider, $stateProvider) {

  $urlRouterProvider.otherwise('/');
  $stateProvider
    .state('home', {
      url: '/',
      views: {
        '@content': {
            templateUrl: 'static/app/scripts/index.html'
        }
      }
    })

  $httpProvider.defaults.cache = true;
}
