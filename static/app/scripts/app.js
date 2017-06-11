angular.module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap',
    'angular-storage',
    'angular-jwt',
    'ngCookies'
  ])
  .run(function run($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
  })
  .config(
    ['$httpProvider', '$urlRouterProvider', '$stateProvider',
      'jwtInterceptorProvider', appConfig
    ]);

function appConfig(
  $httpProvider, $urlRouterProvider, $stateProvider, jwtInterceptorProvider) {

  $urlRouterProvider.otherwise('/');

  $stateProvider
    .state('home', {
      url: '/',
      views: {
        'content@': {
          templateUrl: 'static/app/scripts/index.html'
        }
      }
    });

  jwtInterceptorProvider.tokenGetter = function(store) {
    return store.get('token');
  }

  $httpProvider.interceptors.push('jwtInterceptor');

  $httpProvider.defaults.cache = true;
}
