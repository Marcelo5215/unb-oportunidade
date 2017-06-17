angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyListing', {
      url: '/vagas',
      views: {
        'content@': {
          template: '<vacancy-listing> </vacancy-listing>'
        }
      }
    });

  });
