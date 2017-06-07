(function () {

  angular.module('unbOportunidade')
    .component('navbar', {
      templateUrl: 'static/app/scripts/components/navbar/navbar.html',
      controller: NavbarController
    });

  function NavbarController($scope, $state, store, jwtService) {

    $scope.isUserLoggedIn = isUserLoggedIn;

    function getCurrentToken() {
      return store.get('token');
    }

    function isUserLoggedIn() {
      var currentToken = getCurrentToken();
      if (currentToken) {
        jwtService.verifyAuth(currentToken).then(function() {
          return true;
        });
      }
      return false;
    }

  }
})();
