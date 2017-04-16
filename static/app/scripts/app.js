angular.module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap'
  ])
  .config(['$httpProvider', '$urlRouterProvider', '$stateProvider', appConfig]);

function appConfig($httpProvider, $urlRouterProvider, $stateProvider) {

  $urlRouterProvider.otherwise('/');

  $stateProvider.state('joao', {
    url: '/joao',
    template: '<span> oi </span>',
    controller: function($scope) {

    }
  });

  $httpProvider.defaults.cache = true;
}
