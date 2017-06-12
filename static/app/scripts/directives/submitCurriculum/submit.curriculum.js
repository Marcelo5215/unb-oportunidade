angular.module('unbOportunidade')
  .directive('curriculumModal', function($uibModal) {
    return {
      restrict: 'A',
      link: function(scope, element, attr) {

        scope.$on('toggleCurriculumModal', function () {
          modalInitialization();
        });

        element.bind('click', function () {
          scope.$broadcast('toggleCurriculumModal');
        });

        function modalInitialization(){
          $uibModal.open({
            templateUrl: 'static/app/scripts/directives/submitCurriculum/submit-form.html',
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
