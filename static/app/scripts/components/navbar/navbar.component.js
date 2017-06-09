(function () {

  angular.module('unbOportunidade')
    .component('navbar', {
      templateUrl: 'static/app/scripts/components/navbar/navbar.html',
      controller: NavbarController
    });

  function NavbarController($scope, $state, store, jwtService) {

    $scope.isUserLoggedIn = false;
    $scope.logout = logout;

    this.$onInit = function(){
      jwtService.verifyAuth(getCurrentToken()).then(login, logout);
    };

    function login() {
      $scope.isUserLoggedIn = true;
    }

    function logout() {
      store.set('token', null);
      $scope.isUserLoggedIn = false;
    }

    function getCurrentToken() {
      return store.get('token');
    }
  }
})();
