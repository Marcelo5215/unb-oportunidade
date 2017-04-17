angular.module('unbOportunidade')
  .service('exemploService', ['$http', serviceExemplo])

function serviceExemplo($http) {

  this.getExemplo = $http({
    method: 'GET',
    url: 'url/do/get'
  });

}
