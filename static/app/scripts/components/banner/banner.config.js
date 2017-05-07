angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider
      .state('bannerState', {
        url: '/vagas',
        template: '<banner-comp> </banner-comp>'
      });

  });
