angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyDetail', {
        url: '/vacancyDetail/:id',
        views: {
          'content@': {
            template:'<vacancy-detail> </vacancy-detail>'
          }
        }
      });

  });
