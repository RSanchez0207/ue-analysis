// Dashboard 1 Morris-chart
$( function () {
	"use strict";


	// Morris bar chart 1
	Morris.Bar( {
		element: 'morris-bar-chart2',
		data: [ {
			y: 'Joy',
			a: 78,
        }, 
        {
			y: 'Curiosity',
			a: 65,
			
        }, 
        {
			y: 'Gratitude',
			a: 45,
			
        }, 
        {
			y: 'Caring',
			a: 57,
			
        }, 
        {
			y: 'Pride',
			a: 19,
			
        }, 
        {
			y: 'Optimism',
			a: 27,
			
        }, 
        {
			y: 'Amusement',
			a: 34,
			
        },
        {
			y: 'Love',
			a: 58,
			
        },
        {
			y: 'Admiration',
			a: 75,
			
        }

    ],
		xkey: 'y',
		ykeys: [ 'a'],
		labels: [ 'A'],
		barColors: [ '#ead24d'],
		hideHover: 'auto',
		//gridLineColor: '#eef0f2',
		resize: true
	} );

    //end of chart 1

    // Morris bar chart 2
	Morris.Bar( {
		element: 'morris-bar-chart1',
		data: [ 
        {
            y: 'Fear',
            a: 45,
                
        },
        {
			y: 'Nervousness',
			a: 23,
			
        },
        {
			y: 'Realization',
			a: 67,
			
        }

        
    ],
		xkey: 'y',
		ykeys: [ 'a'],
		labels: [ 'A'],
		barColors: [ '#4680ff'],
		hideHover: 'auto',
		gridLineColor: '#eef0f2',
		resize: true
	} );

	//end of chart 2

	// Morris bar chart 3
	Morris.Bar( {
		element: 'morris-bar-chart3',
		data: [ 
        {
            y: 'Annoyance',
            a: 75,
                
        },
        {
			y: 'Anger',
			a: 54,
			
        },
        {
			y: 'Embarrassment',
			a: 35,
			
        }

        
    ],
		xkey: 'y',
		ykeys: [ 'a'],
		labels: [ 'A'],
		barColors: [ '#fc6180'],
		hideHover: 'auto',
		gridLineColor: '#eef0f2',
		resize: true
	} );

	//end of chart 3

	// Morris bar chart 4
	Morris.Bar( {
		element: 'morris-bar-chart4',
		data: [ 
        {
            y: 'Sadness',
            a: 21,
                
        },
        {
			y: 'Disappointment',
			a: 64,
			
        },
		{
			y: 'Relief',
			a: 34,
			
        },
		{
			y: 'Grief',
			a: 45,
			
        },
        {
			y: 'Remorse',
			a: 27,
			
        }

        
    ],
		xkey: 'y',
		ykeys: [ 'a'],
		labels: [ 'A'],
		barColors: ['#4aa9e9'],
		hideHover: 'auto',
		gridLineColor: '#eef0f2',
		resize: true
	} );

	//end of chart 4

	// Morris bar chart 5
	Morris.Bar( {
		element: 'morris-bar-chart5',
		data: [ 
        {
            y: 'Disgust',
            a: 75,
                
        },
        {
			y: 'Disapproval',
			a: 64,
			
        },
        {
			y: 'Desire',
			a: 24,
			
        }

        
    ],
		xkey: 'y',
		ykeys: [ 'a'],
		labels: [ 'A'],
		barColors: [ '#25c3b2'],
		hideHover: 'auto',
		gridLineColor: '#eef0f2',
		resize: true
	} );

	//end of chart 5

	// Morris bar chart 6
	Morris.Bar( {
		element: 'morris-bar-chart6',
		data: [ 
        {
            y: 'Surprise',
            a: 15,
                
        },
        {
			y: 'Confusion',
			a: 25,
			
        },
		{
			y: 'Excitement',
			a: 35,
			
        },
		{
			y: 'Neutral',
			a: 45,
			
        },
        {
			y: 'Approval',
			a: 55,
			
        }

        
    ],
		xkey: 'y',
		ykeys: [ 'a'],
		labels: [ 'A'],
		barColors: [ '#ff6c60'],
		hideHover: 'auto',
		gridLineColor: '#eef0f2',
		resize: true
	} );

	//end of chart 6

} );
