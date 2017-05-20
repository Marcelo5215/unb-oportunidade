(function () {

  angular.module('unbOportunidade')
    .config(function($stateProvider) {

      $stateProvider.state('signup', {
          url: '/signup',
          template: '<sign-up> </sign-up>'
        });

    });

})();
