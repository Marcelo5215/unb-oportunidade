(function () {

  angular.module('unbOportunidade')
    .component('inputSearch', {
      templateUrl: 'static/app/scripts/components/inputSearch/input-search.html',
      controller: InputSearchController
    });

  function InputSearchController($scope, $state) {

    $scope.search = search;

    function search() {
      $state.go('vacancyListing');
    }

  }


})();
