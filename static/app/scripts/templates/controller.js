(function () {

  angular.module('unbOportunidade')
    .controller('controllerTemp', [
      '$scope', '$http', 'store', function ($scope, $http, store) {

        $scope.login = function () {

          $http.post('api/api-token-auth/',
              {
                'username': $scope.username,
                'password': $scope.password
              })
              .then(function (response) {
                $scope.logged = true;
                $scope.jwt = response.data.token;
                console.log(response);
                console.log(response.data.token);
                store.set('token', response.token);
              },function (response) {
                $scope.logged = false;
                console.log(response);
              });
        }

    }]);

})();
