angular.module('unbOportunidade')
  .directive('loginButton', function($uibModal, $state, $window, store) {
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
                jwtService.auth(user.username, user.password)
                  .then(function successCallback(response) {
                    store.set('token', response.data.token);
                    closeModal();
                    $window.location.reload();
                  });
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
