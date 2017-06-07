angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider.state('vacancyListing', {
      url: '/listing',
      views: {
        'content@': {
          template: '<vacancy-listing> </vacancy-listing>'
        }
      }
    });

  });
