angular.module('unbOportunidade')
  .service('vacanciesService', ['$http', VacanciesService]);

function VacanciesService($http) {

  // Retorna todas as vagas ativas do sistema.
  this.getAllActiveVacancies = function() {
    return $http.get('api/vagas/?is_ativa=true');
  };

  // Retorna vaga específica pelo id.
  this.getVacancy = function(id) {
    return $http.get('api/vagas/' + id);
  };

  // Retorna todas as vagas de uma empresa (ativas e não ativas)
  this.getAllEnterpriseVacancies = function (enterprise_id) {
    return $http.get('api/vagas/?empresa=' + enterprise_id)
  };

  // Retorna todas as vagas ativas de uma empresa.
  this.getActiveEnterpriseVacancies = function(enterprise_id) {
    return $http.get('api/vagas/?is_ativa=true&empresa=' + enterprise_id);
  };

  // Retorna todas as vagas ativas de acordo com um curso.
  this.getActiveCourseVacancies = function(course_id) {
    return $http.get('api/vagas/?is_ativa=true&curso=' + course_id);
  };

  // Retorna todas as vagas ativas de acordo com curso e empresa.
  this.getActiveCourseEnterpriseVacancies = function(course_id, enterprise_id) {
    return $http.get('api/vagas/?is_ativa=true&curso=' + course_id + '&empresa=' + enterprise_id);
  };

}
