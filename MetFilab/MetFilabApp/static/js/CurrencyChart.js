function drawCurrencyChart(id, seriesOptions) {

	var chartId = "#" + id;

	// $(chartId).highcharts('StockChart',{
	// 	chart: {
	// 		marginRight: 50
	// 	},

	// 	series: seriesOptions,

	// });
	$(chartId).highcharts('StockChart', {

		rangeSelector: {
			inputEnabled: false,
		    selected: 4
		},

		yAxis: {
		    title: {
		    	text: 'Currency',
		        tyle: {
		            color: '#7cb5ec',
		            fontWeight: 'bold'
		        }
		    },
		    labels: {
		        formatter: function () {
		        	return (this.value > 0 ? ' + ' : '') + this.value + '%';
		        }
		    },
		    plotLines: [{
		        value: 0,
		        width: 2,
		        color: 'silver'
		    }],
		    floor: -10,
		},

		legend: {
		    enabled: true
		},

		plotOptions: {
		    series: {
		    	compare: 'value'
		    }
		},

		tooltip: {
		    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> <br/>',
		    valueDecimals: 2
		},

		series: seriesOptions
	});


}