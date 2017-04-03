'use strict';

/**
 * @ngdoc overview
 * @name staticApp
 * @description
 * # staticApp
 *
 * Main module of the application.
 */
angular
  .module('unbOportunidade', [
    'ui.router',
    'ui.bootstrap'
  ])
  .config(['$stateProvider', '$httpProvider']);

function appConfig($stateProvider, $httpProvider) {


  $httpProvider.defaults.cache = true;

}
