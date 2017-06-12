angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('candidateList', {
        url: '/admin/candidatos',
        views: {
          'content@' : {
            template: '<candidate-list><candidate-list>'
          }
        }
      });

    $stateProvider
      .state('vacancyList', {
        url: '/admin/vagas',
        views: {
          'content@' : {
            template: '<vacancy-list><vacancy-list>'
          }
        }
      });

  });
