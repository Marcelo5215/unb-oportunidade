angular.module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap'
  ])
  .config(['$httpProvider', '$urlRouterProvider', '$stateProvider', appConfig]);

function appConfig($httpProvider, $urlRouterProvider, $stateProvider) {

  $urlRouterProvider.otherwise('/');

  $httpProvider.defaults.cache = true;
}
