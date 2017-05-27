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

    // $stateProvider
    //   .state('financialData', {
    //     url: '/admin/financial',
    //     views: {
    //       'content@' : {
    //         template: '<enterprise-data></enterprise-data>'
    //       }
    //     }
    //   });

  });
