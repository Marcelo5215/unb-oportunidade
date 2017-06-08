(function() {

  angular.module('unbOportunidade')
    .component('vacancyList', {
      templateUrl: 'static/app/scripts/components/viewsAdmin/candidate/vacancyList.html',
      controller: VacancyListController
    });

    function VacancyListController($scope, $state) {

      /* Atenção, isso está do jeito que está, pois foi tudo desenvolvido com muita pressa (LP),
        então se der pra arrumar, arrume!
      */

      $scope.financialDataState = financialDataState;
      $scope.virtualQueueState = virtualQueueState;
      $scope.candidateListState = candidateListState;
      $scope.vacancyListState = vacancyListState;
      $scope.enterpriseDataState = enterpriseDataState;

      function financialDataState() {
          $state.go('financialData');
      }

      function virtualQueueState() {
        $state.go('virtualQueue');
      }

      function candidateListState() {
        $state.go('candidateList');
      }

      function vacancyListState() {
        $state.go('vacancyList');
      }

      function enterpriseDataState() {
        $state.go('enterpriseData');
      }

      $scope.student = {
        firstName: "",
        lastName: "",

        subjects: [{
            curso: 'Ciência da Computação',
            matriculo: '14/0071989',
            time: 30,
            turno: 'Matutino'
          },
          {
            curso: 'Administração',
            matriculo: '17/0019384',
            time: 20,
            turno: 'Noturno'
          },
          {
            curso: 'Artes Cênicas',
            matriculo: '14/0098374',
            time: 30,
            turno: 'Noturno'
          },
          {
            curso: 'Gestão Publica',
            matriculo: '13/0000666',
            time: 20,
            turno: 'Vespertino'
          }

        ],

        fullName: function() {
          var studentObject;
          studentObject = $scope.student;
          return studentObject.firstName + " " + studentObject.lastName;
        }
      };

      $scope.vagas = {
        vaga: "",
        area: "",
        value: "",
        time: "",
        shift: "",

        management: [{
            vaga: 'Assistente de gerente',
            area: 'Administração',
            value: 1000.00,
            time: 30,
            shift: 'Matutino'
          },
          {
            vaga: 'Programador',
            area: 'Ciência da Computação',
            value: 800.00,
            time: 20,
            shift: 'Noturno'
          },
          {
            vaga: 'Tecnico de farmacos',
            area: 'Biotecnologia',
            value: 1000.00,
            time: 30,
            shift: 'Noturno'
          },
          {
            vaga: 'Gestão de Pol. Publicas',
            area: 'Gestão Publica',
            value: 800.00,
            time: 20,
            shift: 'Vespertino'
          }
        ]

      };

      $scope.line = {
        line_position: [{
            position: 1
          },
          {
            position: 2
          },
          {
            position: 3
          },
          {
            position: 4
          }
        ]
      };
    }

})();