(function () {

  angular.module('unbOportunidade')
    .component('vacancyListing', {
      templateUrl: 'static/app/scripts/components/vacancyListing/vacancy.listing.html',
      controller: VacancyListingController
    });

  function VacancyListingController($scope, $state) {
    $scope.vacancies = [];
    $scope.areas = [];
    $scope.getVacancies = getVacancies;
    $scope.getAreas = getAreas;
    $scope.vacancyDetail = vacancyDetail;


    function getVacancies() {
      $scope.vacancies = apiCallToGetVacancies();
    }

    function getAreas() {
      $scope.areas = apiCallToGetAreas();
    }

    function vacancyDetail(id) {
      $state.go('vacancyDetail', { id: id });
    }

    /* This will be retrieved from an api */
    function apiCallToGetVacancies() {
      return [
        {
          course: "Administração",
          date: "22/03/2017",
          numVacancies: 1,
          localization: "TAGUATINGA",
          semester: "4º ao 6º",
          payment: "R$ 800,00 + benefícios",
          period: "08:00 às 12:00 / 14:00 às 16:00",
          requirements: "Carteira de Habilitação, Windows, Word Excel e Intenet."
        },
        {
          course: "Ciência da Computação",
          date: "17/04/2017",
          numVacancies: 1,
          localization: "ASA NORTE",
          semester: "4º ao 6º",
          payment: "R$ 1100,00 + benefícios",
          period: "08:00 às 14:00 / 12:00 às 16:00",
          requirements: "Java, Spring, AngularJS e Hibernate."
        },
        {
          course: "Biblioteconomia",
          date: "17/04/2017",
          numVacancies: 3,
          localization: "ÁGUAS CLARAS",
          semester: "2º ao 8º",
          payment: "R$ 700,00 + benefícios",
          period: "08:00 às 12:00 / 14:00 às 16:00",
          requirements: "Windows, Word e Excel."
        },
        {
          course: "Ciência da Computação",
          date: "20/04/2017",
          numVacancies: 2,
          localization: "ASA SUL",
          semester: "4º ao 6º",
          payment: "R$ 800,00 + benefícios",
          period: "08:00 às 12:00 / 14:00 às 16:00",
          requirements: "GraphQL, React, Redux e ES6."
        }
      ];
    }

    /* This will be retrieved from an api */
    function apiCallToGetAreas() {
      return [
        {
          id: 1,
          course: "Administração",
          numOffers: 1
        },
        {
          id: 2,
          course: "Biblioteconomia",
          numOffers: 1
        },
        {
          id: 3,
          course: "Ciência da Computação",
          numOffers: 2
        }
      ];
    }
  }

})();
