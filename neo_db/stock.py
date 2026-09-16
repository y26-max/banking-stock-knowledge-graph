#导入数据分析和量化常用库
import pandas as pd
import tushare as ts
import numpy as np
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
#股票数据可视化分析实例
#获取A股交易数据
def get_price(code='sh',start='2019-01-01',end='2025-03-07'):
    df=ts.get_k_data(code,start,end)
    df.index=pd.to_datetime(df.date)
    #将成交量单位改为10000手并取整数
    df['volume']=(df['volume']/10000).apply(int)
    return df[['open','close','high','low','volume']]
sh=get_price()
if __name__ == '__main__':
    get_price()
#sh.head()

def main():
    import pandas as pd
    import tushare as ts
    import numpy as np
    from pyecharts.charts import Line
    from pyecharts import options as opts

    # 定义获取股票数据的函数
    def get_price(code='sh', start='2019-01-01',end='2025-03-07'):
        df = ts.get_k_data(code, start, end)
        df.index = pd.to_datetime(df.date)
        # 将成交量单位改为 10000 手并取整数
        df['volume'] = (df['volume'] / 10000).apply(int)
        return df[['open', 'close', 'high', 'low', 'volume']]

    # 获取数据
    sh = get_price()

    # 计算分位数
    des = sh.close.describe()
    v1, v2, v3 = np.ceil(des['25%']), np.ceil(des['50%']), np.ceil(des['75%'])

    # 定义颜色分段
    pieces = [
        {"min": v3, "color": "red"},
        {"min": v2, "max": v3, "color": "blue"},
        {"min": v1, "max": v2, "color": "black"},
        {"max": v1, "color": "green"},
    ]

    # 创建图表
    g = (
        Line({'width': '100%', 'height': '480px'})  # 设置画布大小
        .add_xaxis(xaxis_data=sh.index.strftime('%Y%m%d').tolist())  # x 数据
        .add_yaxis(
            series_name="",  # 序列名称
            y_axis=sh.close.values.tolist(),  # 添加 y 数据
            is_smooth=True,  # 平滑曲线
            is_symbol_show=False,  # 不显示折线的小圆圈
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2),  # 线宽
            markpoint_opts=opts.MarkPointOpts(  # 添加标记符
                data=[
                    opts.MarkPointItem(type_='max', name='最大值'),
                    opts.MarkPointItem(type_='min', name='最小值'),
                ],
                symbol_size=[100, 30],
            ),
            markline_opts=opts.MarkLineOpts(  # 添加均值辅助线
                data=[opts.MarkLineItem(type_="average")]
            ),
        )
        .set_global_opts(  # 全局参数设置

            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            visualmap_opts=opts.VisualMapOpts(  # 视觉映射配置
                orient="horizontal",
                split_number=4,
                pos_left='center',
                is_piecewise=True,
                pieces=pieces,
            ),
            legend_opts=opts.LegendOpts(  # 调整图例
                pos_bottom="10%",  # 图例距离底部的距离
                item_width=30,  # 图例项的宽度
                item_height=20,  # 图例项的高度
                textstyle_opts=opts.TextStyleOpts(font_size=14),  # 图例字体大小
            ),
        )
        .set_series_opts(
            markarea_opts=opts.MarkAreaOpts(  # 标记区域配置项
                data=[
                    opts.MarkAreaItem(name="牛市", x=("20200505", "20200708")),
                    opts.MarkAreaItem(name="牛市", x=("20230101", "20230405")),
                ]
            )
        )
    )

    g.render('../templates/stock.html')
if __name__ == '__main__':
    main()
