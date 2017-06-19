angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyListing', {
      url: '/vagas',
      params: {
        curso: null
      },
      views: {
        'content@': {
          template: '<vacancy-listing> </vacancy-listing>'
        }
      }
    });

  });
