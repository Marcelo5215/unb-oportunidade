angular.module('unbOportunidade')
  .directive('registerButton', function($uibModal) {
    return {
      restrict: 'A',
      link: function(scope, element, attr) {

        scope.usuario = {
          email: null,
          password: null
        };

        scope.empresa = {
          cnpj: null,
          razao_social: null,
          nome_fantasia: null,
          conveniada: null,
          usuario_id: null,
          imagem: null
        };

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

              function closeModal() {
                $uibModalInstance.close();
              }

              function submitForm() {

                enterpriseService.createUser(JSON.stringify(scope.usuario), function (reseponse) {

                  console.log(reseponse);

                  // enterpriseService.createEnterprise(scope.empresa, function functionName() {
                  //   console.log('CRIADO');
                  // });

                });

              }

            }
          });
        }

      }
    }
  });
