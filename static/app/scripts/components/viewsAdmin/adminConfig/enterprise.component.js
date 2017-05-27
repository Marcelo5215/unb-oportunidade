(function() {

  angular.module('unbOportunidade')
    .component('enterpriseData', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/adminConfig/enterprisedata.html',
      controller: EnterpriseController
    });

  function EnterpriseController($scope) {
    console.log('opa');
    $scope.name = 'Nome da Empresa';
    $scope.corpname = 'Nome corporativo da empresa';
    $scope.cnpj = 'CNPJ da empresa'
    $scope.biography = "Escreva a Biografia"
    $scope.data = {
      areas: { // Should get this from API
        availabeAreas: [{
            id: '1',
            name: 'Selecione uma Área'
          },
          {
            id: '2',
            name: 'Admnistração'
          },
          {
            id: '3',
            name: 'Biblioteconomia'
          },
          {
            id: '4',
            name: 'Ciência da Computação'
          }
        ],
        selectedArea: {
          id: '1',
          name: 'Selecione uma Área'
        } //This sets the default value of the select in the ui
      }
    }

    $scope.data.interest_areas = { // Should get this from API
      availabeAreas: [{
          id: '1',
          name: 'Selecione uma Área'
        },
        {
          id: '2',
          name: 'Admnistração'
        },
        {
          id: '3',
          name: 'Computação'
        },
        {
          id: '4',
          name: 'Biologia'
        },
        {
          id: '5',
          name: 'Educação Física'
        }
      ],
      selectedArea: {
        id: '1',
        name: 'Selecione uma Área'
      } //This sets the default value of the select in the ui
    };

  }

})();
