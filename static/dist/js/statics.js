
    var rent = 0;
    var sold_price = 0;
    var total = 0;
    $(document).ready(function () {
      $(".rent_price").each(function () {
        rent += parseInt($(this).text());
      });
      $(".sold_price").each(function () {
        sold_price += parseInt($(this).text());
      });
      total = rent + sold_price;
      $("#totalsalarys").text("$" + total);
      $(".rent_price").hide()
      $(".sold_price").hide()
    })

    $(function () {
      'use strict'

      var ticksStyle = {
        fontColor: '#495057',
        fontStyle: 'bold'
      }

      var mode = 'index'
      var intersect = true

      var $salesChart = $('#sales-chart')

      var salesChart = new Chart($salesChart, {

        type: 'bar',

        data: {

          labels: [


            'تفاصيل الموظفين',

          ],


          datasets: [
            {
              backgroundColor: '#007bff',
              borderColor: '#007bff',
              data: [
                rent,
              ]
            },
            {
              backgroundColor: '#ced4da',
              borderColor: '#ced4da',
              data: [
                sold_price,
              ]
            }
          ]
        },



        options: {
          maintainAspectRatio: false,
          tooltips: {
            mode: mode,
            intersect: intersect
          },
          hover: {
            mode: mode,
            intersect: intersect
          },
          legend: {
            display: false
          },
          scales: {
            yAxes: [{
              // display: false,
              gridLines: {
                display: true,
                lineWidth: '4px',
                color: 'rgba(0, 0, 0, .2)',
                zeroLineColor: 'transparent'
              },
              ticks: $.extend({
                beginAtZero: true,

                // Include a dollar sign in the ticks
                callback: function (value, index, values) {
                  if (value >= 1000) {
                    value /= 1000
                    value += 'k'
                  }
                  return value
                }
              }, ticksStyle)
            }],
            xAxes: [{
              display: true,
              gridLines: {
                display: false
              },
              ticks: ticksStyle
            }]
          }
        }
      });

      var pieChart = document.getElementById('visitors-chart').getContext('2d')

      var myPieChart = new Chart(pieChart, {
        type: 'pie',
        data: {
          datasets: [{
            data: [{{ bookava }}, {{ bookso }},{{ bookre }}],
      backgroundColor : ["#27c100", "#f3545d", "#fdaf4b"],
      borderWidth: 10,
        
      }],
      labels: ['Available', 'Sold', 'Rented'] 
    },
      options : {
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        position: 'bottom',
        labels: {
          fontColor: '#000',
          fontSize: 15,
          usePointStyle: true,
          padding: 30
        }
      },
      pieceLabel: {
        render: 'percentage',
        fontColor: 'white',
        fontSize: 14,
      },


    }
  })

})


