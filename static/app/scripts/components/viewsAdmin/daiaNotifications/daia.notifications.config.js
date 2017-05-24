angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('virtualQueue', {
        url: '/admin/queue',
        views: {
          'content@' : {
            template: '<virtual-queue></virtual-queue>'
          }
        }
      });

  });
