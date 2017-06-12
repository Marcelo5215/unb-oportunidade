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
            controller: function ($scope, $uibModalInstance, enterpriseService, jwtService, $window, store) {
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

              isUserRegistered();

              function isUserRegistered(){
                if (store.get('token')){
                  $scope.registerUser = false;
                } else {
                  $scope.registerUser = true;
                }
              }

              function closeModal() {
                $uibModalInstance.close();
              }

              function submitForm() {

                enterpriseService.createUser(JSON.stringify($scope.usuario), function (response) {
                  $scope.empresa.usuario = response.data.id;
                  $scope.registerUser = false;
                  login($scope.usuario);


                  // TODO fechar modal de usuario, logar e mostrar o form pra empresa

                  // enterpriseService.createEnterprise(JSON.stringify($scope.empresa), function (response) {
                  //   console.log('CRIADO');
                  //   console.log(response);
                  //   closeModal();
                  // });

                });

              }

              function login(user) {
                jwtService.auth(user.email, user.password)
                  .then(function(response) {
                    store.set('token', response.data.token);
                    var token = store.get('token');
                  });
              }

            }
          });
        }

      }
    }
  });
