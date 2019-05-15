from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

k = [['市级', 54389], ['宝山区', 4023], ['崇明区', 251], ['奉贤区', 626], ['虹口区', 2719], ['黄浦区', 2244], ['嘉定区', 2135],
     ['金山区', 791], ['静安区', 2694], ['闵行区', 9593], ['浦东新区', 19565], ['普陀区', 2466], ['青浦区', 963], ['松江区', 303],
     ['徐汇区', 2444], ['杨浦区', 2007], ['长宁区', 1565]]
x = []
y = []

for n in k:
    x.append(n[0])
    y.append(n[1])

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x[1:])
        .add_yaxis("浦东", y[1:])
        # .add_yaxis("浦西", y[])
        .set_global_opts(
        title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(name="停车位数量(个)"),
        xaxis_opts=opts.AxisOpts(name="各区县", axislabel_opts=opts.LabelOpts(rotate=-45)),
        #title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        datazoom_opts=[opts.DataZoomOpts()],
        #datazoom_opts=[opts.DataZoomOpts(orient="vertical")]
        #datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(orient="vertical"), opts.DataZoomOpts(type_="inside")]
        #datazoom_opts=[opts.DataZoomOpts(type_="inside")],

    )
        .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值", symbol='pin'),
                opts.MarkPointItem(type_="min", name="最小值"),
                # opts.MarkPointItem(type_="average", name="平均值"),

            ]
        )
    )
        .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markline_opts=opts.MarkLineOpts(
            data=[
                #opts.MarkLineItem(type_="min", name="最小值"),
                #opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        ),
    )

)

# axisLabel: {interval:0,rotate:40 }

bar.render()
