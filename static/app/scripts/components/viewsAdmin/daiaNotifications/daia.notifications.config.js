angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('virtualQueue', {
        url: '/admin/fila',
        views: {
          'content@' : {
            template: '<virtual-queue></virtual-queue>'
          }
        }
      });

  });
