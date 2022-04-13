$(document).ready(function() {
    var chartOneDom = document.getElementById("linegraph");
    var chartOne = echarts.init(chartOneDom);

    var chartOneOption = {
        color: ['#4aa9e9'],

        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['Number of Visits']
        },

        calculable : true,
        xAxis : [
            {
                type : 'category',
                boundaryGap : false,
                data: ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value}'
                }
            }
        ],
        series : [

            {
                name:'Number of Visits',
                type:'line',
                data:[1, 5, 20, 10, 15, 7, 14],
                markPoint : {
                    data : [
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name : 'Average'}
                    ]
                }
            }
        ]
    };

    if (chartOneOption && typeof chartOneOption === "object") {
        chartOne.setOption(chartOneOption, true);
    }

    var dom = document.getElementById("hello");
    var npChart = echarts.init(dom);

    var app = {};
    option = null;
    option = {
        color: ['#62549a','#4aa9e9', '#ff6c60' ],
        tooltip : {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            orient : 'vertical',
            x : 'left',
            data:['Positive','Negative','Neutral']
        },
        calculable : false,
        series : [
            {
                name:'Source',
                type:'pie',
                radius : ['50%', '70%'],

                data:[
                    {value:335, name:'Positive'},
                    {value:310, name:'Negative'},
                    {value:234, name:'Neutral'},

                ]
            }
        ]
    };

    if (option && typeof option === "object") {
        npChart.setOption(option, false);
    }

    var dom = document.getElementById("emotion");
    var rainChart = echarts.init(dom);

    var app = {};
    option = null;
    option = {
        color: ['#e9724d'],
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['People']
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                data : ['Positive', 'Neutral','Negative']
            }
        ],
        yAxis : [
            {
                type : 'value'
            }
        ],
        series : [

            {
                name:'People',
                type:'bar',
                data:[10, 12, 7],
                markPoint : {
                    data : [
                        {name : 'Max', value : 182.2, xAxis: 7, yAxis: 183, symbolSize:18},
                        {name : 'Min', value : 2.3, xAxis: 11, yAxis: 3}
                    ]
                },
                markLine : {

                }
            }
        ]
    };
});