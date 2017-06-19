(function() {

  angular.module('unbOportunidade')
    .component('vacancyListing', {
      templateUrl: 'static/app/scripts/components/vacancyListing/vacancy.listing.html',
      controller: VacancyListingController
    });

  function VacancyListingController($scope, $state, vacanciesService, coursesService) {
    $scope.vacancies = [];
    $scope.areas = [];
    $scope.listVacancies = listVacancies;
    $scope.getAllCourses = getAllCourses;
    $scope.vacancyDetail = vacancyDetail;
    $scope.searchVancanciesCourse = searchVancanciesCourse;

    function vacancyDetail(id) {
      $state.go('vacancyDetail', {
        id: id
      });
    }

    function listVacancies() {
        var id = $state.params.curso;
        !id ? getAllVacancies() : searchVancanciesCourse(id);
    }

    function getAllVacancies() {
      vacanciesService.getAllActiveVacancies()
      .then(function(response) {
        $scope.vacancies = response.data;
      });
    }

    function getAllCourses(){
      coursesService.all()
        .then(function(response) {
          $scope.courses = response.data;
        });
    }

    function searchVancanciesCourse(id) {
      vacanciesService.getActiveCourseVacancies(id)
        .then(function(response) {
          $scope.vacancies = response.data;
        });
    }

  }

})();
