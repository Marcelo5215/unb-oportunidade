angular.module('unbOportunidade')
  .service('searchService', ['$http', SearchService])

function SearchService($http) {

  this.searchCompany = function (callback) {
    $http({
        method: 'GET',
        url: '/api/busca/SearchCompany/'
    }).then(callback);
  }

  this.searchVacancy = function (callback) {
    $http({
      method: 'GET',
      url: '/api/busca/SearchVacancy/'
    }).then(callback);
  }

  this.courses = function (callback) {
    $http({
      method: 'GET',
      url: '/api/busca/course/'
    }).then(callback);
  }

}
