option = {
    title: {
        text: 'Sankey Diagram'
    },
    tooltip: {
        trigger: 'item',
        formatter: "{b}"
    },
    series: [{
        type: 'sankey',
        layout: 'none',
        data: [
              {
                "name": "1",
                "value": "99",
                "type": "l1",
                "itemStyle": {
                    "normal": {
                        "color": "#D40404"
                    }
                },
                "label": {
                    "normal": {
                        "position": "l1"
                    }
                }
            },

                {
                "name": "2",
                "value": "99",
                "type": "l1",
                "itemStyle": {
                    "normal": {
                        "color": "#D40404"
                    }
                },
                "label": {
                    "normal": {
                        "position": "l1"
                    }
                }
            },

                {
                "name": "3",
                "value": "99",
                "type": "l1",
                "itemStyle": {
                    "normal": {
                        "color": "#D40404"
                    }
                },
                "label": {
                    "normal": {
                        "position": "l1"
                    }
                }
            },

                {
                "name": "4",
                "value": "99",
                "type": "l1",
                "itemStyle": {
                    "normal": {
                        "color": "#D40404"
                    }
                },
                "label": {
                    "normal": {
                        "position": "l1"
                    }
                }
            },

                {
                "name": "5",
                "value": "99",
                "type": "l1",
                "itemStyle": {
                    "normal": {
                        "color": "#D40404"
                    }
                },
                "label": {
                    "normal": {
                        "position": "l1"
                    }
                }
            },
            
            
            
            
            ],
        links: [
            {
                "source": "1",
                "target": "2",
                "value": "4",
                "lineStyle": {
                    "normal": {
                        "color": "D40404",
                        "opacity": 0.05
                    }
                }
            },

        ],
        itemStyle: {
            normal: {
                borderWidth: 1,
                borderColor: '#000'
            }
        },
        lineStyle: {
            normal: {
                curveness: 0.5
            }
        }
    }]
}