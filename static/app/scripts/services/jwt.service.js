angular.module('unbOportunidade')
  .service('jwtService', ['$http', 'store', JWTService])

function JWTService($http, store) {

  this.auth = function(username, password) {
    $http.post('api/api-token-auth/', { username: username, password: password })
      .then(function(response) {
        store.set('token', response.data.token);
      })
      .catch(function(fallback) {
      });
  };

  this.verifyAuth = function(token) {
    return $http.post('api/api-token-verify/', { token: token });
  };

  this.refreshAuth = function(token) {
    return $http.post('api/api-token-refresh/', { token: token });
  };
}
