(function () {

  angular.module('unbOportunidade')
    .component('inputSearch', {
      templateUrl: 'static/app/scripts/components/inputSearch/input-search.html',
      controller: InputSearchController
    });

  function InputSearchController($scope, $state, coursesService) {

    $scope.listCourses = listCourses;
    $scope.search = search;
    $scope.selectedCourse;

    function search() {
      var course =  JSON.parse($scope.selectedCourse);
      $state.go('vacancyListing', { curso: course.id });
    }

    function listCourses() {
      coursesService.all()
        .then(function(response) {
          $scope.courses = response.data;
        });
    }

  }


})();
