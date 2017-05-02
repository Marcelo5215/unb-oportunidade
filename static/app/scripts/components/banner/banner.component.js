(function () {

  angular.module('unbOportunidade')
    .component('bannerComp', {
      templateUrl: 'static/app/scripts/components/banner/banner.html',
      controller: BannerController
    });

  function BannerController($scope) {
      $scope.quantidadeVagas = '155';
  }

})();
