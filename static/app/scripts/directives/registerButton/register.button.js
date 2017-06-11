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
            controller: function ($scope, $uibModalInstance, enterpriseService) {
              $scope.closeModal = closeModal;
              $scope.submitForm = submitForm;

              $scope.usuario = {
                email: null,
                password: null,
                confirm_password: null
              };

              $scope.empresa = {
                cnpj: null,
                razao_social: null,
                nome_fantasia: null,
                conveniada: false,
                imagem: 'exemplo.png',
                usuario: null
              };


              function closeModal() {
                $uibModalInstance.close();
              }

              function submitForm() {

                enterpriseService.createUser(JSON.stringify($scope.usuario), function (response) {

                  $scope.empresa.usuario = response.data.id;
                  console.log($scope.empresa.usuario);

                  enterpriseService.createEnterprise(JSON.stringify($scope.empresa), function (response) {
                    console.log('CRIADO');
                    console.log(response);
                    closeModal();
                  });

                });

              }

            }
          });
        }

      }
    }
  });
