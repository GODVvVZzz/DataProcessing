# -*- coding: utf-8 -*-
import pandas as pd
import re

data1 = pd.read_excel("金融科技公司1.xlsx")
data1 = data1.drop_duplicates("公司名称")
#  删除空值
data1.dropna(inplace=True)
lie1 = []
results = []
list_data = list(data1["经营范围"])
for line in list_data:
    xx1 = u"受金融机构委托[\\s\u4e00-\u9fff\u3001]+" + "|" + "接受银行委托[\\s\u4e00-\u9fff\u3001]+"

    xx2 = u"[\\s\u4e00-\u9fff\u3001]+外包" + "|" + "接收银行委托[\\s\u4e00-\u9fff\u3001]+"

    xx3 = u"[\uff08\uff09\uff0c\\s\u4e00-\u9fff\u3001]+业务）" + "|" + "接收金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx4 = u"严禁涉及[\uff0c\\s\u4e00-\u9fff\u3001]+业务" + "|" + "接受银行或其他合法机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx5 = u"以上除[\uff0c\\s\u4e00-\u9fff\u3001]+业务" + "|" + "受金融监管机构授权委托[\\s\u4e00-\u9fff\u3001]+"

    xx6 = u"并不得[\\s\u4e00-\u9fff\u3001]+" + "|" + "接受金融机构合法委托[\\s\u4e00-\u9fff\u3001]+"

    xx7 = u"[\uff0c\\s\u4e00-\u9fff\u3001]+不得经营" + "|" + "接受金融机构及银行及个人委托[\\s\u4e00-\u9fff\u3001]+"

    xx8 = u"不可以从事[\uff0c\\s\u4e00-\u9fff\u3001]+业务" + "|" + "受银行或金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx9 = u"不包含[0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+" + "|" + "接受金融机构及银行委托[\\s\u4e00-\u9fff\u3001]+"

    xx10 = u"不含[\uff0c\\s\u4e00-\u9fff\u3001]+" + "|" + "受银行及金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx11 = u"[\\s\u4e00-\u9fff\u3001]+受金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx12 = u"严禁涉及[\uff0c\\s\u4e00-\u9fff\u3001]+" + "|" + "不能从事[\uff0c\\s\u4e00-\u9fff\u3001]+"

    xx13 = u"以上除[\uff0c\\s\u4e00-\u9fff\u3001]+"

    xx14 = u"不可以从事[\uff0c\\s\u4e00-\u9fff\u3001]+"

    xx15 = u"[\\s\u4e00-\u9fff\u3001]+外包[\\s\u4e00-\u9fff\u3001]+"

    xx16 = u"[\uff0c\\s\u4e00-\u9fff\u3001]+除外" + "|" + "金融终端设备" + "|" + "保险代理销售"

    xx17 = u"除[\uff0c\u3001\u4e00-\u9fff]+"  # 除开头的含 ，、中文 删掉

    xx18 = u"不得[0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+"  # 不得；，、数字）

    xx19 = u"非[\uff0c\u3001\u4e00-\u9fff]+" + "|" + "代办保险服务" + "|" + "保险箱" + "|" + "金融知识"

    xx20 = u"未经[A-Za-z0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+" + "|" + "电子支付、支付结算及清算系统的技术开发"

    xx21 = u"不包括[0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+"  # 不得；，、数字）

    xx22 = u"金融器材" + "|" + "机动车保险代理" + "|" + "支付设备" + "|" + "保险柜" + "|" + "金融设备" + "|" + "金融专用" + "|" + "金融系统工程"

    xx23 = u"金融机具" + "|" + "机动车辆保险业务代理" + "|" + "车辆保险咨询服务" + "|" + "代办机动车保险业务" + "|" + "移动支付终端设备"

    xx24 = u"机动车辆保险业务代理" + "|" + "车辆保险咨询服务" + "|" + "汽车保险" + "|" + "代缴社会保险" + "|" + "机动车辆保险兼业代理"

    xx25 = u"代收保险费" + "|" + "代理相关保险业务的损失勘察和理赔" + "|" + "漫游结算清算" + "|" + "金融产品" + "|" + "工程支付担保" + "|" + "金融软件开发"

    xx = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}|{11}|{12}|{13}|{14}|{15}|{16}|{17}|{18}|{19}|{20}|{21}|{22}|{" \
         "23}|{24}".format(xx18, xx19, xx20, xx21,
                           xx16, xx7, xx8, xx9, xx10,
                           xx11, xx12, xx13, xx14, xx25,
                           xx15, xx22, xx17, xx1, xx2,
                           xx3, xx4, xx5, xx23, xx6, xx24)
    pattern = re.compile(xx)
    results += pattern.findall(line)

    newLine = line
    for result in results:
        newLine = newLine.replace(result, " ")

    lie1.append(newLine)
    results.clear()
data1["经营范围1"] = lie1
d = []
for i, j in zip(data1["经营范围1"].index, data1["经营范围1"]):
    if ("金融" in j) or ("保险" in j) or ("信贷" in j) or ("清算" in j) or ("支付" in j) or ("借贷" in j) or ("融资" in j) or (
            "借款" in j):
        d.append(i)

data1 = data1.loc[d, :]

data2 = pd.read_excel("金融科技公司2.xlsx")
data2 = data2.drop_duplicates("公司名称")
data2.dropna(inplace=True)
lie1 = []
results = []
list_data = list(data2["经营范围"])
for line in list_data:
    xx1 = u"受金融机构委托[\\s\u4e00-\u9fff\u3001]+" + "|" + "接受银行委托[\\s\u4e00-\u9fff\u3001]+"

    xx2 = u"[\\s\u4e00-\u9fff\u3001]+外包" + "|" + "接收银行委托[\\s\u4e00-\u9fff\u3001]+"

    xx3 = u"[\uff08\uff09\uff0c\\s\u4e00-\u9fff\u3001]+业务）" + "|" + "接收金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx4 = u"严禁涉及[\uff0c\\s\u4e00-\u9fff\u3001]+业务" + "|" + "接受银行或其他合法机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx5 = u"以上除[\uff0c\\s\u4e00-\u9fff\u3001]+业务" + "|" + "受金融监管机构授权委托[\\s\u4e00-\u9fff\u3001]+"

    xx6 = u"并不得[\\s\u4e00-\u9fff\u3001]+" + "|" + "接受金融机构合法委托[\\s\u4e00-\u9fff\u3001]+"

    xx7 = u"[\uff0c\\s\u4e00-\u9fff\u3001]+不得经营" + "|" + "接受金融机构及银行及个人委托[\\s\u4e00-\u9fff\u3001]+"

    xx8 = u"不可以从事[\uff0c\\s\u4e00-\u9fff\u3001]+业务" + "|" + "受银行或金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx9 = u"不包含[0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+" + "|" + "接受金融机构及银行委托[\\s\u4e00-\u9fff\u3001]+"

    xx10 = u"不含[\uff0c\\s\u4e00-\u9fff\u3001]+" + "|" + "受银行及金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx11 = u"[\\s\u4e00-\u9fff\u3001]+受金融机构委托[\\s\u4e00-\u9fff\u3001]+"

    xx12 = u"严禁涉及[\uff0c\\s\u4e00-\u9fff\u3001]+" + "|" + "不能从事[\uff0c\\s\u4e00-\u9fff\u3001]+"

    xx13 = u"以上除[\uff0c\\s\u4e00-\u9fff\u3001]+"

    xx14 = u"不可以从事[\uff0c\\s\u4e00-\u9fff\u3001]+"

    xx15 = u"[\\s\u4e00-\u9fff\u3001]+外包[\\s\u4e00-\u9fff\u3001]+"

    xx16 = u"[\uff0c\\s\u4e00-\u9fff\u3001]+除外" + "|" + "金融终端设备" + "|" + "保险代理销售"

    xx17 = u"除[\uff0c\u3001\u4e00-\u9fff]+"  # 除开头的含 ，、中文 删掉

    xx18 = u"不得[0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+"  # 不得；，、数字）

    xx19 = u"非[\uff0c\u3001\u4e00-\u9fff]+" + "|" + "代办保险服务" + "|" + "保险箱" + "|" + "金融知识"

    xx20 = u"未经[A-Za-z0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+" + "|" + "电子支付、支付结算及清算系统的技术开发"

    xx21 = u"不包括[0-9\\s\uff1b\uff0c\u3001\uff1a\u4e00-\u9fff]+"  # 不得；，、数字）

    xx22 = u"金融器材" + "|" + "机动车保险代理" + "|" + "支付设备" + "|" + "保险柜" + "|" + "金融设备" + "|" + "金融专用" + "|" + "金融系统工程"

    xx23 = u"金融机具" + "|" + "机动车辆保险业务代理" + "|" + "车辆保险咨询服务" + "|" + "代办机动车保险业务" + "|" + "移动支付终端设备"

    xx24 = u"机动车辆保险业务代理" + "|" + "车辆保险咨询服务" + "|" + "汽车保险" + "|" + "代缴社会保险" + "|" + "机动车辆保险兼业代理"

    xx25 = u"代收保险费" + "|" + "代理相关保险业务的损失勘察和理赔" + "|" + "漫游结算清算" + "|" + "金融产品" + "|" + "工程支付担保" + "|" + "金融软件开发"

    xx = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}|{11}|{12}|{13}|{14}|{15}|{16}|{17}|{18}|{19}|{20}|{21}|{22}|{" \
         "23}|{24}".format(xx18, xx19, xx20, xx21,
                           xx16, xx7, xx8, xx9, xx10,
                           xx11, xx12, xx13, xx14, xx25,
                           xx15, xx22, xx17, xx1, xx2,
                           xx3, xx4, xx5, xx23, xx6, xx24)
    pattern = re.compile(xx)
    results += pattern.findall(line)

    results = list(set(results))
    newLine = line
    for result in results:
        newLine = newLine.replace(result, " ")

    results = list(set(results))
    lie1.append(newLine)
    results.clear()
data2["经营范围1"] = lie1
d = []
for i, j in zip(data2["经营范围1"].index, data2["经营范围1"]):
    if ("金融" in j) or ("保险" in j) or ("信贷" in j) or ("清算" in j) or ("支付" in j) or ("借贷" in j) or ("融资" in j) or (
            "借款" in j):
        d.append(i)

data2 = data2.loc[d, :]

data = pd.concat([data1, data2])
data.to_excel("合-数据.xlsx")

data["year"] = data["成立日期"].map(lambda x: x[0:4])
data["SUM"] = 1

import numpy as np

year = data.groupby("year").sum().index.astype(int)
goup = data.groupby(["所属城市", "year"]).sum().unstack()
goup = goup.fillna(0)
goup.columns = year
goup1 = goup.copy()
for i in goup.index:
    for j in goup.columns:
        # print(np.sum(goup.loc[i].loc[:j+1]))
        goup.loc[i, j] = np.sum(goup1.loc[i].loc[:j])

goup.to_excel("累加.xlsx")
