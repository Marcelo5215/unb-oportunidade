angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('enterpriseData', {
        url: '/admin/empresa',
        views: {
          'content@' : {
            template: '<enterprise-data></enterprise-data>'
          }
        }
      });

    $stateProvider
      .state('financialData', {
        url: '/admin/financeiro',
        views: {
          'content@' : {
            template: '<financial-data></financial-data>'
          }
        }
      });

  });
