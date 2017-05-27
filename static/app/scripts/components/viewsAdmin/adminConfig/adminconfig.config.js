angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('enterpriseData', {
        url: '/admin/enterprise',
        views: {
          'content@' : {
            template: '<enterprise-data></enterprise-data>'
          }
        }
      });

  });
