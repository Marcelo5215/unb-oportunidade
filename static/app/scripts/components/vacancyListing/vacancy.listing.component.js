(function () {

  angular.module('unbOportunidade')
    .component('vacancyListing', {
      templateUrl: 'static/app/scripts/components/vacancyListing/vacancy.listing.html',
      controller: VacancyListingController
    });

  function VacancyListingController($scope) {

    $scope.vacancies = [
      {
        area: "Administração",
        date: "22/03/2017",
        numVacancies: 1,
        localization: "TAGUATINGA",
        semester: "4º ao 6º",
        payment: "R$ 800,00 + benefícios",
        period: "08:00 às 12:00 / 14:00 às 16:00",
        requirements: "Carteira de Habilitação, Windows, Word Excel e Intenet."
      },
      {
        area: "Ciência da Computação",
        date: "17/04/2017",
        numVacancies: 1,
        localization: "ASA NORTE",
        semester: "4º ao 6º",
        payment: "R$ 1100,00 + benefícios",
        period: "08:00 às 14:00 / 12:00 às 16:00",
        requirements: "Java, Spring, AngularJS e Hibernate."
      },
      {
        area: "Biblioteconomia",
        date: "17/04/2017",
        numVacancies: 3,
        localization: "ÁGUAS CLARAS",
        semester: "2º ao 8º",
        payment: "R$ 700,00 + benefícios",
        period: "08:00 às 12:00 / 14:00 às 16:00",
        requirements: "Windows, Word e Excel."
      },
      {
        area: "Ciência da Computação",
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

})();
