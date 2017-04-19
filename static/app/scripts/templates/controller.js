(function () {

  angular.module('unbOportunidade')
    .controller('controllerTemp', [
      '$scope', 'djangoAuth', function ($scope, djangoAuth) {

        $scope.opa = { tudo: 'bom' };

        console.log('oi');

      }]);

})();
