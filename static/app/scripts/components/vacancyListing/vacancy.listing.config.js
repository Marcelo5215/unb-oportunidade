(function () {

  angular.module('unbOportunidade')
    .config(function($stateProvider) {

      $stateProvider.state('vacancyListing', {
          url: '/listagem',
          template: '<vacancy-listing> </vacancy-listing>'
        });

    });

})();
