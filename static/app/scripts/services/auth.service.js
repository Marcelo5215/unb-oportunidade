angular.module('unbOportunidade')
  .service('jwtService', ['$http', JWTService])

function JWTService($http) {

  this.auth = function(username, password) {
    $http.post('/api/api-token-auth/', { username: username, password: password });
  };

  this.verifyAuth = function(token) {
    $http.post('/api/api-token-verify/', { token: token });
  };

  this.refreshAuth = function(token) {
    $http.post('/api/api-token-refresh/', { token: token });
  };
}
