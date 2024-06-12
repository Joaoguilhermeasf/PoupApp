document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM fully loaded and parsed');

  const menuItems = document.querySelectorAll('.menu li');

  menuItems.forEach(function(menuItem) {
    menuItem.addEventListener('click', function() {
      const submenu = menuItem.querySelector('.submenu');
      const isOpen = menuItem.classList.contains('active');

      // Remover a classe 'active' e fechar todos os submenus
      menuItems.forEach(function(item) {
        item.classList.remove('active');
        const sub = item.querySelector('.submenu');
        if (sub) {
          sub.style.maxHeight = null;
        }
      });

      // Abrir o submenu apenas se não estiver aberto
      if (!isOpen && submenu) {
        menuItem.classList.add('active');
        submenu.style.maxHeight = submenu.scrollHeight + 'px';
      }
    });
  });

fetch('/gastos')
  .then(response => response.json())
  .then(data => {
    // Pegar os valores retornados e atribuir às variáveis globais
    series_values = data.series_values;
    series_dates = data.series_dates;

    // Realizar as operações que dependem dos dados dentro deste bloco
    maxYValue = Math.max(...series_values);
    minYValue = Math.min(...series_values);
    lenDates = series_dates.length;
    mesAtual = data.mesAtual;
    // Inicializar o gráfico ApexCharts após receber os dados
    iniciarGrafico();
  })
  .catch(error => {
    console.error('Erro:', error);
  });

  function getMonthName(monthNumber) {
    const months = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ];

    // Os índices do array começam em 0, então subtrair 1 do número do mês
    return months[monthNumber - 1];
}

function iniciarGrafico() {
  // Código para inicializar o gráfico ApexCharts
  var options = {
    series: [{
      name: 'Gastos',
      data: series_values
    }],
    chart: {
      height: 350,
      type: 'line',
      zoom: {
        enabled: false
      },
      toolbar: {
        show: false
      }
    },
    tooltip: {
      y: {
        formatter: function(value) {
          return 'R$ ' + parseFloat(value).toFixed(2);
        }
      },
      x: {
        formatter: function(value) {
            console.log(value)
            return 'Total gasto em '+ getMonthName(new Date(value).getMonth() + 1);
        }
      }
    },
    forecastDataPoints: {
      count: 7
    },
    stroke: {
      width: 5,
      curve: 'smooth',
      colors: ['#00e8f5']
    },
    xaxis: {
      type: 'datetime',
      categories: series_dates,
      labels: {
        datetimeFormatter: {
          year: 'yyyy',
          month: 'MMM yyyy',
          day: 'dd MMM yyyy'
        }
      }
  },
    yaxis: {
      min: (minYValue -2) < 0 ? 0 : minYValue - 2,
      ...(maxYValue < 20 ? { tickAmount: maxYValue/2+1 } : {}),
    },
    fill: {
      type: 'gradient',
      gradient: {
        shade: 'dark',
        gradientToColors: ['#c92d0e'],
        shadeIntensity: 1,
        type: 'vertical',
        opacityFrom: 100,
        opacityTo: 100,
        stops: [0, 100, 100, 100]
      },
    }
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();
}

  // Código para inicializar o gráfico Plotly
  var data = [
    {
      type: "indicator",
      mode: "gauge+number+delta",
      value: 14943,
      title: { text: "Rendimentos Totais", font: { size: 24 } },
      delta: { reference: 12550, increasing: { color: "green" } },
      gauge: {
        axis: { range: [null, 20000], tickwidth: 1, tickcolor: "darkblue" },
        bar: { color: "#" },
        bgcolor: "white",
        borderwidth: 0.5,
        bordercolor: "gray",
        steps: [
          { range: [5000, 11000], color: "lightyellow" },
          { range: [11000, 16000], color: "lightgreen" },
          { range: [16000, 20000], color: "green" }
        ],
        threshold: {
          line: { color: "black", width: 1 },
          thickness: 0.75,
          value: 19000
        }
      }
    }
  ];

  var layout = {
    height: 300,
    margin: { t: 0, r: 28, l: 25, b: 0 },
    paper_bgcolor: "white",
    font: { color: "black", family: "roboto" }
  };

  var config = { displayModeBar: false }; // Configuração para remover a barra de ferramentas

  Plotly.newPlot('velocimetro', data, layout, {displayModeBar: false}); // Alterado para usar 'velocimetro' e aplicar a configuração correta
});
