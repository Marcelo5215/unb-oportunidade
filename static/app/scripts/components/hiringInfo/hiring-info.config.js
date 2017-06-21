angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('hiringInfo', {
        url: '/info-contratacao',
        views: {
          'content@': {
            template: '<hiring-info> </hiring-info>'
          }
        }
      });
  });
