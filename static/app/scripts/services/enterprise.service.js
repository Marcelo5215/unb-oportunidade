angular.module('unbOportunidade')
  .service('enterpriseService', enterpriseService)

function enterpriseService($http) {

  this.getAllEnterprises = function(callback) {
    $http({
      method: 'GET',
      url: '/api/empresas'
    }).then(callback);
  }

  this.getEnterprise = function(id, callback) {
    $http({
      method: 'GET',
      url: '/api/empresas' + id
    }).then(callback);
  }

  this.createEnterprise = function(enterpriseData, callback) {
    $http({
      method: 'ṔOST',
      url: '/api/empresas',
      data: enterpriseData
    }).then(callback);
  }

  this.updateEnterprise = function(enterpriseData, callback) {
    $http({
      method: 'PATCH',
      url: '/api/empresas/' + enterpriseData.id,
      data: enterpriseData,
    }).then(callback);
  }

}
