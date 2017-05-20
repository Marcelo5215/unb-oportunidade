(function () {

  angular.module('unbOportunidade')
    .component('navbar', {
      templateUrl: 'static/app/scripts/components/navbar/navbar.html',
      controller: NavbarController
    });

  function NavbarController($scope, $state) {

    $scope.login = login;
    $scope.register = register;

    function login() {
      // $state.go('login');
    }

    function register() {
      // $state.go('register');
    }

    function home() {
      $state.go('home');
    }

  }


})();
