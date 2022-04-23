var NoOfBeds = ['1', '2', '3']

Plotly.d3.csv('https://raw.githubusercontent.com/nhakkarainen/NU-Project-3/main/Output/housing_prices.csv', (err, rows) => {
  var data = NoOfBeds.map(y => {
    var d = rows.filter(r => r.NoOfBeds === y)
  
    return {
      type: 'bar',
      name: y,
      x: d.map(r => r.State),
      y: d.map(r => r.Jan2020)
    }
  })
  
  Plotly.newPlot('graph', data)
})