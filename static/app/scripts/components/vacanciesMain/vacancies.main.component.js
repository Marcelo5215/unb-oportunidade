(function () {

  angular.module('unbOportunidade')
    .component('vacanciesMain', {
      templateUrl: 'static/app/scripts/components/vacanciesMain/vacancies-main.html',
      controller: VacanciesController
    });

  function VacanciesController($scope, $state) {

    $scope.vagas = {
      vaga1: {
        titulo: 'Estágio em desenvolvimento de Software',
        descricao: 'Desenvolvedor Python',
        carga_horaria: '20h semanais',
        semestre_minimo: 'Segundo semestre',
        empresa: 'IBM',
        turno: 'Vespertino',
        empresa: {
          cnpj: null,
          razao_social: null,
          nome_fatansia: null,
          conveniada: null,
          usuario: null,
          imagem: null
        }
      },
      vaga2: {
        titulo: 'Estágio em RH',
        descricao: 'Assistente de RH',
        carga_horaria: '20h semanais',
        semestre_minimo: 'Quarto semestre',
        empresa: 'Coca-Cola',
        turno: 'Matutino',
        empresa: {
          cnpj: null,
          razao_social: null,
          nome_fatansia: null,
          conveniada: null,
          usuario: null,
          imagem: null
        }
      },
      vaga3: {
        titulo: 'Estágio em Engenharia Civil',
        descricao: 'Auxiliar de obra',
        carga_horaria: '30h semanais',
        semestre_minimo: 'Quinto semestre',
        empresa: 'Odebrech',
        turno: 'Horário Maleavel',
        empresa: {
          cnpj: null,
          razao_social: null,
          nome_fatansia: null,
          conveniada: null,
          usuario: null,
          imagem: null
        }
      }
    }

  }


})();
