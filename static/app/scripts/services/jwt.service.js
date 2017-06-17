angular.module('unbOportunidade')
  .service('jwtService', ['$http', 'store', JWTService])

function JWTService($http, store) {

  this.auth = function(email, password) {
    return $http({
      method: 'POST',
      url: 'api/login/',
      data: {
        email: email,
        password: password
      }
    });
  };

  this.verifyAuth = function(token) {
    return $http({
      method: 'POST',
      url: 'api/token-verify/',
      data: { token: token }
    });
  };

  this.refreshAuth = function(token) {
    return $http({
      method: 'POST',
      url: 'api/token-refresh/',
      data: { token: token }
    });
  };
}
