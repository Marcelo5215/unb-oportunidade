(function () {

  angular.module('unbOportunidade')
    .component('signup', {
      templateUrl: 'static/app/scripts/components/signup/signup.html',
      controller: SignupController
    });

function SignupController($scope){

      $scope.firstname = null;
      $scope.email = null;
      $scope.celular = null;
      $scope.objetivo = null;

      $scope.data = {
        singleSelect: null,
        multipleSelect: [],
        option1: 'adm'
        option2: 'cic'
        option3 : 'bib'
       };

       $scope.add = function(){
            var f = document.getElementById('file').files[0],
                r = new FileReader();
                r.onloadend = function(e){

                    var data = e.target.result;

              }
              r.readAsBinaryString(f);
            }


}
