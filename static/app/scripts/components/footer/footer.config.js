angular.module('unbOportunidade')
  .config(function($stateProvider) {

    $stateProvider
      .state('footerState', {
        url: '/footer',
        template: '<footer-comp> </footer-comp>'
      });

  });
