angular.module('unbOportunidade')
  .config(function ($stateProvider) {

    $stateProvider
      .state('vacancyRegister', {
        url: '/admin/vagas/cadastro',
        views: {
          'content@' : {
            template: '<vacancy-register></vacancy-register>'
          }
        }
      });

  });
