'use strict';

angular
  .module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap'
  ])
  .config(['$stateProvider', '$httpProvider', appConfig]);

function appConfig($stateProvider, $httpProvider) {


  $httpProvider.defaults.cache = true;
}
