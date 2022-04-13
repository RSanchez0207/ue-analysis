$(document).ready(function() {


    //<!--Doughnut echarts init-->

    var dom = document.getElementById("doughnut");
    var npChart = echarts.init(dom);

    var app = {};
    option = null;
    option = {
        color: ['#25c3b2','#ff6c60', '#eac459' ],
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

  
});
