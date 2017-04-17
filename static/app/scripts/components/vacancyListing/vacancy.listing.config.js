(function () {

  angular.module('unbOportunidade')
    .config(function($stateProvider) {

      $stateProvider.state('vacancyListing', {
          url: '/listagem', /* Temporary URL just for simplicity */
          template: '<vacancy-listing> </vacancy-listing>'
        });

    });

})();
