angular.module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap',
    'angular-storage',
    'angular-jwt'
  ])
  .config(
    ['$httpProvider', '$urlRouterProvider', '$stateProvider',
    'jwtInterceptorProvider', appConfig]);

function appConfig(
  $httpProvider, $urlRouterProvider, $stateProvider, jwtInterceptorProvider) {

  $urlRouterProvider.otherwise('/');

  jwtInterceptorProvider.tokenGetter = function (store) {
    return store.get('token');
  }

  $httpProvider.interceptors.push('jwtInterceptor');

  $httpProvider.defaults.cache = true;
}
