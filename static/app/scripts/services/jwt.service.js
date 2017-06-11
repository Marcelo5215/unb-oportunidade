angular.module('unbOportunidade')
  .service('jwtService', ['$http', 'store', JWTService])

function JWTService($http, store) {

  this.auth = function(username, password) {
    return $http.post('login/', { username: username, password: password });
  };

  this.verifyAuth = function(token) {
    return $http.post('token-verify/', { token: token });
  };

  this.refreshAuth = function(token) {
    return $http.post('token-refresh/', { token: token });
  };
}
