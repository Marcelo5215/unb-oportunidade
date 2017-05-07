angular.module('unbOportunidade')
  .directive('registerButton', function($uibModal) {
    return {
      restrict: 'A',
      link: function(scope, element, attr) {

        scope.$on('toggleRegisterModal', function () {
          modalInitialization();
        });

        element.bind('click', function () {
          scope.$broadcast('toggleRegisterModal');
        });

        function modalInitialization(){
          $uibModal.open({
            templateUrl: 'static/app/scripts/directives/registerButton/register-modal.html',
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
