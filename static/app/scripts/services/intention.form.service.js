angular.module('unbOportunidade')
  .service('intentionFormService', IntentionFormService)

function IntentionFormService($http) {

  this.getForms = function(vaga_id, callback) {
    $http({
      method: 'GET',
      url: '/api/interesses_vagas/',
      params: {
        vaga: vaga_id
      }
    }).then(callback);
  }

  this.submitForm = function(formData, callback) {
    $http({
      method: 'POST',
      url: '/api/interesses_vagas',
      data: formData
    }).then(callback);
  }

}
