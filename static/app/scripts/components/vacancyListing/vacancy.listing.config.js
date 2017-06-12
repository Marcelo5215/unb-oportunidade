angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyListing', {
      url: '/listagem',
      views: {
        'content@': {
          template: '<vacancy-listing> </vacancy-listing>'
        }
      }
    });

  });
