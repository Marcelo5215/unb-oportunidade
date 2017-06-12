angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyDetail', {
        url: '/vaga/:id/detalhes',
        views: {
          'content@': {
            template:'<vacancy-detail> </vacancy-detail>'
          }
        }
      });

  });
