# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:10:08 2017

@author: wangjing
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:08:48 2017

@author: wangjing
"""

# -*- coding: utf-8 -*-

import time
import requests
import pymysql.cursors
import pymysql
connection = pymysql.connect(host='58edd9c77adb6.bj.cdb.myqcloud.com',
                             port=5432,
                             user='root',
                             password='1160329981wang',
                             db='hotshuju',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#url = 'http://dc.simuwang.com/'
#formdata ={'name':'18604309462','pass':'1160329981wang','rz_cback':'jQuery17207119221001745222_1505624722482',
          # 'type':'login','_':'1505626246611','m':'passport','c':'auth','a':'login'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
#z6 = requests.post(url = url,data = formdata,headers = headers)
#print(z6)
#headerss = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

#urls = 'http://dc.simuwang.com/index.php?m=Data2&c=Chart&a=jzdb_fund&fund_id=HF00001PJ4&muid=147832&index_type=0&rz_type=0&nav_flag=1&period=0'
for i in range(1,115):
    urls = 'http://dc.simuwang.com/Ranking/get.html?page='+str(i)+'&condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Bistiered%3A0%3Bcompany_type%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A'
#urls ='http://dc.simuwang.com/Ranking/get.html?condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Bistiered%3A0%3Bcompany_type%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A'
    r = requests.get(url= urls,headers = headers)
    time.sleep(3)
    myjson= r.json()
    for listall in myjson['data']:
        try:
            citys = listall['city']
            company_short_name= listall['company_short_name']
            fund_id = listall['fund_id']
            fund_name= listall['fund_name']
            fund_short_name= listall['fund_short_name']
            inception_date= listall['inception_date']
            nav= listall['nav']
            price_date= listall['price_date']
            profit_col1= listall['profit_col1']
            profit_col2=listall['profit_col2']
            profit_col3= listall['profit_col3']
            profit_col4= listall['profit_col4']
            profit_col5= listall['profit_col5']
            profit_col6= listall['profit_col6']
            province= listall['province']
            register_number= listall['register_number']
            relative_nav= listall['relative_nav']
            ret_1m = listall['ret_1m']
            ret_1y= listall['ret_1y']
            ret_2y= listall['ret_2y']
            ret_3m= listall['ret_3m']
            ret_3y= listall['ret_3y']
            ret_4y=listall['ret_4y']
            ret_5y= listall['ret_5y']
            ret_6m= listall['ret_6m']
            ret_incep = listall['ret_incep']
            ret_incep_a= listall['ret_incep_a']
            ret_ytd= listall['ret_ytd']
            sharperatio_1y= listall['sharperatio_1y']
            sharperatio_2y= listall['sharperatio_2y']
            sharperatio_3y= listall['sharperatio_3y']
            sharperatio_3m=listall['sharperatio_3m']
            sharperatio_4y= listall['sharperatio_4y']
            sharperatio_5y= listall['sharperatio_5y']
            sharperatio_6m= listall['sharperatio_6m']
            sharperatio_2011=listall['sharperatio_2011']
            sharperatio_2012= listall['sharperatio_2012']
            sharperatio_2013=listall['sharperatio_2013']
            sharperatio_2014= listall['sharperatio_2014']
            sharperatio_2015= listall['sharperatio_2015']
            sharperatio_2016= listall['sharperatio_2016']
            sharperatio_incep=listall['sharperatio_incep']
            sharperatio_ytd= listall['sharperatio_ytd']
            strategy= listall['strategy']
        except:
            citys = ''
            company_short_name= ''
            fund_id = ''
            fund_name= ''
            fund_short_name= ''
            inception_date= ''
            nav= ''
            price_date= ''
            profit_col1= ''
            profit_col2= ''
            profit_col3= ''
            profit_col4= ''
            profit_col5= ''
            profit_col6= ''
            province= ''
            register_number= ''
            relative_nav= ''
            ret_1m = ''
            ret_1y= ''
            ret_2y= ''
            ret_3m= ''
            ret_3y= ''
            ret_4y= ''
            ret_5y= ''
            ret_6m= ''
            sharperatio_1y= ''
            sharperatio_2y= ''
            sharperatio_3y= ''
            sharperatio_3m= ''
            sharperatio_4y= ''
            sharperatio_5y= ''
            sharperatio_6m= ''
            sharperatio_2011= ''
            sharperatio_2012= ''
            sharperatio_2013= ''
            sharperatio_2014= ''
            sharperatio_2015= ''
            sharperatio_2016= ''
            strategy= ''
            ret_incep=''
            ret_incep_a=''
            ret_ytd=''
            sharperatio_incep=''
            sharperatio_ytd=''
        
        if  citys=='' or company_short_name==''or fund_id=='' or fund_name =='' or fund_short_name == '' or inception_date =='' or nav=='' or price_date =='' or profit_col1=='' or profit_col2 ==''or profit_col3=='' or profit_col4 =='' or profit_col5=='' or profit_col6=='' or province==''or register_number =='' or relative_nav=='' or ret_1m =='' or ret_1y=='' or ret_2y== '' or ret_3m=='' or ret_3y=='' or ret_4y=='' or ret_5y=='' or ret_6m=='' or sharperatio_1y=='' or sharperatio_2y=='' or sharperatio_3m=='' or sharperatio_3y=='' or sharperatio_4y==''or sharperatio_5y==''  or sharperatio_6m=='' or sharperatio_2011==''or sharperatio_2012=='' or sharperatio_2013 =='' or sharperatio_2014=='' or sharperatio_2015=='' or sharperatio_2016=='' or strategy==''or ret_incep=='' or ret_incep_a=='' or ret_ytd=='' or sharperatio_incep=='' or sharperatio_ytd=='':
            continue
        print(citys,sharperatio_incep)
        #try:
            #with connection.cursor() as cursor:
                
                
                # 执行sql语句，插入记录
                #SQL = """insert into smppxiapus2(citys,company_short_name, fund_id, fund_name,fund_short_name ,inception_date,nav,price_date , profit_col1, profit_col2 , profit_col3, profit_col4 , profit_col5,profit_col6, province,register_number, relative_nav,ret_1m ,ret_1y,ret_2y,ret_3m, ret_3y,ret_4y, ret_5y,ret_6m,sharperatio_1y,sharperatio_2y,sharperatio_3m,sharperatio_3y,sharperatio_4y,sharperatio_5y,sharperatio_6m,sharperatio_2011,sharperatio_2012,sharperatio_2013,sharperatio_2014,sharperatio_2015,sharperatio_2016,ret_incep,ret_incep_a,ret_ytd,sharperatio_incep,sharperatio_ytd,strategy)
                #values
                #(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s)"""
                #cursor.execute(SQL,(citys,company_short_name, fund_id, fund_name,fund_short_name ,inception_date,float(nav),price_date , profit_col1, profit_col2 , profit_col3, profit_col4 , profit_col5,profit_col6, province,register_number, relative_nav,ret_1m ,ret_1y,ret_2y ,ret_3m, ret_3y,ret_4y, ret_5y,ret_6m,sharperatio_1y,sharperatio_2y,sharperatio_3m,sharperatio_3y,sharperatio_4y,sharperatio_5y,sharperatio_6m,sharperatio_2011,sharperatio_2012,sharperatio_2013,sharperatio_2014,sharperatio_2015,sharperatio_2016,ret_incep,ret_incep_a,ret_ytd,sharperatio_incep,sharperatio_ytd,strategy))
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                #connection.commit()
            
            
       # except Exception as e:
            #print('***** Logging failed with this error:', str(e))



    
#times = myjson['categories']
#syls = myjson['data'][0]
#nav_lists=myjson['nav_list']
#for time,syl, nav_list in zip(times,syls,nav_lists):
    #print(time,syl,nav_list)
