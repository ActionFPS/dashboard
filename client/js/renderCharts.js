/* Declare undefined globals for ESLint. */
/*
global
  $: true
  Chart: true
  moment: true
*/

$(() => {
  $.getJSON('chart.json')
    .then((jsonData) => {
      const sortedDates = Object.keys(jsonData).sort((a, b) => new Date(a) - new Date(b));
      const sortedData = [];
      const formattedDates = [];
      // Put data into an array in the same order as the sorted datasets
      // Also format the dates into the format "Mar 4th, 2017"
      sortedDates.forEach((key) => {
        sortedData.push(jsonData[key]);
        formattedDates.push(moment(key).format('MMM Do, YYYY'));
      });

      const ctx = $('#game-chart');

      // Create chart
      const chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: formattedDates,
          datasets: [{
            label: 'Game Count',
            data: Object.values(sortedData),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 0.3,
          }],
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true,
              },
            }],
          },
        },
      });
    })
    .catch((error) => {
      console.log(error);
    });
});
