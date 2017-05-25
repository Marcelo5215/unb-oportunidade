angular.module('unbOportunidade')
  .service('jwtService', ['$http', JWTService])

function JWTService($http) {

  this.auth = function(username, password) {
    $http.post('api/api-token-auth/', { username: username, password: password })
      .then(function(data) {
        store.set('token', data.token);
        // $state.go('somewhere')
      })
      .catch(function(fallback) {
        // Msg de falha de login para usuário
      });
  };

  this.verifyAuth = function(token) {
    return $http.post('api/api-token-verify/', { token: token });
  };

  this.refreshAuth = function(token) {
    return $http.post('api/api-token-refresh/', { token: token });
  };
}
