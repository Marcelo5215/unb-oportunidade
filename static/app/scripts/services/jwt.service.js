angular.module('unbOportunidade')
  .service('jwtService', ['$http', 'store', JWTService])

function JWTService($http, store) {

  this.auth = function(username, password) {
    return $http({
      method: 'GET',
      url: 'login/',
      data: {
        username: username,
        password: password
      }
    });
  };

  this.verifyAuth = function(token) {
    return $http({
      method: 'POST',
      url: 'token-verify/',
      data: { token: token }
    });
  };

  this.refreshAuth = function(token) {
    return $http({
      method: 'POST',
      url: 'token-refresh/',
      data: { token: token }
    });
  };
}
