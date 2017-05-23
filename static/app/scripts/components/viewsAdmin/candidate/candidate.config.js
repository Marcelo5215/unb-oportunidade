angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('candidateList', {
        url: '/admin/candidates',
        views: {
          'content@' : {
            template: '<candidate-list><candidate-list>'
          }
        }
      });

    $stateProvider
      .state('vacancyList', {
        url: '/admin/vagancies',
        views: {
          'content@' : {
            template: '<vacancy-list><vacancy-list>'
          }
        }
      });

  });
