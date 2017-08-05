# -*- coding: utf-8 -*-
html_text = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN">
<head>
		
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>国家企业信用信息公示系统</title>
		<meta name="renderer" content="webkit" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
		<meta name="keywords" content="全国 企业 信用 信息 公示" />
		<meta name="description" content="国家企业信用信息公示系统" />
		<meta http-equiv="Cache-Control" content="no-transform" />

        	<link rel="stylesheet" href="/css/lib/reset.css?v=201706272856"/>
        	<link rel="stylesheet" href="/css/lib/zxx.lib.css?v=201706272856"/>
        	<link rel="stylesheet" href="/css/lib/font-awesome.min.css?v=201706272856"/>
        	<link rel="stylesheet" href="/css/common_fq.css?v=201706272856"/>
        	<link rel="stylesheet" href="/css/portal.css?v=201706272856"/>
        	<link rel="stylesheet" href="/css/newInfo.css?v=201706272856"/>
        	<link rel="stylesheet" href="/css/annualReport_fq.css?v=201706272856"/>
	
            <script type="text/javascript" src="/js/lib/jquery-1.11.1.min.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/lib/datatables.min.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/lib/custom_datatables.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/primaryInfoMain.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/details.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/affiche-common-search.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/geetest/geetestlib.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/selectAnnualReport.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/annualreport_public.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/forAnnalReportDetial.js?v=201706272856"></script>
            <script type="text/javascript" src="/js/instant_public.js?v=201706272856"></script>
        <script src="/js/logcollector.js" ></script>

<div style="display:none">
    <link rel="stylesheet" href="/css/mid.css"/>
       <script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1261033118'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s4.cnzz.com/z_stat.php%3Fid%3D1261033118' type='text/javascript'%3E%3C/script%3E"));</script>
         <script type="text/javascript">
			var _hmt = _hmt || [];
			(function() {
			  var hm = document.createElement("script");
			  hm.src = "https://hm.baidu.com/hm.js?cdb4bc83287f8c1282df45ed61c4eac9";
			  var s = document.getElementsByTagName("script")[0]; 
			  s.parentNode.insertBefore(hm, s);
			 })();
		 </script>
		<script type="text/javascript">
			window.onload = function() {sessionId_gsxt = "36A1AB264263B2CA5BA2E9A4898055CC-n1";t1Collect_gsxt();}
		</script>
</div>
<div id="loading" class="mid loading" style="display: none"><img src="/images/loading.png" alt="加载中。。"></div>
<div id="loadFail" class="mid loadFail" style="display: none"><img src="/images/loadFail.png" alt="加载失败"></div>
<div class="model mid" style="display: none"></div>
</head>
<body>
<div class="container">
    <div class="header_box">
        <div class="header f16">
            <div class="header_container rel">
                <a class="menu_item db l tc wh rel" href="/corp-query-homepage.html"><span class="icon_01 db abs"></span>首页</a>
                <a class="menu_item db l tc wh rel pl50" href="/login"><span class="icon_02 db abs"></span>企业信息填报</a>
                <a class="menu_item db l tc wh rel pl50" href="/affiche-query-info-paperall.html?&FKID=0&areaId=100000"><span class="icon_04 db abs"></span>信息公告</a>
                <a class="menu_item db l tc wh rel pl20" href="/affiche-query-info-help.html"><span class="icon_03 db abs"></span>使用帮助</a>
                <span class="menu_item" style="display:inline-block;height:100%;width:0;border-right:none;"></span>
                <div class="r choose_state rel f12" id="choose_state">
                    <div class="tc choose_txt">导航</div>
                      <div class="loadingView abs">加载中......</div>
                      <div class="state_box abs">
                         
                          <table class=" f14 tcc" width="100%">
                            <tr><td class="b tc" width="13%">华北</td><td width="4%">|</td> <td><a href="#">北京</a><a href="#">天津</a><a href="#">河北</a><a href="#">山西</a><a href="#">内蒙古</a></td> </tr>
                            <tr><td class="b tc">东北</td><td>|</td> <td><a href="#">辽宁</a><a href="#">吉林</a><a href="#">黑龙江</a></td> </tr>
                            <tr><td class="b tc">华东</td><td>|</td> <td><a href="#">上海</a><a href="#">江苏</a><a href="#">浙江</a><a href="#">安徽</a><a href="#">福建</a><a href="#">江西</a><a href="#">山东</a></td> </tr>
                            <tr><td class="b tc">华南</td><td>|</td> <td><a href="#">广东</a><a href="#">广西</a><a href="#">海南</a></td> </tr>
                            <tr><td class="b tc">华中</td><td>|</td> <td><a href="#">河南</a><a href="#">湖北</a><a href="#">湖南</a></td> </tr>
                            <tr><td class="b tc">西南</td><td>|</td> <td><a href="#">重庆</a><a href="#">四川</a><a href="#">贵州</a><a href="#">云南</a><a href="#">西藏</a></td> </tr>
                            <tr><td class="b tc">西北</td><td>|</td> <td><a href="#">陕西</a><a href="#">甘肃</a><a href="#">青海</a><a href="#">宁夏</a><a href="#">新疆</a></td> </tr>
                          </table>
                      </div>
                </div>
            </div>
        </div>

    </div>
    <div class="search_box">
        <div class="search auto rel">
            <div class="search_logo_100000"></div>
            <div class="search_box2">
                <div class="searchkuang"></div>
                <div class="tabs f14 r">
                    <span class='search-icon-l'></span>
                    <a href="javascript:;" class="search_tab general_tab selected" onclick="selectTab(this)">企业信用信息</a>
                    <i>|</i>
                    <a href="javascript:;" class="search_tab excep_tab" onclick="selectTab(this)">经营异常名录</a>
                    <i>|</i>
                    <a href="javascript:;" class="search_tab ill_tab" onclick="selectTab(this)">严重违法失信企业名单</a>
                </div><!-- /tabs -->
                <form name="f" action="/corp-query-search-1.html" method="post">
                    <input type="text" id="keyword" name="searchword" placeholder="请输入企业名称、统一社会信用代码或注册号" class="abs">
                    <input id="token" type="hidden" name="token" value="2016" />
                    <input type="hidden" name="tab" id="selectedSearchTab" value=""/>
                    <button id="btn_query" title="查询" type="button" class="abs search_btn">
                    </button>
                    <button id="pop-captcha-submit" class="db f18 l fw" type="submit" style="display: none;"></button>
                    <div id="popup-captcha"></div>
                </form>
            </div>
        </div>
    </div>
<div id="url" class="mainContent">
<script type="text/javascript">

    var VAnnualReportBaseinfoUrl = "/corp-query-entprise-info-annualReportBaseinfo-";
    
    var anCheYearInfo = "/%7BErbGxngVxW85OELepofBn_ECCn1oUAmSsTvqAS0kJ6YLmUwZVhOs5DyOmt9EdB-vsymXYd8H72eDg35q6f-DxRmhLiPMUqnh9K5bukLtZsxMVFUgWhCOa6_42e5g0cxr-1499307223374%7D";
    
    var insLicenceInfoNull = "/%7BErbGxngVxW85OELepofBnwWxgS_GfzNcI9OW5hOkpTcfR-Pe54LX7nXKfUEwtCPMAHVQhV_30x48qPwFOiHrOF2ej0UrrnV0-wQjUCksoomhIpKaV_PidOFyJprzIugF-1499307223376%7D";
    
    var insImKlpInfoNull = "/%7BErbGxngVxW85OELepofBn3zIb_OwZn8iXbzhFYhJWUa-JaBuIrVIVATBVflPzkAOmjk8n8FNBYtvkC1iW02XRmTivHMSyabmQSSfyCf7rt_97O4qGPla-h2GUFpcy4TI-1499307223378%7D";
   
    var tradeMarkDetailUrl ="/%7BErbGxngVxW85OELepofBnzhEjCeuHMGj72Ln4lYYh3A1lvLP5Hlnbrd7GUyfL_hxPrWFqNe2cfPoibeWww_QW-tIe87jcm2urVIsr1OVsHLpuKNATVFrV6X160iaSeW6-1499307223379%7D";
   
    var keyPersonAllUrl ="/%7BErbGxngVxW85OELepofBn6vnBuO5GQTsu1UwVNM-_w_ayAOS1tqMl2HNEHYEUMuoPrWFqNe2cfPoibeWww_QW-tIe87jcm2urVIsr1OVsHJ6m-QF1Z7pOg87VjQd7ftjAAZaKZ4KrTTZ05rA-R0sVA-1499307223381%7D";
   
    var vAnnualReportBaseInfoForJsUrl = "/corp-query-entprise-info-vAnnualReportBaseInfoForJs-";
   
    var vAnnualSfcReportBaseInfoForJsUrl = "/corp-query-entprise-info-vAnnualSfcReportBaseInfoForJs-";
   
    var vAnnualPbReportBaseInfoForJsUrl = "/corp-query-entprise-info-vAnnualPbReportBaseInfoForJs-";
    
    var insLicenceInfoForJsUrl = "/corp-query-entprise-info-insLicenceInfoForJs-";
    
    var insImKlpInfoForJsUrl = "/corp-query-entprise-info-insImKlpInfoForJs-";
   
    var insPunshmentInfoForJsUrl = "/corp-query-entprise-info-insPunshmentInfoForJs-";
    
    var annRepDetailUrl = "/%7BErbGxngVxW85OELepofBn4r2ORDbrL2miD-D1n9JA2HiPHXOYCBYWfnvpW3WmwjkM28zif_oL7E1vMQs9RKilwRgN0nLcvt9VvoLziITy1S2BjDdluaxo7hKsLICuL7k-1499307223382%7D";

    var VAnnualReportSfcBaseinfoUrl = "/corp-query-entprise-info-annualReportSfcBaseinfo-";

    var VAnnualReportPbBaseinfoUrl = "/corp-query-entprise-info-vAnnualReportPbBaseinfo-";

    var punishmentInfoUrl = "/%7BErbGxngVxW85OELepofBn0fc-ByhAjPfBzqIMtxewZwq6h_z2-7pGTo_8NshYgklMHNKYm7MvLK5k0BQOZWbiOBDsa5gIXWBEJJmjgMYZ8lp0LIQH7IBjnstPFsmx7p6-1499307223385%7D";

    var punishmentDetailInfoUrl = "/%7BErbGxngVxW85OELepofBn0fc-ByhAjPfBzqIMtxewZzlnXUJEitrUfocKgYOWd3QM28zif_oL7E1vMQs9RKilwRgN0nLcvt9VvoLziITy1S2BjDdluaxo7hKsLICuL7k-1499307223386%7D"

    var entBusExcepUrl = "/%7BErbGxngVxW85OELepofBn_KJSbX_uKN3qpNSkifwu8xDKPTSqR0Tww8MFMwCdnutKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223388%7D";

    var indBusExcepUrl = "/%7BErbGxngVxW85OELepofBn5TDuIEoMHI80QLbnhVNyCVDKPTSqR0Tww8MFMwCdnutKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223389%7D";

    var argBusExcepUrl = "/%7BErbGxngVxW85OELepofBn-PIYaKvsUqP-JJmfPmHrxZDKPTSqR0Tww8MFMwCdnutKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223390%7D";

    var argBranchBusExcepUrl = "/%7BErbGxngVxW85OELepofBn751PWYd7Kb5wQY626EyEJrMi137rEfFKNmyemSpSJF6mMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223391%7D";

    var IllInfoUrl = "/%7BErbGxngVxW85OELepofBn87XaGNiCSb8OqkwyB0tpN4AdVCFX_fTHjyo_AU6Ies4XZ6PRSuudXT7BCNQKSyiiaEikppX8-J04XImmvMi6AU-1499307223393%7D";

    var spotCheckInfoUrl = "/%7BErbGxngVxW85OELepofBn5xwN3cg_GgSD9aQPqcl5WrvvcVNb7fNFRQ4jQdNhuXxsymXYd8H72eDg35q6f-DxRmhLiPMUqnh9K5bukLtZsxMVFUgWhCOa6_42e5g0cxr-1499307223394%7D";

    var judiciaryStockfreezePersonUrl = "/%7BErbGxngVxW85OELepofBn8ZzD8LN3XGd8PNsrKbIbYwfqhes-1q6ptyCYviL5CmwsSs0Q-5Jvz7-XoQpjaidfNP3Ox-ER5FN17mb4Bm65FkZq7Ie23gehPK7_Zy0e2tQBiqWlRQUiKC2Iyntr30Dxg-1499307223396%7D";

    var judiciaryStockfreezeDetailUrl = "/%7BErbGxngVxW85OELepofBn8ZzD8LN3XGd8PNsrKbIbYyCe_4uZB3QAUZToSu0pZ6VdZA0UEp1n3B3WoPy39VJvSBs58av3P1muYEFPH7iOPfkiQSMrTyKegRfs68Y0qc2-1499307223397%7D"

    var judiciaryAltershareholderUrl = "/%7BErbGxngVxW85OELepofBn8ZzD8LN3XGd8PNsrKbIbYxFgz0iPKD0njX3a8o9MZAOYwE9640clQ7dyBu1UcPVqptEawo9ETOsg6PvODyuzQ-r3WwKeGj5MBJ_ovimE8ku-1499307223398%7D";

    var insInvinfoUrl = "/%7BErbGxngVxW85OELepofBn5GCgQyKZnlAKawe0FC3ClF81C8twOEkdabyx0cxSX5f0_c7H4RHkU3XuZvgGbrkWRmrsh7beB6E8rv9nLR7a1AGKpaVFBSIoLYjKe2vfQPG-1499307223399%7D";

    var insInvAlterStockinfoUrl = "/%7BErbGxngVxW85OELepofBn1iPrPolp-LVu8eb_THl8AYRNUfYG7lgsFyA6vGKtUxDdZA0UEp1n3B3WoPy39VJvSBs58av3P1muYEFPH7iOPfkiQSMrTyKegRfs68Y0qc2-1499307223401%7D";

    var insAlterstockinfoUrl = "/%7BErbGxngVxW85OELepofBn3HDgOKY2WJpjOTOfOIpPU5KO537NNV0KaJaJtsOyd-rmMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223402%7D";

    var insLicenceinfoUrl = "/%7BErbGxngVxW85OELepofBnwWxgS_GfzNcI9OW5hOkpTcPpVykCNNvSCk_tZDLkXg4MHNKYm7MvLK5k0BQOZWbiOBDsa5gIXWBEJJmjgMYZ8lp0LIQH7IBjnstPFsmx7p6-1499307223403%7D";

    var insProPledgeRegInfoUrl = "/%7BErbGxngVxW85OELepofBn6uOlEUWoDQNIaWAPwtoSuHNJnXZsRUyuTJy8cNWf5_YPrWFqNe2cfPoibeWww_QW-tIe87jcm2urVIsr1OVsHLpuKNATVFrV6X160iaSeW6-1499307223404%7D";

    var proPledgeRegInfoUrl = "/%7BErbGxngVxW85OELepofBn3fRBy5sCoNHwy4GwTIKW9HBYw29LT1pU2oeKvqmJmMuM28zif_oL7E1vMQs9RKilwRgN0nLcvt9VvoLziITy1S2BjDdluaxo7hKsLICuL7k-1499307223405%7D";

    var trademarkInfoUrl = "/%7BErbGxngVxW85OELepofBn7CMHic-942g1zMIHWnXrnjs9dl7VFaMcMugPG5PoQKmm0RrCj0RM6yDo-84PK7ND6vdbAp4aPkwEn-i-KYTyS4-1499307223406%7D";

    var insPunishmentinfoUrl = "/%7BErbGxngVxW85OELepofBn4jwT4hPoTXoC5eGMenuLCKz-pWdet578fwREUHxc9FbmMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223407%7D";

    var shareholderUrl = "/%7BErbGxngVxW85OELepofBn7CUZjTxmqaQjZ14-X0ZThnqWMjGRHGCz9e7egPLkQ-ZKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223408%7D";

    var shareholderDetailUrl = "/%7BErbGxngVxW85OELepofBn7CUZjTxmqaQjZ14-X0ZThmhAhC1mUXtwatYaDI2B3MAmMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223409%7D";

    var alterInfoUrl = "/%7BErbGxngVxW85OELepofBnziDi7qIKa_2Zi72s5DwuoiaOTyfwU0Fi2-QLWJbTZdGZOK8cxLJpuZBJJ_IJ_uu3_3s7ioY-Vr6HYZQWlzLhMg-1499307223410%7D";

    var gtAlertInfoUrl = "/%7BErbGxngVxW85OELepofBn3SoH9ezgBWQGNsZIjCJgS0AdVCFX_fTHjyo_AU6Ies4XZ6PRSuudXT7BCNQKSyiiaEikppX8-J04XImmvMi6AU-1499307223411%7D"

    var keyPersonUrl = "/%7BErbGxngVxW85OELepofBnwepBKgymKV2o1ep9sjaNSKo1ALURbZ5qkEDaxLFQZl2m0RrCj0RM6yDo-84PK7ND6vdbAp4aPkwEn-i-KYTyS4-1499307223411%7D";

    var gtKeyPersonUrl = "/%7BErbGxngVxW85OELepofBnxL22UIvCw22oTQF9Q3cNol_PHU-GHAYpnGOoOAD8PbOKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223414%7D";

    var branchUrl = "/%7BErbGxngVxW85OELepofBn2a3guDOZxKy_3DQl-5NHdcpXNGxA2BDf6SL4JW34-59vewt0ONLgxDpOl6r0uwd8mKDWnDnRTxbRbUEipth6Fs-1499307223416%7D";

    var branchUrlAll = "/%7BErbGxngVxW85OELepofBn_yaSE6qiEGBFGWXL4Z6Yvqn6pYSVegyd32GCZ_83YeAM28zif_oL7E1vMQs9RKilwRgN0nLcvt9VvoLziITy1SF2VbXAmYD_-FYGI1ezLuCRZRdMywyDKbZyvxapp-_wg-1499307223418%7D";

    var liquidationUrl = "/%7BErbGxngVxW85OELepofBnzw7l5Q_YDxGKuG8NJY3yoixKBwRShV353r77-cUcGfxKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223420%7D";

    var allTrademarkUrl = "/%7BErbGxngVxW85OELepofBn0c27oJNgdXPcyjI4vYwwz_P9TSdl59R1lxx1Y2VbvstPrWFqNe2cfPoibeWww_QW-tIe87jcm2urVIsr1OVsHLpuKNATVFrV6X160iaSeW6-1499307223421%7D";

    var mortRegInfoUrl = "/%7BErbGxngVxW85OELepofBn1GfwFTejg3e7kDG7slZXpuxQWdSdahDHfoh8OPinS6LKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223422%7D";

    var mortRegDetailInfoUrl = "/%7BErbGxngVxW85OELepofBn1GfwFTejg3e7kDG7slZXpv3FjvRGcg2iBuUmunDa5dcmMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223424%7D";

    var stakQualitInfoUrl = "/%7BErbGxngVxW85OELepofBn_Xrqlq1aLOukvlm4mSoZ5NjJdA0KLcYQJfcRZ8C2JaiMHNKYm7MvLK5k0BQOZWbiOBDsa5gIXWBEJJmjgMYZ8lp0LIQH7IBjnstPFsmx7p6-1499307223426%7D";

    var stakQualitDetailInfoUrl = "/%7BErbGxngVxW85OELepofBn_Xrqlq1aLOukvlm4mSoZ5P1CyG-4UDnRjY2WrucgwWQdZA0UEp1n3B3WoPy39VJvSBs58av3P1muYEFPH7iOPfkiQSMrTyKegRfs68Y0qc2-1499307223427%7D";

    var otherLicenceInfoUrl = "/%7BErbGxngVxW85OELepofBnxCsnzt-HjiFHQxBbyDqCLqxQWdSdahDHfoh8OPinS6LKHKLZEK2Zl0FYa-OlSa8rU6LE9GsjG_IT0jzm71JpVB56b9d3HzvpehdNy7ngTIN-1499307223428%7D";

    var otherLicenceDetailInfoUrl = "/%7BErbGxngVxW85OELepofBnxCsnzt-HjiFHQxBbyDqCLp5jOF9OBEQYZHJ6NfHVtrlmMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223429%7D"

    var assistUrl = "/%7BP7XEJiVXI6PAQQMH1LuIhDKp_15rY74EGj0tpci8IPx1kDRQSnWfcHdag_Lf1Um9IGznxq_c_Wa5gQU8fuI49-SJBIytPIp6BF-zrxjSpzY-1499307223430%7D"

    var InsStockAlterModelUrl = "/%7BErbGxngVxW85OELepofBn79iq1_D4rZq41V3NHDdq03J37C8RGtTVJ7a5BWVpmulKMjffsyLNyeGx2hlzr3tbMIV3_Mv5tj68wnG9enYz3bpcomMAuUkYlICI3-GorA4-1499307223431%7D"

    var shareHolderAll = "/%7BErbGxngVxW85OELepofBn8Bo5QNUhXsQ92UwgIOgfkllOHExMk0fqwBk33CFMYuLMHNKYm7MvLK5k0BQOZWbiOBDsa5gIXWBEJJmjgMYZ8k4G3bXFdVGD1kM1A-xhvUD-1499307223432%7D"

    var alterAllUrl = "/%7BErbGxngVxW85OELepofBn1TN7uTTiVA1it5cuggzjv8pXNGxA2BDf6SL4JW34-59vewt0ONLgxDpOl6r0uwd8opkIni8ATpacY6962JLRLJER9CWjikJW6fwE5MS-c-3-1499307223433%7D"

    var licenceAllUrl = "/%7BErbGxngVxW85OELepofBn47Pz6Wn4VBnJiDSiKNN364OVzdfex6K0fNJrD_AeTs40_c7H4RHkU3XuZvgGbrkWRmrsh7beB6E8rv9nLR7a1AKP8CJtTeLQcTuyDvq59Mb-1499307223434%7D"

    var branchAllUrl = "/%7BErbGxngVxW85OELepofBn_yaSE6qiEGBFGWXL4Z6Yvqn6pYSVegyd32GCZ_83YeAM28zif_oL7E1vMQs9RKilwRgN0nLcvt9VvoLziITy1SF2VbXAmYD_-FYGI1ezLuCRZRdMywyDKbZyvxapp-_wg-1499307223418%7D"

    var punishmentAllUrl = "/%7BErbGxngVxW85OELepofBn7i9MfuI7GTA-qoGifnPpdED7L24K9E2DelissJcIEW76pGlDsnPjtyGX9roKXEasK8W3r99qIKk3H5eb0-uvorZsMedPN-qWOpWuOJuP5gX-1499307223437%7D"

    var StakqualitAllUrl = "/%7BErbGxngVxW85OELepofBny3MOSAAoNtDwaipmkqe1S7_0WC5aIaCJVoOOzS7tk9CsymXYd8H72eDg35q6f-DxRmhLiPMUqnh9K5bukLtZswi5WPvyvGMoZ_Lj2c89GvZ-1499307223440%7D"

    var MortregAllUrl = "/%7BErbGxngVxW85OELepofBnxvr_2WpuswI25pX0ybg56YmDIgxR8WlAeuUjzMVEXsf0_c7H4RHkU3XuZvgGbrkWRmrsh7beB6E8rv9nLR7a1AKP8CJtTeLQcTuyDvq59Mb-1499307223441%7D"
    
    var toSimpleCancelInfoAndObjectionUrl = "/%7BOv3ZCskvFoLdz_L62OUwncKudzRVxLMzL09vMKrDaifmIs79BsBkht3etiBLarJXmMHZagEwzsN7WmWysUuaNWtSa8m21bKYXchrEoFb7x7PdMf_2lVT76IEczQ9dapa-1499307223442%7D"

    var simpleCancelUrl = "/%7BErbGxngVxW85OELepofBn9wKayeF7wiL-jgM0hnO3_6SzTfIEb4MKlwpN3XNB5iS6pGlDsnPjtyGX9roKXEasK8W3r99qIKk3H5eb0-uvooz_-gxIpeJuBL7RG3q7cfT-1499307223444%7D";
   
</script></div>
<div class="container1">

    <input type="hidden" id="entType" value="16">
    <input type="hidden" id="newTab" value="all" >
    
    <div class="summary"></div>
    <div class="result">
<div class="mainform row-fluid detailsOops licence_alter" id="licence_alter" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
        <p class="detail-title">行政许可变更详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('licence_alter').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div  style="height: auto;position: relative;width: 900px;">
	<div id="onemortgage_alter_info" class="classify" style="margin:20px auto auto 7px;">行政许可变更信息</div> 
    <table  cellspacing="0" class="item2">
        <tr>
            <th class="title">变更事项</th>
            <th class="title">变更时间</th>
            <th class="title">变更前内容</th>
            <th class="title">变更后内容</th>

        </tr>
        <tr class="">
            <td class="entry" id="licence_alter_alt"></td>
            <td class="entry" id="licence_alter_altDate"></td>
            <td class="entry" id="licence_alter_altBe"></td>
            <td class="entry" id="licence_alter_altAf"></td>                        
        </tr>    
    </table>
    </div>
</div><div class="mainform row-fluid detailsOops licence_alter" id="licence_alter_invalidation" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
        <p class="detail-title">其它无效详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('licence_alter_invalidation').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
   	</div>
	<div  style="height: auto;position: relative;width: 900px;">
	<div id="onemortgage_alter_info" class="classify" style="margin:20px auto auto 7px;">其他无效信息</div> 
    <table  cellspacing="0" class="item2">
        <tr>
            <th class="title" style="width:30%">无效日期</th>
            <td class="entry" id="licence_alter_invalidDate"></td>  
        </tr>
        <tr>
            <th class="title" style="width:30%">无效原因</th>
            <td class="entry" id="licence_alter_invalidRea"></td>                      
        </tr>    

    </table>
    </div>
 </div><div class="mainform row-fluid detailsOops shareholders_details" id="shareholders_details" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('shareholders_details').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
        <p class="detail-title">股东及出资详细信息</p>
	</div>    
	<div style="height: auto;position: relative;">  
	<div id="onemortgage_alter_info" class="classify" style="margin:20px auto auto 7px;" >股东信息</div> 
	<table  cellspacing="0" class="item2" id="shareholders_details_table">
      <tr  class="test1">
        <th class="title" style="width:50%">股东名称</th>
        <td id="shareholders_details_inv"></td>
      </tr>
      <tr class="test1">
        <th class="title" style="width:50%">认缴额（万元）</th>
        <td id="shareholders_details_liSubConAm"></td>
      </tr>
      <tr class="test1">
        <th class="title" style="width:50%">实缴额（万元）</th>
        <td id="shareholders_details_liAcConAm"></td>
      </tr>
    </table>

    <div id="onemortgage_alter_info2" class="classify" style="margin:20px auto auto 7px;" >认缴明细信息</div> 
    <table  cellspacing="0" class="item2">
      <tr>
        <th class="title">认缴出资方式</th>
        <th class="title">认缴出资额(万元)</th>
        <th class="title">认缴出资日期</th>
      </tr>
   
      <tr class="test1" id="shareholders_details_sub">
       <!--
        <td class="entry" id="shareholders_details_subConForm_CN"></td>
        <td class="entry" id="shareholders_details_subConAm"></td>
        <td class="entry" id="shareholders_details_subConDate"></td>
         -->
      </tr>       
    </table>

    <div id="onemortgage_alter_info3" class="classify" style="margin:20px auto auto 7px;" >实缴明细信息</div> 
    <table  cellspacing="0" class="item2">

      <tr>
        <th class="title">实缴出资方式</th>
        <th class="title">实缴出资额(万元)</th>
        <th class="title">实缴出资日期</th>
      </tr>
      
      <tr class="test1" id="shareholders_details_paid">
     <!--
        <td class="entry" id="shareholders_details_conForm_CN"></td>
        <td class="entry" id="shareholders_details_acConAm"></td>
        <td class="entry" id="shareholders_details_conDate"></td>
      -->  
      </tr>
         
    </table>
    </div>
</div>	<div class="mainform2 row-fluid detailsOops mortgage_alter" id="mortgage_alter" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
        <p class="detail-title">动产抵押详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('mortgage_alter').style.display = 'none';$('.temp').remove();">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div style="height: 500px;position: relative;width: 913px;overflow-y: scroll;">  
	<div id="onemortgage_alter_info" class="classify" style="margin:20px auto auto 7px">动产抵押登记信息</div>     
   <table style="margin-top:10px;" cellspacing="0" class="item2" id="mortgage_alter_info">
        <tr>
            <th class="title">登记编号</th>
            <td class="entry" id="mortgage_alter_morRegCNO"></td>
            <th class="title">登记日期</th>
            <td class="entry" id="mortgage_alter_regiDate"></td>
        </tr> 
        <tr>
       	 	<th class="title">登记机关</th>
       	 	<td class="entry" id="mortgage_alter_RegOrg_CN"></td>	
       	 	<th class="title"></th>
            <td class="entry"></td>
        </tr>   
    </table>
    <div id="twoperson" class="classify" style="margin:20px auto auto 7px">抵押权人信息</div> 
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="person">
        <tr>
            <th class="title">序号</th>
            <th class="title">抵押权人名称</th>
            <th class="title">抵押权人证照类型</th>
            <th class="title">证照号码</th>
            <th class="title">住所地</th>
        </tr>
    </table>
    <div id="threepriClaSec" class="classify" style="margin:20px auto auto 7px">被担保主债权信息</div>
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="noPriClaSec">
    </table>
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="priClaSec">
        <tr>
	        <th class="title">种类</th>
	        <td class="entry" id="mortgage_alter_priClaSecKind_CN"></td>
	        <th class="title">数额</th>
	        <td class="entry" id="mortgage_alter_priClaSecAm"></td>
	    </tr>
	    <tr>
	    	<th class="title">担保的范围</th>
	        <td class="entry" id="mortgage_alter_warCov"></td>
	        <th class="title">债务人履行债务的期限</th>
	        <td class="entry" id="mortgage_alter_pefPerForm"></td>
	    </tr>
	    <tr class="" >
	        <th class="title">备注</th>
	        <td class="entry" id="mortgage_alter_cremark"></td>
	    </tr>
    </table>
	<div id="fourmortGuaranteeInfo" class="classify" style="margin:20px auto auto 7px"> 抵押物信息</div>
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="mortGuaranteeInfo">
        <tr>
            <th class="title">序号</th>
            <th class="title">抵押物名称</th>
            <th class="title">所有权或使用权归属</th>
            <th class="title">数量、质量、状况、所在地等情况</th>
            <th class="title">备注</th>
        </tr>
    </table>
    <div id="fivealt" class="classify" style="margin:20px auto auto 7px">变更信息</div>
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="alt">
        </tr>
        <tr>
            <th class="title">序号</th>
            <th class="title">变更日期</th>
            <th class="title">变更内容</th>
        </tr>
    </table>
    <div id="fivecancel" class="classify" style="margin:20px auto auto 7px">注销信息</div>
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="cancel">
        <tr>
            <th class="title">注销日期</th>
            <td class="entry" id="mortgage_alter_canDate"></td>
        </tr>
        <tr class="" id="cancelColumns">
            <th class="title">注销原因</th>
            <td class="entry" id="mortgage_alter_morCanRea_CN"></td>
        </tr>
    </table>
    <table style="margin-top:10px;" cellspacing="0" class="item2" id="cancel2">
    </table>
    </div>
</div>   <div class="mainform2 row-fluid detailsOops mortgage_alter" id="mortgage_alter2" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
		<p class="detail-title">动产抵押详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('mortgage_alter2').style.display = 'none';$('.temp').remove()">
			<img src="images/closeForDetail.png" />
		</p>
	</div> 
	<div style="height: 557px;position: relative;width: 913px;overflow-y: auto;">
	<div id="oneFormortgage" class="classify" style="margin:20px auto auto 7px">动产抵押登记信息</div>            
	<table  style="margin-top:10px;" cellspacing="0" class="item2" id="mortgage_alter_info2">
	    <tr>
	        <th class="title">登记编号</th>
	        <td class="entry" id="mortgage_alter_morRegCNO2"></td>
	        <th class="title">登记日期</th>
	        <td class="entry" id="mortgage_alter_regiDate2"></td>
	    </tr> 
	    <tr>
	   	 	<th class="title">登记机关</th>
	   	 	<td class="entry" id="mortgage_alter_RegOrg_CN2"></td>	
	   	 	<th class="title"></th>
	        <td class="entry"></td>
	    </tr>   
	</table>
	<div id="twoperson2" class="classify" style="margin:20px auto auto 7px">抵押权人信息</div> 
	<table style="margin-top:10px;"  cellspacing="0" class="item2" id="person2">
	    <tr>
	        <th class="title">序号</th>
	        <th class="title">抵押权人名称</th>
	        <th class="title">抵押权人证照类型</th>
	        <th class="title">证照号码</th>
	        <th class="title">住所地</th>
	    </tr>
	</table>
	<div id="threepriClaSec2" class="classify" style="margin:20px auto auto 7px">被担保主债权信息</div> 
	<table  style="margin-top:10px;" cellspacing="0" class="item2" id="priClaSec2">
	    <tr>
	        <th class="title">种类</th>
	        <td class="entry" id="mortgage_alter_priClaSecKind_CN2"></td>
	        <th class="title">数额</th>
	        <td class="entry" id="mortgage_alter_priClaSecAm2"></td>
	    </tr>
	    <tr>
	    	<th class="title">担保的范围</th>
	        <td class="entry" id="mortgage_alter_warCov2"></td>
	        <th class="title">债务人履行债务的期限</th>
	        <td class="entry" id="mortgage_alter_pefPerForm2"></td>
	    </tr>
	    <tr class="" id="priClaSecColumns">
	        <th class="title">备注</th>
	        <td class="entry" id="mortgage_alter_pefPerTo2"></td>
	    </tr>
	</table>
		<div id="fourmortGuaranteeInfo2" class="classify" style="margin:20px auto auto 7px"> 抵押物信息</div>
	<table style="margin-top:10px;" cellspacing="0" class="item2" id="mortGuaranteeInfo2">
	    <tr>
	        <th class="title">序号</th>
	        <th class="title">抵押物名称</th>
	        <th class="title">所有权或使用权归属</th>
	        <th class="title">数量、质量、状况、所在地等情况</th>
	        <th class="title">备注</th>
	    </tr>
	</table>
	<div id="fivealt2" class="classify" style="margin:20px auto auto 7px">变更信息</div>
	<table style="margin-top:10px;" cellspacing="0" class="item2" id="alt2">
	    <tr>
	        <th class="title">序号</th>
	        <th class="title">变更日期</th>
	        <th class="title">变更内容</th>
	    </tr>
	</table>
	</div>
</div>   <div class="mainform2 row-fluid detailsOops pledge_alter" id="pledge_alter" style="display: none; border-radius: 8px; z-index:1002">
	<div id="closeColumn">
        <p class="detail-title">股权出质详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('pledge_alter').style.display = 'none';$('.temp').remove();">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div id="pledge_alt_div" style="height: 155px;position: relative;width: 913px;overflow-y: scroll;">  
		<div class="classify" style="margin:20px auto auto 7px">股权出质变更信息</div>     
	   	<table style="margin-top:10px;" cellspacing="0" class="item2" id="pledge_alter_table">
	        <thead>
	        	<tr>
		            <th class="title" style="width:15%">序号</th>
		            <th class="title" style="width:20%">变更日期</th>
		            <th class="title" style="width:65%">变更内容</th>
	            </tr>
	        </thead>
	        <tbody>
		        <tr>
		       	 	<td class="title">登记机关</td>
		       	 	<td class="entry" id="mortgage_alter_RegOrg_CN"></td>	
		       	 	<td class="title"></td>
		        </tr>
	        </tbody> 
	    </table>
	</div>
	<div id="pledge_cancel_div" style="height: 155px;position: relative;width: 913px;overflow-y: scroll;">  
		<div class="classify" style="margin:20px auto auto 7px">股权出质注销信息</div>     
	   	<table style="margin-top:10px;" cellspacing="0" class="item2" id="pledge_cancel_table">
	        <tr>
	            <th class="title" style="width:15%">注销日期</th>
	            <td class="entry" style="width:85%;text-align:left;" id="pledge_cancel_date"></td>
	        </tr> 
	        <tr>
	       	 	<th class="title">注销原因</th>
	       	 	<td class="entry" id="pledge_cancel_rea" style="text-align:left"></td>	
	        </tr>   
	    </table>
	</div>
	<div id="pledge_revoke_div" style="height: 155px;position: relative;width: 913px;overflow-y: scroll;">  
		<div class="classify" style="margin:20px auto auto 7px">股权出质撤销信息</div>     
	   	<table style="margin-top:10px;" cellspacing="0" class="item2" id="pledge_revoke_table">
	        <tr>
	            <th class="title" style="width:15%">撤销日期</th>
	            <td class="entry" style="width:85%;text-align:left;" id="pledge_revoke_date"></td>
	        </tr> 
	        <tr>
	       	 	<th class="title">撤销原因</th>
	       	 	<td class="entry" id="pledge_revoke_rea" style="text-align:left"></td>	
	        </tr>   
	    </table>
	</div>
</div><div class="mainform2 row-fluid detailsOops holder_alter" id="holder_alter" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
        <p class="detail-title">股权出质变更详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('holder_alter').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div style="height: auto;position: relative;width: 900px;">
	<div style="margin-top:10px;" class="classify" style="margin:20px auto auto 6px">股权出质变更信息</div>
    <table  cellspacing="0" class="item2">
        <tr>
            <th class="title">变更时间</th>
            <th class="title">变更内容</th>

        </tr>
        <tr class="">
            <td class="entry" id="holder_alter_altDate"></td>
            <td class="entry" id="holder_alter_alt"></td>
        </tr>    
    </table>
    </div>
</div>    <div class="mainform2 row-fluid detailsOops holder_alter" id="holder_alter2"  style="display: none; border-radius: 8px;">
   <div id="closeColumn">
      <p class="detail-title">股权出质注销详细信息</p>
   		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('holder_alter2').style.display = 'none'">
   			<img src="images/closeForDetail.png"></img>
   		</p>
   	</div>
   	<div style="height: auto;position: relative;width: 900px;">
   	<div style="margin-top:10px;" class="classify" style="margin:20px auto auto 6px">股权出质注销信息</div>
    <table  cellspacing="0" class="item2">
        <tr>
            <th class="title">注销时间</th>
            <th class="title">注销原因</th>

        </tr>
        <tr class="">
            <td class="entry" id="holder_alter_canDate"></td>
            <td class="entry" id="holder_alter_equPleCanRea"></td>
        </tr>    
    </table>
    </div> 
</div>    <div class="mainform2 row-fluid detailsOops holder_alter" id="holder_alter3"  style="display: none; border-radius: 8px;">
	<div id="closeColumn">
        <p class="detail-title">股权出质撤销详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('holder_alter3').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div style="height: auto;position: relative;width: 900px;">
   	<div style="margin-top:10px;" class="classify" style="margin:20px auto auto 6px">股权出质撤销信息</div>
    <table  cellspacing="0" class="item2">
        <tr>
            <th class="title">撤销时间</th>
            <th class="title">撤销原因</th>

        </tr>
        <tr class="">
            <td class="entry" id="holder_alter_cancelDate"></td>
            <td class="entry" id="holder_alter_cancelRea"></td>
        </tr>    
    </table>
    </div>
</div>       <div class="mainform row-fluid detailsOops freeze_detail" id = "freeze_detail_continuation">
      <div id="closeColumn">
        <p class="detail-title">司法协助详细信息</p>
	   	<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('freeze_detail_continuation').style.display = 'none'">
	   		<img src="images/closeForDetail.png"></img>
	   	</p>
	   </div>
     <table  cellspacing="0" class="item2">
         <tr>
             <th class="title textcenter" colspan="12">冻结情况</th>
         </tr>
         <tr>
             <th class="title">执行法院</th>
             <th class="title">执行事项</th>
             <th class="title">执行裁定书文号</th>
             <th class="title">执行通知书文号</th>
             <th class="title">被执行人</th>
             <th class="title">被执行人持有股权、其它投资权益的数额</th>
             <th class="title">被执行人证件种类</th>
             <th class="title">被执行人证件号码</th>
             <th class="title">冻结期限自</th>
             <th class="title">冻结期限至</th>
              <th class="title">冻结期限</th>
             <th class="title">公示日期</th>
         </tr>

     </table>
     <table  cellspacing="0" class="item2">
         <tr>
             <th class="title textcenter" colspan="10">续行冻结情况</th>
         </tr>
         <tr>
             <th class="title">执行法院</th>
             <th class="title">执行事项</th>
             <th class="title">执行裁定书文号</th>
             <th class="title">执行通知书文号</th>
             <th class="title">被执行人</th>
             <th class="title">被执行人持有股权、其它投资权益的数额</th>
             <th class="title">被执行人证件种类</th>
             <th class="title">被执行人证件号码</th>
             <th class="title">解除冻结日期</th>
             <th class="title">公示日期</th>
         </tr>
     </table>
        
    </div>   <div class="mainform row-fluid detailsOops freeze_detail" id = "freeze_detail_invalid">
     <div id="closeColumn">
        <p class="detail-title">司法协助详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('freeze_detail_invalid').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	 </div>
     <table  cellspacing="0" class="item2">
         <tr>
             <th class="title textcenter" colspan="12">冻结情况</th>
         </tr>
         <tr>
             <th class="title">执行法院</th>
             <th class="title">执行事项</th>
             <th class="title">执行裁定书文号</th>
             <th class="title">执行通知书文号</th>
             <th class="title">被执行人</th>
             <th class="title">被执行人持有股权、其它投资权益的数额</th>
             <th class="title">被执行人证件种类</th>
             <th class="title">被执行人证件号码</th>
             <th class="title">冻结期限自</th>
             <th class="title">冻结期限至</th>
             <th class="title">冻结期限</th>
             <th class="title">公示日期</th>
         </tr>
     </table>
     <table  cellspacing="0" class="item2">
         <tr>
             <th class="title textcenter" colspan="2">失效情况</th>
         </tr>
         <tr>
             <th class="title">失效原因</th>
             <th class="title">失效时间</th>
         </tr> 
     </table>
    </div><div class="mainform row-fluid detailsOops freeze_detail" id = "freeze_detail_only">
	<div id="closeColumn">
        <p class="detail-title">司法协助详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('freeze_detail_only').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
     <table  cellspacing="0" class="item2">
         <tr>
             <th class="title textcenter" colspan="4">冻结情况</th>
         </tr>
         <tr>
             <th class="title">执行法院</th>
             <td class="entry" id="freeze_detail_froAuth"></td>
             <th class="title">执行事项</th>
             <td class="entry" id="freeze_detail_executeItem_CN"></td>
         </tr>
         <tr>
             <th class="title">执行裁定书文号</th>
             <td class="entry" id="freeze_detail_froDocNo"></td>
             <th class="title">执行通知书文号</th>
             <td class="entry" id="freeze_detail_executeNo"></td>
         </tr>
         <tr>
             <th class="title">被执行人</th>
             <td class="entry" id="freeze_detail_inv"></td>
             <th class="title">被执行人持有股权、其它投资权益的数额</th>
             <td class="entry" id="freeze_detail_froAm"></td>
         </tr>
         <tr>
             <th class="title">被执行人证件种类</th>
             <td class="entry" id="freeze_detail_cerType_CN"></td>
             <th class="title">被执行人证件号码</th>
             <td class="entry" id="freeze_detail_cerNo"></td>
         </tr>
         <tr>
             <th class="title">冻结期限自</th>
             <td class="entry" id="freeze_detail_froFrom"></td>
             <th class="title">冻结期限至</th>
             <td class="entry" id="freeze_detail_froTo"></td>
         </tr>
         <tr>
             <th class="title">冻结期限</th>
             <td class="entry" id="freeze_detail_frozDeadline"></td>
             <th class="title">公示日期</th>
             <td class="entry" id="freeze_detail_publicDate"></td>
         </tr>    
     </table>
    </div><div class="mainform row-fluid detailsOops freeze_detail" id = "freeze_detail">
	<div id="closeColumn">
        <p class="detail-title">司法协助详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('freeze_detail').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div class="detail-info-container">
	 <div id="one" class="classify" style="margin:20px auto auto 6px">冻结情况</div>
     <table style="margin-top:10px;" cellspacing="0" class="item2" id="baseDetailCancel">
        <col style="width:222px"></col> 
     	<col style="width:222px"></col> 
		<col style="width:222px"></col> 
		<col></col> 
         <tr id="froAuthAndThing">

         </tr>
         <tr id="NumAndfroDocNo">
         
         </tr>
         <tr id="bePerson">
         
         </tr>    
         <tr id="cardTypeOne">
         
         </tr>    
         <tr id="congeal">
         
         </tr>   
         <tr id="congealAndDate">   

         </tr>
     </table>
     <div id="two" class="classify" style="margin:20px auto auto 6px">续行冻结情况</div>
      <table style="margin-top:10px;" cellspacing="0" class="item2" id="continuation">
      <col style="width:222px"></col> 
     	<col style="width:222px"></col> 
		<col style="width:222px"></col> 
		<col></col> 
         <tr id="froAuth">
         
         </tr>
         <tr id="froDocNo">
         
         </tr>
		 <tr id="inv">
		 
		 </tr>
		 <tr id="cardType">
		 
		 </tr>
		 <tr id="dateFrom">
		 </tr>
		 <tr id="publicDate">

         </tr>
     </table>
     <div id="three" class="classify" style="margin:20px auto auto 6px">解冻情况</div>
     <table style="margin-top:10px;" cellspacing="0" class="item2" id="freezeCancelInfo">
		<col style="width:222px"></col> 
     	<col style="width:222px"></col> 
		<col style="width:222px"></col> 
		<col></col> 
         <tr id="froAuthThree">
         
         </tr>
         <tr id="cardNumThree">
         
         </tr>
         <tr id="personThree">
         
         </tr>
         <tr id="cardTypeThree">
         
         </tr>
         <tr id="conDateThree">

         </tr>  
     </table>
      <div id="four" class="classify" style="margin:20px auto auto 6px">失效原因</div>
       <table  style="margin-top:10px;" cellspacing="0" class="item2" id="invalid">
       <col style="width:222px"></col> 
     	<col style="width:222px"></col> 
		<col style="width:222px"></col> 
		<col></col> 
         <tr id="reson">
             
         </tr>
         <tr id="time">
             
         </tr> 
     </table>
     </div>
    </div>	<div class="mainform row-fluid detailsOops copyright_alter" id="copyright_alter">
   <div id="closeColumn">
   	<p class="detail-title">股权变更详细信息</p>
   	<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('copyright_alter').style.display = 'none'">
   		<img src="images/closeForDetail.png"></img>
   		</p>
   	</div>
   	<div class="detail-info-container">
   	<div  class="classify" style="margin:20px auto auto 6px">股权变更信息</div>
	<table style="margin-top:10px;" cellspacing="0" class="item2">
	 <col style="width:222px"></col> 
     	<col style="width:222px"></col> 
		<col style="width:222px"></col> 
		<col></col> 
	<tr>
		<th class="title">执行法院</th>
		<td class="entry" id="copyright_alter_froAuth"></td>
		<th class="title">执行事项</th>
		<td class="entry" id="copyright_alter_thing"></td>
	</tr>
	<tr>
		<th class="title">执行裁定书文号</th>
		<td class="entry" id="copyright_alter_froDocNo"></td>
		<th class="title">执行通知书文号</th>
		<td class="entry" id="copyright_alter_executeNo"></td>	
	</tr>
	<tr>
			<th class="title">被执行人</th>
			<td class="entry" id="copyright_alter_inv"></td>
			<th class="title">被执行人持有股权数额</th>
			<td class="entry" id="copyright_alter_froAm"></td>
	</tr>
	<tr>
			<th class="title">被执行人证照种类</th>
			<td class="entry" id="copyright_alter_invCerType_CN"></td>
		<th class="title">被执行人证照号码</th>
		<td class="entry" id="copyright_alter_invCerNo"></td>

	</tr>
	<tr>
		<th class="title">受让人</th>
		<td class="entry" id="copyright_alter_Alien"></td>
		<th class="title">协助执行日期</th>
		<td class="entry" id="copyright_alter_executeDate"></td>
	</tr>
	<tr>
		<th class="title">受让人证照种类</th>
		<td class="entry" id="copyright_alter_AlienCerType_CN"></td>
		<th class="title">受让人证照号码</th>		
		<td class="entry" id="copyright_alter_alienCerNo"></td>
	</tr>    
	<tr>

	</tr>
	</table>
	</div>
</div>        <div class="page">


<div class="mask" id="mask"></div>
 <div class="nameBox  clearfix">
            <div class="companyDetail clearfix">
            <div class="companyName">
			                         <h1 class="fullName">
			                          			                                  <dd class="result" title="仙桃市灵成百货经营部">仙桃市灵成百货经营部</dd>
			                         </h1>
			                         	<span class="companyStatus" title="存续（在营、开业、在册）">存续（在营、开业、在册）</span>
			                     <span class="status"></span>
						</div>
						<span class="regNum_inner">
			                <i class="abs fa fa-map1" aria-hidden="true"></i> 
                           统一社会信用代码：<span class="nameBoxColor">92429004MA4C8HHT0U</span>  
			            </span>
			            
			             
			             
			             		<span class="owner"><i class="abs fa fa-user1" aria-hidden="true"></i>经营者：<span class="nameBoxColor">李秀雯</span>
			                     </span>
				              	 <span class="regNum_inner">
				            		 <i class="abs fa fa-map-marker1" aria-hidden="true"></i>登记机关： <span class="nameBoxColor">仙桃市工商行政管理局经济开发区工商所</span>             
				                 </span>
				             <span class="regNum_inner">
				                 <i class="abs fa fa-info-circle1" aria-hidden="true"></i>成立日期 : <span class="nameBoxColor">2017年06月30日</span>
			                 </span>
			                 
                 			<input type="hidden" id="subsites" value="100000">
		                    <input type="hidden" id="prip" value="">
		                    <input type="hidden" id="scId" value="">
				                 
			             </div>
			             <div class="button-box r">
								<a href="javascript:void(0)" id="btn_send_pdf" class="bt1 tc wh">发送报告</a>
								<a href="javascript:void(0)" id="btn_share"  class="bt2 tc wh">信息分享</a>
								<a href="javascript:void(0)" id="btn_print" class="bt3 tc wh">信息打印</a>
								<div style="display:none">
									<form name="f" id="f-form" action="/%7BErbGxngVxW85OELepofBn7QPNDFPlzN4WkoXCDbeemKaOTyfwU0Fi2-QLWJbTZdGZOK8cxLJpuZBJJ_IJ_uu3y5X-QgxQL9Cxd8H7t7N2jYEXDFlDQqjbxauVNimLdvi-1499307223321%7D" method="post">
										<button id="pop-captcha-print" type="button" style="display: none;"></button>
										<div id="popup-captcha-print-div"></div>
									</form>
									
									<button id="pop-captcha-share" type="button" style="display: none;"></button>
									<div id="popup-captcha-share-div" style="display: none;"></div>
									
									<button id="pop-captcha-pdf" type="button" style="display: none;"></button>
									<div id="popup-captcha-pdf-div" style="display: none;"></div>
								</div>
							</div>
				</div>
<div class="mainform row-fluid send_pdf_dialog_ops shareholders_details" id="send_pdf_dialog" style="display: none; border-radius: 8px;">
	<div id="closeColumn" style="height:36px;border-bottom: 1px solid #999;width: 370px;margin-left: 0px;background-color:#d5b661;color:#fff;">
		<p style="float:left;margin-top:8px;margin-left:20px;">提示</p>
	</div>    
	<div style="height: auto;position: relative;width: 370px;">  
	<div style="margin:20px auto auto 7px;margin-left: 25px;" >请输入您的邮箱</div>
	<div style="margin:20px auto auto 7px;color: red; text-align:center;" id="message" ></div>
	<div style="margin-top:20px;text-align:center"><input type="text" id="email_input" style="width:210px;height:30px;border:1px solid #A9A9A9;margin-left: auto;margin-right:auto;border-radius: 4px;"></div>
	<div style="color:#fff;margin-top:20px;">
		<div onclick="sendPdf();" style="cursor:pointer;width:87px;height:27px;background-color:#d5b661;float:left;margin-left:80px;text-align:center;padding-top:3px;border-radius: 4px;">确定</div>
		<div onclick="document.getElementById('bg').style.display ='none';document.getElementById('send_pdf_dialog').style.display = 'none'" style="border-radius: 4px;cursor:pointer;width:87px;height:27px;background-color:#d5b661;margin-left:36px;float:left;text-align:center;padding-top:3px;">取消</div>
	</div>
	<script>
	function sendPdf() {
		var email = $('#email_input').val();
	//	if (email.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/) != -1) {
	    if (email.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9_-]+((\.|-)[A-Za-z0-9_-]+)*\.[A-Za-z0-9_-]+$/) != -1) {
			document.getElementById('bg').style.display ='none';
			document.getElementById('send_pdf_dialog').style.display = 'none';
			var geetest_challenge = $("#popup-captcha-pdf-div").find(".geetest_challenge").val();
			var geetest_validate = $("#popup-captcha-pdf-div").find(".geetest_validate").val();
			var geetest_seccode = $("#popup-captcha-pdf-div").find(".geetest_seccode").val();
			$.post("/%7BErbGxngVxW85OELepofBn_Cw4Ol_xBS4hoOf7RASurl1kDRQSnWfcHdag_Lf1Um9IGznxq_c_Wa5gQU8fuI49648E7Bm3Zgrae7lLDLYXzBwOlCM9Mw6nm83AQZelpkshZUsuPODqYqjeGar9I76KhuiJ5wDq3d06_ny-5mz5Zc-1499307223322%7D", {email: email, geetest_challenge: geetest_challenge, geetest_validate: geetest_validate, geetest_seccode: geetest_seccode}, function(result){
				alert(result);
			});
		} else {
			$("#message").text("邮箱不正确");
		}
	}
	</script>
    </div>
</div>	

<div class="mainform row-fluid share_dialog_ops shareholders_details" id="share_dialog" style="display: none; border-radius: 8px;">
	<div id="closeColumn" style="height:36px;border-bottom: 1px solid #999;width: 300px;margin-left: 0px;background-color:#d5b661;color:#fff;">
		<p style="float:left;margin-top:8px;margin-left:20px;">信息分享</p>
		<p onclick="document.getElementById('bg').style.display ='none';document.getElementById('share_dialog').style.display = 'none'" style="float:right;margin-top:8px;margin-right:20px;cursor:pointer;">X</p>
	</div>    
	<div style="height: auto;position: relative;width: 300px;">
		<div style="margin-left:70px;margin-right:70px;margin-top:20px;margin-bottom:-14px;">
		<div class="bdsharebuttonbox"><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a><a href="#" class="bds_sqq" data-cmd="sqq" title="分享到QQ好友"></a></div>
<script>var keywords = encodeURI("仙桃市灵成百货经营部");var domain = document.domain;window._bd_share_config={"common":{"bdUrl":window.location.href,"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='/js/share/share.js'];</script>
    	</div>
    </div>
</div>	
            <div class="content">

<div class="menu">
    <div class='menu-i'>
	    <span id="tab_primary1" class="">
	          基础信息
	   	</span>
	    <div style="height:16px;width:1px;position:absolute; right:1px;background:#ccc; top: 9px">
	    </div>      
	</div>
	<div class='menu-i'>
	   <span id="tab_primary2" class="">
	          行政许可信息
	   	</span>
	    <div style="height:16px;width:1px;position:absolute; right:1px;background:#ccc; top: 9px">
	    </div>      
	</div>
	<div class='menu-i'>
	    <span id="tab_primary3" class="">
	          行政处罚信息
	   	</span>
	    <div style="height:16px;width:1px;position:absolute; right:1px;background:#ccc; top: 9px">
	    </div>      
	</div>
	<div class='menu-i'>
	        <span id="tab_primary4" class="">
	          经营异常信息
	   	</span>
	    <div style="height:16px;width:1px;position:absolute; right:1px;background:#ccc; top: 9px">
	    </div>      
	</div>
	<div  class='menu-i'>
	   <span id="tab_primary5" class="" style="display:none;">
	          列入严重违法失信企业名单（黑名单）信息
	   	</span>  
	</div>          
</div>                
                <div id="bg"></div>
               
                <div class='content-i' id="content1" style="display:block">
                    <div class='wrap' id='wrap-base'>
			             			         


			         
			        
			       
			         			       
			        
			        
			        
			             <div id="primaryInfo" class="tabin mainContent">
			                 <div class="details clearfix">
			                     <div class="classify">营业执照信息</div>

			                     <div class="overview">
			                         <dl>			                      			                             
			                              	<dt class="item"> 统一社会信用代码：</dt>
			                              	<dd class="result">92429004MA4C8HHT0U</dd>
			                     	</dl>
				                 <dl>
			                         <dt class="item_right">名称：</dt>
			                         <dd class="result" title="仙桃市灵成百货经营部">仙桃市灵成百货经营部</dd>
			                     </dl>
			                     <dl>
			                         <dt class="item">类型：</dt>
			                         <dd class="result">个体工商户</dd>
			                     </dl>
				                 <dl>
			                         <dt class="item_right">经营者：</dt>
			                         <dd class="result">李秀雯</dd>
			                     </dl>
			                     <dl>
			                         <dt class="item">组成形式：</dt>
			                         <dd class="result">个人经营
			                     </dd>
			                     </dl>
				                 <dl>
			                     <dt class="item_right">注册日期：</dt>
			                     <dd class="result">2017年06月30日</dd>
			                 </dl>
			                 <dl>
			                     <dt class="item">登记机关：</dt>
			                     <dd class="result">仙桃市工商行政管理局经济开发区工商所</dd>
			                 </dl>
			                 <dl>
			                     <dt class="item_right">核准日期：</dt>
			                     <dd class="result">2017年06月30日</dd>
			                 </dl>
			                 <dl class="item info-dl all">
			                     <dt class="item_right">登记状态：</dt>
			                     <dd class="result">存续（在营、开业、在册）</dd>
			                 </dl>
			                 <dl class="item info-dl all">
			                     <dt class="item">经营场所：</dt>
			                     <dd class="result" title="仙桃市工业园区铁匠湾社区还建房40号">仙桃市工业园区铁匠湾社区还建房40号</dd>
			                 </dl>
			                 <dl class="item info-dl all">
			                 <dt class="item">经营范围：</dt>
			                 <dd class="result">日用百货零售。</dd>
			             </dl>
			             </div>

			         </div>
			        
			        
</div></div>
                    <div class='wrap' id='wrap-shareholder'><div id="holderInfo" class="holderInfo">

</div></div>
                    <div class='wrap' id='wrap-keyperson'>

</div>
                    <div class='wrap' id='wrap-branch'></div>
                    <div class='wrap' id='wrap-clear'></div>
                    <div class='wrap' id='wrap-alter'><div id="changeInfo" class="changeInfo">
    <div class="classify" id="alterInfoAll">
        变更信息
    </div>
    <table class="display" id="altInfo">
        <thead>
        <tr>
            <th width="6%">序号</th>
            <th width="22%">变更事项</th>
            <th>变更前内容</th>
            <th>变更后内容</th>
            <th width="13%">变更日期</th>
        </tr>
        </thead>

    </table>
</div></div>
                    <div class='wrap' id='wrap-mort'><div class="other_dcdy">
    <div class="classify" id="mortregInfoAll">
        动产抵押登记信息
    </div>
    <table class="display" id="needPaging_guaranty" >
        <thead>
        <tr>
            <th width="6%">序号</th>
            <th>登记编号</th>
            <th width="13%">登记日期</th>
            <th>登记机关</th>
            <th width="10%">被担保债权数额</th>
            <th width="6%">状态</th>
            <th width="13%">公示日期</th>
            <th width="6%">详情</th>
        </tr>
        </thead>

    </table>
</div></div>
                    <div class='wrap' id='wrap-stock'></div>
                    <div class="wrap" id='wrap-copyright'>
<div class="baseinfo_copyright">


    <div id="bg"></div>
    <div class="classify">
        知识产权出质登记信息
    </div>
    <table class="display" id="copyright_baseinfo" style="width:100%">
        <thead>
            <tr>
                <th width="5%">序号</th>
                <th width="13%">知识产权登记证号</th>
                <th>名称</th>
                <th width="8%">种类</th>
                <th>出质人名称</th>
                <th>质权人名称</th>
                <th width="13%">质权登记期限</th>
                <th width="6%">状态</th>
                <th width="13%">公示日期</th>
                <th width="5%">详情</th>
            </tr>
        </thead>
    </table>
</div>
</div>
                    <div class='wrap' id='wrap-trademark'><div id="trademark" class="trademark">
    <div class="classify rel">商标注册信息
        <span class="trademarkCount"><span id="trademarkCount"></span><a></a></span>
    </div>
    <div id="trademarkInfo" class="clearfix">
        <ul class="trademark-list" id="trademark-list">
        </ul>
    </div>
</div></div>
                    <div class='wrap' id='wrap-check'><div class="warning_inspect">
    <div class="classify">
        抽查检查结果信息
    </div>
    <table class="display" id="needPaging_inspect" >
        <thead>
        <tr>
            <th width="6%">序号</th>
            <th>检查实施机关</th>
            <th>类型</th>
            <th width="13%">日期</th>
            <th>结果</th>
        </tr>
        </thead>

    </table>
</div></div>
                    <div class='wrap' id='wrap-assist'></div>
                    <div class='biaoshi' style="width:100%;height:1px;"></div>
                    <div class='annual-tishi'>以下信息由该企业提供，企业对其报送信息的真实性、合法性负责</div>
                    <div class='wrap' id='wrap-annualreport'><div id="annual_menu" class="annual_menu">
    <div class="classify" id="annual_menuAll">
            个体户年报信息
    </div>
    <table class="display" id="annual_menu_table">
        <thead>
        <tr>
            <th width="7%">序号</th>
            <th>报送年度</th>
            <th>公示日期</th>
            <th width="15%">详情</th>
        </tr>
        </thead>
        <tbody></tbody>
    </table>
</div></div>
                    <div class='wrap' id='wrap-instant'><div id="instantInfo">




<div class="mainform row-fluid detailsOops ins_intellectual_detail" id="ins_intellectual_detail">
<div id="closeColumn">
    <span class="detail-title">知识产权出质详细信息</span>
   	<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('ins_intellectual_detail').style.display = 'none'">
   		<img src="images/closeForDetail.png"></img>
   		</p>
   	</div>
   		<div class="detail-info-container">
   					<div  class="classify" style="margin:20px auto auto 7px;" id="knowlage1">知识产权出质登记变更信息</div>
                     <table style="margin-top:10px;" cellspacing="0" class="item2" id="ins_ImKlp_detailInfo">

                     </table>
                     
                     
                     <div  class="classify" style="margin:20px auto auto 7px;" id="knowlageConDate1">注销信息</div>
                     <table style="margin-top:10px;" cellspacing="0" class="item2" id="ins_ImKlp_detailInfoLayout">
                        <col style="width:222px"></col> 
                        <col style="width:222px"></col> 
                        <col style="width:222px"></col> 
                        <col></col>
                         <tr>
                             <th class="title">注销日期</th>
                             <td class="entry" id="ins_ImKlp_detail_EquDate"></td>
                         </tr>
                         <tr>
                             <th class="title">注销原因</th>
                             <td class="entry" id="ins_ImKlp_detail_EquRes"></td>
                         </tr>
                     </table>
                     
                      <div  class="classify" style="margin:20px auto auto 7px;" id="knowlageNoUse1">其他无效信息</div>
                     <table style="margin-top:10px;" cellspacing="0" class="item2" id="ins_ImKlp_detailInfoOther">
                          <col style="width:222px"></col> 
                          <col style="width:222px"></col> 
                          <col style="width:222px"></col> 
                          <col></col>
                         <tr>
                             <th class="title">其他无效日期</th>
                             <td class="entry" id="ins_ImKlp_detail_InvDate"></td>
                         </tr>
                         <tr>
                             <th class="title">其他无效原因</th>
                             <td class="entry" id="ins_ImKlp_detail_InvRes"></td>
                         </tr>
                     </table>
      </div>
</div>
</div></div>
                    <div class='wrap' id='wrap-simplecancer'></div> 
                    <div id="footer_ac"></div>
                    <div onclick="clickToAddmore()" id="addmore">
                    	<div class="center_line"></div>
                    	<div class="addmore_drop">点击或下拉加载更多信息</div>
                    </div>
                </div>
               
                <div class='content-i' id="content2" style="display:none"><div id="other_licensing" class="other_licensing">
    <div class="classify" id="liceInfoAll">
        行政许可信息<i class="arrow"></i>
    </div>
    <table class="display mytable" id="needPaging_otherLicensing" style="width:auto">
        <thead>
        <tr>
            <th style="padding: 0">
                <div class="specialfuckth">
                    <table frame='void' rules='rows' width="1070px;">
                        <thead>
                        <tr>
                            <th width="44px">序号</th>
                            <th class="sorting_disabled" width="131px">许可文件编号</th>
                            <th class="sorting_disabled" width="132px">许可文件名称</th>
                            <th class="sorting_disabled" width="100px">有效期自</th>
                            <th class="sorting_disabled" width="100px">有效期至</th>
                            <th class="sorting_disabled" width="140px">许可机关</th>
                            <th class="sorting_disabled" width="150px">许可内容</th>
                        </tr>
                        </thead>
                    </table>
                </div>
            </th>

        </tr>
        </thead>
    </table>
</div></div>

                
                <div class='content-i' id="content3" style="display: none">
    <div class="warning_punish">
    <div class="mainform row-fluid detailsOops punish_detail" id="punish_detail" style="display: none; border-radius: 8px;">
	<div id="closeColumn">
        <p class="detail-title">行政处罚详细信息</p>
		<p class="closeOops" onclick="document.getElementById('bg').style.display ='none';document.getElementById('punish_detail').style.display = 'none'">
			<img src="images/closeForDetail.png"></img>
		</p>
	</div>
	<div style="height: auto;position: relative;">
   <div  class="classify" style="margin:20px auto auto 7px;">详情摘要</div>     
     <table style="margin-top:10px;" cellspacing="0" class="item2">
         <tr>
             <th class="title" style="width:33.33%">行政处罚决定书文号</th>
             <td class="entry" id="punish_detail_penDecNo"></td>
         </tr>
         <tr>
             <th class="title">名称</th>
             <td class="entry" id="punish_detail_name"></td>
         </tr>
         <tr>
             <th class="title">统一社会信用代码/注册号</th>
             <td class="entry" id="punish_detail_regNo"></td>
         </tr>
                  <tr style="display:none">
             <th class="title">法定代表人（负责人）姓名</th>
             <td class="entry" id="punish_detail_leRep"></td>
         </tr>
         <tr>
             <th class="title">违法行为类型</th>
             <td class="entry" id="punish_detail_illegActType"></td>
         </tr>
         <tr>
             <th class="title">行政处罚内容</th>
             <td class="entry" id="punish_detail_penContent"></td>
         </tr>
         <tr>
             <th class="title">作出行政处罚决定机关名称</th>
             <td class="entry" id="punish_detail_penAuth_CN"></td>
         </tr>
         <tr>
             <th class="title">作出行政处罚决定日期</th>
             <td class="entry" id="punish_detail_PenDecIssDate"></td>
         </tr>

     </table>
     </div>
 </div>        <div id="bg"></div>

        <div class="classify" id="punishMentAll">行政处罚信息
        </div>
        <table class="display" id="needPaging_punish">
            <thead>
            <tr>
                <th style="padding: 0">
                    <div class="specialfuckth">
                        <table frame='void' rules='rows' width="1070px;">
                            <thead>
                            <tr>
                                <th width="48px">序号</th>
                                <th class="sorting_disabled" width="151px">决定书文号</th>
                                <th class="sorting_disabled" width="112px">违法行为类型</th>
                                <th class="sorting_disabled" width="140px">行政处罚内容</th>
                                <th class="sorting_disabled" width="197px">决定机关名称</th>
                                <th class="sorting_disabled" width="120px">处罚决定日期</th>
                                <th class="sorting_disabled" width="120px">公示日期</th>
                                <th class="sorting_disabled" width="48px">详情</th>
                            </tr>
                            </thead>
                        </table>
                    </div>
                </th>
            </tr>
            </thead>
        </table>
    </div></div>

                
                <div class='content-i' id="content4" style="display: none"><div class="warning_abnormal" id="excep_tab">
    <div class="classify">
        经营异常信息
    </div>
    <table class="display" id="needPaging_abnormal" >
        <thead>
        <tr>
            <th width="6%">序号</th>
            <th>标记经营异常状态原因</th>
            <th>列入日期</th>
            <th width="12%">作出决定机关(标记)</th>
            <th>恢复正常记载状态原因</th>
            <th>移出日期</th>
            <th width="15%">作出决定机关(恢复)</th>
        </tr>
        </thead>
    </table>
</div>
</div>

               
                <div class='content-i' id="content5" style="display: none"></div>

            </div>
        </div>
    </div>
</div>
</div>
</div>
<div class="back-to-nav">返回导航</div>

<script>  
        var displaylabel = 1;
			
</script>
</div>
<div class="footer3" style="padding-bottom: 20px;">
   	<div class="footer_info1" style="padding-top: 20px;">
        <div>主办单位：中华人民共和国国家工商行政管理总局</div>
        <div>地址：北京市西城区三里河东路八号&nbsp;&nbsp;&nbsp;邮政编码：100820&nbsp;&nbsp;&nbsp;备案号：京ICP备16053442号-1</div>
        <div class="connect-link"><input type="hidden" value="100000" id="subsite"/><a href="/tel.html" target="_blank" style="color:#ff2020">业务咨询与技术支持联系方式</a></div>
        <input type="hidden" value="56709@GSZJ_IDC_GSXT_WB_QTWEB_014"/>
    </div>
    <!--
    <div style="position: absolute;right:20%;top:25px;width: 140px;height: 55px;" id="imgBox"><img onclick="Link('bm30000013')" style='margin:0;border:0;cursor: pointer;' src="http://121.43.68.40/exposure/images/jiucuo.png?v=bm30000013"></div>
    -->
</div></body>
</html>
'''
