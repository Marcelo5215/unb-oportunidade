angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyDetail', {
        url: '/vagas/:id/detalhes',
        views: {
          'content@': {
            template:'<vacancy-detail> </vacancy-detail>'
          }
        }
      });

  });
