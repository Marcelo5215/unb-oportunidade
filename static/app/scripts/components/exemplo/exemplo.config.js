angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider
      .state('exemploState', {
        url: '/exemplo',
        template: '<exemplo-comp> </exemplo-comp>'
      });

  });
