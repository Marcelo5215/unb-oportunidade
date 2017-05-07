angular.module('unbOportunidade')
  .directive('loginButton', function($uibModal) {
    return {
      restrict: 'A',
      link: function(scope, element, attr) {

        scope.$on('toggleLoginModal', function () {
          modalInitialization();
        });

        element.bind('click', function () {
          console.log('entrei');
          scope.$broadcast('toggleLoginModal');
        });

        function modalInitialization(){
          $uibModal.open({
            templateUrl: 'static/app/scripts/directives/loginButton/login-modal.html',
            controller: function ($scope, $uibModalInstance) {
              $scope.closeModal = closeModal;

              function closeModal() {
                $uibModalInstance.close();
              }
            }
          });
        }

      }
    }
  });
