angular.module('unbOportunidade')
  .service('vacanciesService', ['$http', VacanciesService]);

function VacanciesService($http) {
  this.getAllVacancies = function() {
    return $http.get('api/vagas/');
  };

  this.getVacancy = function(id) {
    return $http.get('api/vagas/' + id);
  };

  this.getEnterpriseVacancies = function(enterprise_id) {
    return $http.get('api/vagas/?empresa=' + enterprise_id);
  };

  this.filterCourseVacancies = function (course_id) {
    return $http.get('api/vagas/?curso=' + course_id);
  }

}
