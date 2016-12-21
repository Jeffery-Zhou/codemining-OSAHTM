# coding:utf-8
"""
bar.js 	21451 	352
boxplot.js 	19318 	343
component_brush.js 	21236 	375
component_dataarea_narrow.js 	20969 	382
component_legend.js 	19436 	356
component_markarea.js 	19283 	331
component_markline.js 	20006 	343
component_markpoint.js 	19769 	365
component_timeline.js 	20397 	381
component_title.js 	18873 	308
component_toolbox.js 	21916 	371
component_tooltip.js 	19850 	383
component_version.js 	21695 	388
coordinate_geo.js 	20586 	373
coordinate_polar.js 	20434 	379
coordinate_rectangular.js 	20718 	362
coordinate_singeaxis.js 	20172 	371
funnel.js 	19225 	383
gauge.js 	19156 	369
graph.js 	36390 	656
heatmap.js 	19354 	365
k_line.js 	19294 	376
line.js 	22733 	419
lines.js 	20015 	349
map.js 	20901 	413
parallel.js 	21687 	375
pie.js 	19586 	331
radar.js 	20858 	394
sankey.js 	20705 	397
scatter.js 	22128 	385
treemap.js 	21672 	372
"""

"""
bar.js
boxplot.js
component_brush.js
component_dataarea_narrow.js
component_legend.js
component_markarea.js
component_markline.js
component_markpoint.js
component_timeline.js
component_title.js
component_toolbox.js
component_tooltip.js
component_version.js
coordinate_geo.js
coordinate_polar.js
coordinate_rectangular.js
coordinate_singeaxis.js
funnel.js
gauge.js
graph.js
heatmap.js
k_line.js
line.js
lines.js
map.js
parallel.js
pie.js
radar.js
sankey.js
scatter.js
treemap.js
"""



API_DOC = """echarts: { init: Function, connect: Function, disConnect: Function, dispose: Function, getInstanceByDom: Function, registerMap: Function, getMap: Function, registerTheme: Function,},
echartsInstance: { group: ..., setOption: Function, getWidth: Function, getHeight: Function, getDom: Function, getOption: Function, resize: Function, dispatchAction: Function, on: Function, off: Function, convertToPixel: Function, convertFromPixel: Function, containPixel: Function, showLoading: Function, hideLoading: Function, getDataURL: Function, getConnectedDataURL: ..., clear: ..., isDisposed: ..., dispose: ...,},
action: { highlight: ..., downplay: ..., legend: {...}, legendSelect: ..., legendUnSelect: ..., legendToggleSelect: ...,}, tooltip: {...}, showTip: ..., hideTip: ...,}, dataZoom: {...}, dataZoom: ...,}, visualMap: {...}, selectDataRange: ...,}, timeline: {...}, timelineChange: ..., timelinePlayChange: ...,}, toolbox: {...}, restore: ...,}, pie: {...}, pieSelect: ..., pieUnSelect: ..., pieToggleSelect: ...,}, geo: { geoSelect: ..., geoUnSelect: ..., geoToggleSelect: ...,}, map: {...}, mapSelect: ..., mapUnSelect: ..., mapToggleSelect: ...,}, brush: { brush: ...,},},
events: { 鼠标事件: {...}, click: ..., dblclick: ..., mousedown: ..., mouseup: ..., mouseover: ..., mouseout: ..., globalout: ...,}, legendselectchanged: ..., legendselected: ..., legendunselected: ..., datazoom: ..., datarangeselected: ..., timelinechanged: ..., timelineplaychanged: ..., restore: ..., dataviewchanged: ..., magictypechanged: ..., geoselectchanged: ..., geoselected: ..., geounselected: ..., pieselectchanged: ..., pieselected: ..., pieunselected: ..., mapselectchanged: ..., mapselected: ..., mapunselected: ..., axisareaselected: ..., brush: ..., brushselected: ...,},
"""
8+20+12+23=28+12+23=40+23=63
70 * 2 = 140
35 * 2 = 70

"""


api_list = API_DOC.split('\n')
print api_list
print len(api_list)