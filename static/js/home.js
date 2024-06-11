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

  // Código para inicializar o gráfico ApexCharts
  var options = {
    series: [{
      name: 'Gastos',
      data: [4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5]
    }],
    chart: {
      height: 350,
      type: 'line',
      toolbar: {
        show: false
      }
    },
    forecastDataPoints: {
      count: 7
    },
    stroke: {
      width: 5,
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ['1/11/2000', '2/11/2000', '3/11/2000', '4/11/2000', '5/11/2000', '6/11/2000', '7/11/2000', '8/11/2000', '9/11/2000', '10/11/2000', '11/11/2000', '12/11/2000', '1/11/2001', '2/11/2001', '3/11/2001', '4/11/2001' ,'5/11/2001' ,'6/11/2001'],
      tickAmount: 10,
      labels: {
        formatter: function(value, timestamp, opts) {
          return opts.dateFormatter(new Date(timestamp), 'dd MMM')
        }
      }
    },
    title: {
      text: '',
      align: 'left',
      style: {
        fontSize: "16px",
        color: '#666'
      }
    },
    fill: {
      type: 'gradient',
      gradient: {
        shade: 'dark',
        gradientToColors: ['#FDD835'], // Alterado para laranja claro
        shadeIntensity: 1,
        type: 'horizontal',
        opacityFrom: 100,
        opacityTo: 100,
        stops: [0, 100, 100, 100]
      },
    }
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

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
        bar: { color: "limegreen" },
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
