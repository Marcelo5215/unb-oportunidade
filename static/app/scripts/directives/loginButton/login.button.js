angular.module('unbOportunidade')
  .directive('loginButton', function($uibModal) {
    return {
      restrict: 'A',
      link: function(scope, element, attr) {

        scope.$on('toggleLoginModal', function () {
          modalInitialization();
        });

        element.bind('click', function () {
          scope.$broadcast('toggleLoginModal');
        });

        function modalInitialization(){
          $uibModal.open({
            templateUrl: 'static/app/scripts/directives/loginButton/login-modal.html',
            controller: function ($scope, $uibModalInstance, jwtService) {
              $scope.user = new User();

              $scope.login = login;
              $scope.closeModal = closeModal;

              function login(user) {
                jwtService.auth(user.username, user.password);
              }

              function closeModal() {
                $uibModalInstance.close();
              }

              function User() {
                this.username = null;
                this.password = null;
              }
            }
          });
        }

      }
    }
  });
