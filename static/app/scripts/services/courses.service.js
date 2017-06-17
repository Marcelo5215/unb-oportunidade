angular.module('unbOportunidade')
  .service('coursesService', ['$http', CoursesService])

function CoursesService($http) {

  this.all = function() {
    return $http.get('api/cursos/');
  };

  this.one = function(id) {
    return $http.get('api/cursos/', id);
  };
}
