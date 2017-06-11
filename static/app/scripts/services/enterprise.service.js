angular.module('unbOportunidade')
  .service('enterpriseService', enterpriseService)

function enterpriseService($http) {

  this.createUser = function (userData, callback) {
    $http({
      method: 'POST',
      url: 'usuarios/',
      data: JSON.stringify({
        email: 'email@email.com',
        password: '123456'
      })
    }).then(callback);
  }

  this.getAllEnterprises = function(callback) {
    $http({
      method: 'GET',
      url: 'empresas/'
    }).then(callback);
  }

  this.getEnterprise = function(id, callback) {
    $http({
      method: 'GET',
      url: 'empresas/' + id
    }).then(callback);
  }

  this.createEnterprise = function(enterpriseData, callback) {
    $http({
      method: 'ṔOST',
      url: 'empresa/s',
      data: enterpriseData
    }).then(callback);
  }

  this.updateEnterprise = function(enterpriseData, callback) {
    $http({
      method: 'PATCH',
      url: 'empresas/' + enterpriseData.id,
      data: enterpriseData,
    }).then(callback);
  }

}
