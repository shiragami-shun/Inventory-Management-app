document.addEventListener('DOMContentLoaded', function () {
  const dataElement = document.getElementById('product-sales-data');
  if (!dataElement) return;

  const productSales = JSON.parse(dataElement.textContent);

  const productLabels = Object.keys(productSales);
  const productData = Object.values(productSales);

  if (productLabels.length === 0) return;

  const canvas = document.getElementById('productSalesChart');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: productLabels,
      datasets: [{
        data: productData,
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'bottom'
        },
        datalabels: {
          color: '#fff',
          font: {
            weight: 'bold',
            size: 12
          },
          formatter: function(value, context) {
            const label = context.chart.data.labels[context.dataIndex];
            return `${label}\n¥${value.toLocaleString()}`;
          }
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return context.label + ': ¥ ' + context.parsed.toLocaleString();
            }
          }
        }
      }
    },
    plugins: [ChartDataLabels]   // ← 忘れがち
  });  
});
